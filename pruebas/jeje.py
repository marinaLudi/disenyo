from sqlalchemy import *

engine = create_engine('postgresql://marina:mari@localhost/marina')
metadata = MetaData(engine)

pasajero = Table('pasajero',metadata, autoload=True)

s = pasajero.select()
rs = s.execute()

row = rs.fetchall()
for a in row:
	print 'nombre', a.quien
	
