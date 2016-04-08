import xlrd
from datetime import datetime
from .models import *


def get_or_none(classmodel, **kwargs):
	"""
		the function will get the from the Model if exist other
		wise will return none

		@author : Arun Gopi
		@date   : 3/4/2016
	"""
	try:
		return classmodel.objects.get(**kwargs)
	except classmodel.DoesNotExist:
		return None


def date_from_excel(d, dm):
	"""
		return date from excel file

		@author : Arun Gopi
		@date   : 6/4/2016
	"""

	if d:

		try:
			if isinstance(d, float) or isinstance(d, int):
				year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(
					d, dm)
				d = "%04d-%02d-%02d" % (year, month, day)
			elif isinstance(d, str) or isinstance(d, unicode):
				d = datetime.strptime(d, '%d-%m-%Y %I:%M')
			else:
				print "ERROR : Unknown datatype", type(d)
		except ValueError:
			d = None
	else:
		d = None
	return d


def create_project_info(data):
	"""
		the function will 
		create a new record in project_info Table

		@author : Arun Gopi
		@date   : 7/4/2016
	"""
	
	project = ProjectInfo()
	project.name = data['name']
	project.description = data['description']
	project.start_date = data['start_date']
	project.end_date = data['end_date']
	project.save()
	print 'Inserted'
	return True

def update_project_info(data):
	"""
		the function will update
		ProjectInfo table if you pass PK

		@author : Arun Gopi
		@date   : 7/4/2016
	"""
	if 'pk' in data:
		if data['pk'] is not None:
			project = get_or_none(ProjectInfo, pk=data['pk'])
			if project:
				project.name = data['name']
				project.description = data['description']
				project.start_date = data['start_date']
				project.end_date = data['end_date']
				project.save()
				print 'Updated'
				return True
			else:
				return False
		else:
			return False

	else:
		print "please provide pk for updating"
		return False

