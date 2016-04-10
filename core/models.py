from __future__ import unicode_literals

from django.db import models

# Create your models here.
class todo(models.Model):
	name = models.CharField(max_length=250, unique=True)
	desc = models.TextField()
	completed = models.BooleanField(default=False)
	completed_on = models.DateTimeField(editable=False, default=None)
	time_completed = models.DurationField(editable=False, default= None) #time took to complete
	created_on = models.DateTimeField(editable=False, auto_now_add=True)
	modifed_on = models.DateTimeField(editable=False, auto_now=True)

	def __unicode__(self):
		return self.name
	


