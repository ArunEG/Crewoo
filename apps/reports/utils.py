from apps.reports.models import *

def create_project(data):
	"""
		The fnction will create a recored in ProjectInfo table
		@author : Arun
		@date : 9/4/2016

	"""
	project = ProjectInfo()
	project.name = data['name']
	project.description = data['description']
	project.start_date = data['start_date']
	project.end_date = data['end_date']
	project.save()
	return True