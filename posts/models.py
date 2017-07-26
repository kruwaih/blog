from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	image = models.ImageField(upload_to="blog_image", null=True, blank=True)
	updated = models.DateTimeField(auto_now = True)
	timestamp =  models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ("posts:detail", kwargs = {"post_id": self.id})

	class Meta:
		ordering = ['-timestamp'] #for ordering everything by defult