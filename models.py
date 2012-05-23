from django.db import models


class Menu(models.Model):
	name = models.CharField(max_length=100)
	enable = models.BooleanField(default=False)

class Starter(models.Model):
	menu = models.ForeignKey(Menu)
	name = models.CharField(max_length=100)
	price = models.IntegerField()

class Dishes(models.Model):
	menu = models.ForeignKey(Menu)
	name = models.CharField(max_length=100)
	price = models.IntegerField()

class Dessert(models.Model):
	menu = models.ForeignKey(Menu)
	name = models.CharField(max_length=100)
	price = models.IntegerField()

class Restaurant(models.Model):
	name = models.CharField(max_length=100)

class Zone(models.Model):
	number = models.IntegerField()
	restaurant = models.ForeignKey(Restaurant)

class Waiter(models.Model):
	name = models.CharField(max_length=15)
	zone = models.ForeignKey(Zone)
	
class Table(models.Model):
	zone = models.ForeignKey(Zone)

class Seat(models.Model):
	table = models.ForeignKey(Table)

class Order(models.Model):
	seat = models.ForeignKey(Seat)
	waiter = models.ForeignKey(Waiter)
	starter = models.ForeignKey(Starter)
	dishes = models.ForeignKey(Dishes)
	dessert = models.ForeignKey(Dessert)
	total_price = models.IntegerField()
	paid = models.BooleanField(default=False)



