from django.db import models

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	open = models.FloatField()  #price at start of day
	close = models.FloatField() # #price at end of day
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker

