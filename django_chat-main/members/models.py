from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,User
from django.utils import timezone
class MembersManager(BaseUserManager):

	def create_user(self, username, email=None, password=None):

		if not email:
			raise ValueError('An email is required.')


		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_staff=True

						  )

		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self,username, email, password):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(username,email, password)
		user.is_superuser = True
		user.save()
		return user


class Members(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	country = models.CharField(max_length=100)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	is_staff = models.BooleanField(default=False)
	objects = MembersManager()
	def __str__(self):
		return self.username

