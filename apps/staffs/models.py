from django.db import models
from django.contrib.auth.models import User

GENDER = (('F','Female'),('M','Male'))
USER_GROUPS = (('TL','Team Lead'),('PM','Project Manager'),('OT','Other'))
class Staff(User):
	gender = models.CharField(choices=GENDER,max_length=1,verbose_name=u'Gender')
	image = models.ImageField(upload_to = "Staffs/",verbose_name = "Image",blank = True,null=True)
	mobile = models.CharField(max_length=100,null=True,blank=True)
	address = models.TextField(verbose_name=u'Address',null=True,blank=True)
	dob = models.DateField(verbose_name ="DOB",null=True,blank=True)
	user_type = models.CharField(choices=USER_GROUPS, max_length=2,default='OT')
	is_first_login = models.BooleanField(default=False)

	class Meta:
		verbose_name = ('Staff')
		verbose_name_plural = ('Staffs')

	def __unicode__(self):
		return self.first_name+" "+self.last_name

	def image_display(self):
		if not self.image:
			return '/static/assets/img/nouser.png'
		else:
			return self.image.url