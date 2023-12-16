from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,User

class MembersManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
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
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
		room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
		user = models.ForeignKey(Members, related_name='messages', on_delete=models.CASCADE)
		content = models.TextField()

		date_added = models.DateTimeField(auto_now_add=True)

		class Meta:
			ordering = ('date_added',)
