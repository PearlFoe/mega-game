from django.db import models

import datetime

class Event(models.Model):
	"""
	Модель мероприятий, которые будут проводиться
	"""
	name = models.CharField(max_length=300)
	description = models.TextField()
	start_date = models.DateTimeField(null=True)
	creation_date = models.DateTimeField()
	created_by = models.ForeignKey('User', on_delete=models.PROTECT)

	class Meta:
		db_table = 'events'
		ordering = ['-creation_date']

	def __str__(self):
		return self.name

	def get_event_status(self):
		if not self.start_date:
			return 'START_DATE_UNDEFINED'
		if datetime.date.today() > self.start_date:
			return 'FINISHED'
		elif datetime.date.today() == self.start_date:
			return 'IN_PROGRESS'
		else:
			return 'NOT_STARTED'