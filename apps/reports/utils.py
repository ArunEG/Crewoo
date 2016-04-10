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

def get_project_as_pdf(request, data):
	""" The function will retun project info in pdf format
			@Author  : Arun Gopi
			@date    : 3/4/2016
	"""

	filename = 'project_info.pdf'
	response = PDFTemplateResponse(request=request,
								   template='reports/pdf/project_info.html',
								   filename=filename,
								   context=data,
								   show_content_in_browser=False,
								   cmd_options={
									   'encoding': 'utf8', 'quiet': True}
								   )
	return response