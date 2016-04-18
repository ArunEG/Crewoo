from django.db import models

class ProjectManager(models.Manager):
	"""docstring for ProjectManager"""
	def active(self):
		"""
			this manager will return all the active objects.
			means is_deleted = 0

			@Author : Arun Gopi
			@Date   : 9/4/2016
		"""
		return self.get_queryset().filter(is_deleted=False)


		