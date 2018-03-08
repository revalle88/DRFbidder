from django.db import models

# Create your models here.


class Campaign(models.Model):
	name = models.CharField(max_length=128)
	directId = models.CharField(max_length=128)
#created_at = models.DateTimeField(_('created at'), auto_now_add=True)
#announce_text = models.TextField(_('announce'), max_length=512, blank=True)
#text = models.TextField(_('text'), max_length=4096)

	def __str__(self):
		return self.name

class Keyword(models.Model):
	keyword = models.CharField(max_length=128)
	directId = models.CharField(max_length=128)
	bid = models.CharField(max_length=128)
	campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE)


	def __str__(self):
		return self.keyword