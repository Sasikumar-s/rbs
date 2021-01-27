from django.db import models

class Batch_entry(models.Model):
	Batch_name = models.CharField(max_length = 100, primary_key=True)
	Quantity = models.IntegerField()
	Chick_arrived = models.IntegerField()
	Arrived_date = models.DateField()
	Arrived_time = models.TimeField()
	Matralty = models.IntegerField()
	def __str__(self):
		return self.Batch_name

class Production(models.Model):
	Batch_detail = models.ForeignKey(Batch_entry,on_delete = models.CASCADE)
	Trays = models.IntegerField()
	Feed = models.IntegerField()
	Medicine = models.CharField(max_length=50)
	Matralty_on_days = models.IntegerField(default = 0)

	

