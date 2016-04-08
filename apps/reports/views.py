from django.shortcuts import render
from .lib import *
from wkhtmltopdf.views import PDFTemplateResponse
from apps.reports.models import ProjectInfo
from django.http import Http404
import xlwt
import xlrd
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.contrib import messages


def insertcolx():
	"""
			Excel row/colum style for excel
			@Author  : Arun Gopi
			@date    : 3/4/2016
	"""

	style = xlwt.XFStyle()
	borders = xlwt.Borders()
	borders.bottom = borders.top = borders.left\
		= borders.right = xlwt.Borders.THIN
	borders.top = xlwt.Borders.THIN
	style.borders = borders
	style.pattern.pattern = 26
	style.pattern.pattern_fore_colour = 0x16
	style.protection.cell_locked = False
	style.protection.formula_hidden = False
	return style


def upload_file(request):
	"""
			The view use for upload files

			@Author : Arun Gopi
			@date   : 6/4/2016
	"""
	sheetname = 'ProjectInfo'
	return_data = {}

	if 'project_info_excel' in request.FILES:

		upload_excel = request.FILES['project_info_excel'].read()
		try:
			work_book = xlrd.open_workbook(file_contents=upload_excel)
		except:
			messages.error(
				request, 'You are trying to uplaod a file that is not supported. Please select the downloaded file only.')
			return HttpResponseRedirect(reverse('projects', args=[]))

		try:
			worksheet = work_book.sheet_by_name(sheetname)
		except:
			messages.error(
				request, 'You are trying to uplaod a wrong file. Please upload a file with sheet name ' + sheetname + '.')
			return HttpResponseRedirect(reverse('projects', args=[]))

		rows = worksheet.nrows
		cols = worksheet.ncols

		row = 1
		for row in range(1,rows):
			data = {}
			data['name'] = worksheet.cell_value(row, 0)
			data['description'] = worksheet.cell_value(row, 1)

			data['start_date'] = date_from_excel(
				worksheet.cell_value(row, 2), work_book.datemode)
			data['end_date'] = date_from_excel(
				worksheet.cell_value(row, 3), work_book.datemode)
			data['pk'] = worksheet.cell_value(
				row, 4) if worksheet.cell_value(row, 4) else None

			if data['pk']:
				update_project_info(data)
			else:
				create_project_info(data)

		return HttpResponseRedirect(reverse('projects'))
	return render(request, 'reports/upload.html', return_data)


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


def get_project_as_excel(project):
	""" The function will retun project info in excel format
			@Author  : Arun Gopi
			@date    : 3/4/2016
	"""

	row_num, col_num = 0, 0
	work_book = xlwt.Workbook(encoding='utf-8')
	work_sheet = work_book.add_sheet("ProjectInfo")
	insertcol = insertcolx()
	# work_sheet.col(4).hidden = True
	lables = ["Name ", "Overview", "Start date", "Start date"]
	for label in lables:
		work_sheet.write(row_num, col_num, label, insertcol)
		work_sheet.col(col_num).width = 5000
		col_num += 1
	row_num += 1
	work_sheet.write(row_num, 0, str(project.name), insertcol)
	work_sheet.write(
		row_num, 1, str(strip_tags(project.description)), insertcol)
	work_sheet.write(
		row_num, 2, project.start_date.strftime('%d-%m-%Y %H:%M'), insertcol)
	work_sheet.write(
		row_num, 3, project.end_date.strftime('%d-%m-%Y %H:%M'), insertcol)
	work_sheet.write(
		row_num, 4, project.pk, insertcol)

	response = HttpResponse(content_type='application/ms-excel')
	file_name = "ProjectInfo"+'.xls'
	response['Content-Disposition'] = 'attachment; filename="'+file_name+'"'
	work_book.save(response)
	return response


def projects(request, project_id=None, download=None):
	"""
			The view use for get the project list or project info as PDF or excel
			@Author : Arun Gopi
			@Date   : 3/4/2016
	"""

	data = {}
	if project_id:
		project = get_or_none(ProjectInfo, pk=project_id)
		if project:
			if download == 'pdf':
				data['project'] = project
				response = get_project_as_pdf(request, data)
				return response
			elif download == 'excel':
				response = get_project_as_excel(project)
				return response
			else:
				raise Http404
		else:
			raise Http404
	else:
		projects = ProjectInfo.objects.filter(is_deleted=False)
		return render(request, 'reports/projects.html', {'projects': projects})
