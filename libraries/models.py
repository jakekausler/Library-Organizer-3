from django.db import models
from users.models import User


class Library(models.Model):
	name = models.CharField(max_length=255, default="")
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	sort_method = models.TextField(default="")

	def __str__(self):
		return self.name
