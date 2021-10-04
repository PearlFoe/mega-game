from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=300)
	description = models.TextField()
	start_date = models.DateTimeField()
	participants_count = models.IntegerField()
	#participants_id_list = models.

	class Meta:
		db_table = 'events'
		ordering = ['-creation_date']

	def __str__(self):
		return self.name