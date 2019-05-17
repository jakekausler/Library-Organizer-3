from django.db import models
from libraries.models import Library
from users.models import User


class Book(models.Model):
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255, default="")
	originally_published = models.DateField(null=True, default=None)
	publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
	is_read = models.BooleanField(default=False)
	is_reference = models.BooleanField(default=False)
	is_owned = models.BooleanField(default=False)
	isbn = models.CharField(max_length=13, default="")
	dewey = models.CharField(max_length=10)
	pages = models.IntegerField(default=0)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	depth = models.IntegerField(default=0)
	weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	primary_language = models.CharField(max_length=255, default="")
	secondary_language = models.CharField(max_length=255, default="")
	original_language = models.CharField(max_length=255, default="")
	series = models.CharField(max_length=255, default="")
	volume = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	format = models.CharField(max_length=255, default="")
	edition = models.IntegerField(default=1)
	image_url = models.CharField(max_length=255, default="")
	is_reading = models.BooleanField(default=False)
	is_shipping = models.BooleanField(default=False)
	spine_color = models.CharField(max_length=6, default="000000")
	cheapest_new = models.DecimalField(max_digits=10, decimal_places=2, default=99999999.99)
	cheapest_used = models.DecimalField(max_digits=10, decimal_places=2, default=99999999.99)
	edition_published = models.DateField(null=True, default=None)
	library = models.ForeignKey(Library, on_delete=models.CASCADE)
	loanee = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
	lexile = models.IntegerField(default=-1)
	spine_color_overridden = models.BooleanField(default=False)
	notes = models.TextField(default="")
	lexile_code = models.CharField(max_length=2, default="")
	interest_level = models.IntegerField(default=-1)
	ar = models.DecimalField(max_digits=2, decimal_places=1, default=-1.0)
	learning_az = models.IntegerField(default=-1)
	guided_reading = models.IntegerField(default=-1)
	dra = models.IntegerField(default=-1)
	grade = models.IntegerField(default=-1)
	founta_spinnell = models.IntegerField(default=-1)
	age = models.IntegerField(default=-1)
	reading_recovery = models.IntegerField(default=-1)
	pm_readers = models.IntegerField(default=-1)
	library_of_congress = models.CharField(max_length=32, default="")
	fiction_genre = models.CharField(max_length=255, default="")
	is_anthology = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class WrittenBy(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	author = models.ForeignKey("Person", on_delete=models.CASCADE)
	role = models.CharField(max_length=255, default="Author")

	def __str__(self):
		return self.book.title + " " + str(self.author) + " " + self.role


class Person(models.Model):
	first_name = models.CharField(max_length=255, default="")
	middle_names = models.CharField(max_length=255, default="")
	last_name = models.CharField(max_length=255)

	def __str__(self):
		return self.first_name + " " + " ".join(self.middle_names.split(";")) + " " + self.last_name


class Publisher(models.Model):
	publisher_name = models.CharField(max_length=255)
	city = models.CharField(max_length=255, default="")
	state = models.CharField(max_length=255, default="")
	country = models.CharField(max_length=255, default="")
	parent = models.ForeignKey("Publisher", null=True, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.publisher_name
