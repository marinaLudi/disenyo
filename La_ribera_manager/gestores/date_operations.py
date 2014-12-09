#### Operaciones para Date ####
import datetime

def daterange(start_date, end_date):
	if start_date < end_date:
		for n in range((end_date - start_date).days + 1):
			yield start_date + datetime.timedelta(n)


def is_in_between(date, start, end):
	return start <= date <= end
