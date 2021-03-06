#!/usr/bin/python
#### Interfaz Mostrar Estado Habitacion ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk
from gestores.gestorcombos import GestorCombos
from gestores.gestordialogos import GestorDialogos
from gestores.gestorMostrarEstadoHab import GestorMostrarEstadoHab
import interfaces.interfazOcuparHabitacion
from datetime import timedelta,date,datetime

# Globals
BORDE_ANCHO = 25
VENTANA_ANCHO = 530
VENTANA_ALTO = 735


class InterfazEstadoHabitacion:
    def __init__(self,menu):

        self.menu = menu

        builder = Gtk.Builder()
        builder.add_from_file("estado_habitacion.xml")

        # Obtenemos ventana
        self.window = builder.get_object("window")
        self.window.set_border_width(BORDE_ANCHO)
        self.window.set_default_size(VENTANA_ALTO, VENTANA_ANCHO)

        # Obtenemos combos de la interfaz
        self.dia_ini_combo = builder.get_object("dia_ini_combo")
        self.mes_ini_combo = builder.get_object("mes_ini_combo")
        self.ano_ini_combo = builder.get_object("ano_ini_combo")

        self.dia_fin_combo = builder.get_object("dia_fin_combo")
        self.mes_fin_combo = builder.get_object("mes_fin_combo")
        self.ano_fin_combo = builder.get_object("ano_fin_combo")

        self.scrolled_window = builder.get_object("scrolled_window")
        self.scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)
        self.tree = Gtk.TreeView()
        self.scrolled_window.add(self.tree)

        self.gestorDialogos = GestorDialogos()
        self.gestor_estado = GestorMostrarEstadoHab()

        # Gestorcombos se ocupa de cargar los combos con info
        self.gestorCombos = GestorCombos()

        self.gestorCombos.initDateCombo(self.dia_ini_combo,
                self.mes_ini_combo,
                self.ano_ini_combo,datetime.today().year,datetime.today().year)

        self.gestorCombos.initDateCombo(self.dia_fin_combo,
                self.mes_fin_combo,
                self.ano_fin_combo,datetime.today().year,datetime.today().year + 2)

        # Seteamos items activos
        self.gestorCombos.setActive([self.dia_ini_combo,
            self.mes_ini_combo,
            self.ano_ini_combo,
            self.dia_fin_combo,
            self.mes_fin_combo,
            self.ano_fin_combo],
                [0, 0, 0, 0, 0, 0])

        # Conectamos las senales con sus funciones
        handlers = {
            "onDeleteWindow": Gtk.main_quit,
            "onButtonClicked": self.mostrarHabitaciones,
            "onComboIniChanged": self.comboIniChanged,
            "onComboFinChanged": self.comboFinChanged
        }
        builder.connect_signals(handlers)

        # Monstramos ventana
        self.window.show_all()


    def comboIniChanged(self, combo):
        self.gestorCombos.comboUpDate(self.dia_ini_combo,
                self.mes_ini_combo,
                self.ano_ini_combo)


    def comboFinChanged(self, combo):
        self.gestorCombos.comboUpDate(self.dia_fin_combo,
                self.mes_fin_combo,
                self.ano_fin_combo)


    def mostrarHabitaciones(self, combo):
        fecha_ini = self.gestorCombos.getDate(self.dia_ini_combo,
                self.mes_ini_combo,
                self.ano_ini_combo)


        fecha_fin = self.gestorCombos.getDate(self.dia_fin_combo,
                self.mes_fin_combo,
                self.ano_fin_combo)


        if self.gestor_estado.validarFecha(fecha_ini, fecha_fin):
            self.scrolled_window.remove(self.tree)
            self.armarGrilla(fecha_ini,fecha_fin)

        else:
            self.gestorDialogos.confirm("La fecha inicial no puede ser mayor que la final",
                    "Aceptar")



    def armarGrilla(self,fecha_inicio,fecha_fin):

        #crea la lista de donde va a tomar las cosas el toggle, el boolean activado o no
        #los colores seria rojo=ocupada, azul=libre y amarillo=reservada
        #la ultima columna seria la fecha
        self.store = Gtk.ListStore(str)
        self.tree = Gtk.TreeView(self.store)
        for fecha in self.daterange(fecha_inicio, fecha_fin):
            treeiter = self.store.append([str(fecha)])


        renderer = Gtk.CellRendererText()

        column = Gtk.TreeViewColumn("Fecha\hab", renderer, text=0)
        self.tree.append_column(column)

        self.estados = self.gestor_estado.selectHab(fecha_inicio, fecha_fin)
        self.stores = []
        columns = []
        renderers = []
        num = 0

        for e in self.estados:
            self.stores.append(Gtk.ListStore(bool,str,str,str))

            i = 0
            for fecha in self.daterange(fecha_inicio, fecha_fin):
                self.stores[num].append([False,e[3][i],e[2][i],str(fecha)])
                i = i + 1

            renderers.append(Gtk.CellRendererToggle())
            columns.append(Gtk.TreeViewColumn(str(e[0])+" \n"+str(e[1].getTipo().getDescripcion()), renderers[num]))
            columns[num].set_cell_data_func(renderers[num], self.inIta, self.stores[num])
            self.tree.append_column(columns[num])
            renderers[num].connect("toggled", self.on_cell_toggled,num)

            num = num + 1

        self.fecha_ini = None
        self.primerCelda = [None, None]
        self.fecha_fin = None


        self.scrolled_window.add(self.tree)
        self.window.show_all()

    # Devuelve true si son iguales
    def compararCelda(self,path1,num1,path2,num2):
        if path1==path2 and num1==num2:
            return True

    def on_cell_toggled(self, widget, path, num):
        if self.compararCelda(self.primerCelda[0],self.primerCelda[1],int(path),num):
            self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
            self.fecha_ini=None

        elif self.fecha_ini is None:
            self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
            self.fecha_ini = self.stores[num][int(path)][3]
            self.primerCelda[0]=int(path)
            self.primerCelda[1]=num
            self.pos_ini = int(path)

        elif self.fecha_fin is None:
            if num != self.primerCelda[1] or int(path)<self.primerCelda[0]:
                self.resetearGrilla(num,path)
            else:
                self.fecha_fin = self.stores[num][int(path)][3]
                self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
                validacion = self.gestor_estado.validarRango(self.stores[num],
                        self.primerCelda[0],
                        int(path),
                        self.estados[num][1])

                if validacion == False:

                    self.resetearGrilla(num,path)
                else:
                    self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
                    self.fecha_fin = self.stores[num][int(path)][3]

                    validacion = self.gestor_estado.validarRango(self.stores[num],self.primerCelda[0],int(path),self.estados[num][1])
                    if validacion == False:
                        self.resetearGrilla(num,path)

                    elif validacion == True:
                        #pintamos las celdas de color ocupado
                        self.pintarCeldas(num,path)

                        if self.gestorDialogos.presTecla('PRESIONE CUALQUIER TECLA Y CONTINUA...'):
                            interfaces.interfazOcuparHabitacion.InterfazOcuparHabitacion(self.menu,self.fecha_ini,self.fecha_fin,self.estados[num][1])
                            self.window.hide()
                    else:
                        respuesta = self.gestorDialogos.confirm("Ya existe una reserva nombre de {2} {3} entre la fecha {0} y {1}".\
                        format(str(validacion[0]),str(validacion[1]),validacion[2],validacion[3]),"Ocupar Igual","Volver")

                        if respuesta == True:
                            self.pintarCeldas(num,path)
                            interfaces.interfazOcuparHabitacion.InterfazOcuparHabitacion(self.menu,self.fecha_ini,self.fecha_fin,self.estados[num][1])
                            self.window.hide()
                        else:
                            self.resetearGrilla(num,path)

    def pintarCeldas(self,num,path):
        for b in range(self.primerCelda[0],int(path)+1):
            self.stores[num][b][1] = 'red'

    def resetearGrilla(self,num, path):
        self.stores[num][int(path)][0] = False
        self.stores[self.primerCelda[1]][self.primerCelda[0]][0] = False  # lint:ok
        self.primerCelda = [None,None]
        self.fecha_ini = None
        self.fecha_fin = None



    def inIta(self,col, cell, model, iter, mymodel):
        s = model.get_string_from_iter(iter)
        niter = mymodel.get_iter_from_string(s)
        obj = mymodel.get_value(niter, 0)
        back = mymodel.get_value(niter,1)
        cell.set_property('active', obj)
        cell.set_property('cell-background',back)

    def daterange(self,start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)




if __name__ == '__main__':
    inter=InterfazEstadoHabitacion()
    Gtk.main()
