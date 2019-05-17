from django.db import models


class User(models.Model):
	user = models.CharField(max_length=32, unique=True)
	password = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	reset_token = models.CharField(max_length=255, default="")
	reset_expiration = models.DateTimeField(null=True, default=None)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	icon_url = models.CharField(max_length=255)

	def __str__(self):
		return self.user
