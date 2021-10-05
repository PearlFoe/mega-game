from django.db import models

class Article(models.Model):
	"""
	Модель статей, которые будут выкладываться
	участниками во время мероприятия
	"""
	title = models.CharField(max_length=300)
	description = models.TextField()
	creation_date = models.DateTimeField()
	created_by = models.ForeignKey('User', on_delete=models.PROTECT)
	event = models.ForeignKey('Event', on_delete=models.CASCADE)

	class Meta:
		db_table = 'articles'
		ordering = ['-creation_date']

	def __str__(self):
		return self.title
