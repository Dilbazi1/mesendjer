from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from members.models import Members
User = get_user_model()

class Group(models.Model):
	uuid = models.UUIDField(default=uuid4, editable=False)
	members = models.ManyToManyField(User)


	def add_user(request, user):
		self.members.add(user)
		self.save()
		return

	def remove_user(request, user):
		self.members.remove(user)
		self.save()
		return


class Message(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Room_Message(models.Model):
		room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
		user = models.ForeignKey(Members, related_name='messages', on_delete=models.CASCADE)
		content = models.TextField()

		date_added = models.DateTimeField(auto_now_add=True)

		class Meta:
			ordering = ('date_added',)