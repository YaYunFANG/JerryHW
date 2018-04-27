from django.db import models

# Create your models here.
class Uname(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class Gender(models.Model):
	sexuality = models.CharField(max_length=20)
	name = models.ForeignKey(Uname)

	def __str__(self):
		return self.sexuality

class Birth(models.Model):
	date = models.CharField(max_length=10)
	name = models.ForeignKey(Uname)

	def __str__(self):
		return self.date

class Introduction(models.Model):
	intro = models.CharField(max_length=200)
	name = models.ForeignKey(Uname)

	def __str__(self):
		return self.intro