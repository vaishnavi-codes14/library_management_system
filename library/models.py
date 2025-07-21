from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Resolve conflicts with default User model
    groups = models.ManyToManyField(
        Group,
        related_name="adminuser_groups",  # Custom related name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="adminuser_permissions",  # Custom related name
        blank=True,
    )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title