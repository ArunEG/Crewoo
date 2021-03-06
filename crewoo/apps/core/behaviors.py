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


class Permalinkable(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True

    def get_url_kwargs(self, **kwargs):
        kwargs.update(getattr(self, 'url_kwargs', {}))
        return kwargs

    @models.permalink
    def get_absolute_url(self):
        url_kwargs = self.get_url_kwargs(slug=self.slug)        
        return (self.url_name, (), url_kwargs)

    def pre_save(self, instance, add):
        from django.utils.text import slugify
        if not instance.slug:
            instance.slug = slugify(self.slug_source)


class Scheduleable(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True
