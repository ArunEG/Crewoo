from django.db import models

class Timestampable(models.Model):
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    lastmod_by = models.ForeignKey(User)
    lastmod_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publishable(models.Model):
    published_on = models.DateTimeField(null=True)
    published_by = models.ForeignKey(User)

    class Meta:
        abstract = True