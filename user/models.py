from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

""" Custom User model has one field less than the Django Original, it is important to modify its Manager """

class UserManager(BaseUserManager):
    # DEFINE A MODEL MANAGER FOR USER MODEL WITH NO 'username' field

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ create and save a regular User with the email and password """
        extra_fields.setdefault('is_stuff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ create and save a SuperUser with the given email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_stuff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have isv_superuser=True')

        return self._create_user(email, password, **extra_fields)

# User model
class User(AbstractUser):
    class Meta:
        db_table = "user"
    username = None
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(('email'),max_length=100, unique=True)
    password = models.CharField(max_length=255)
    phone = PhoneNumberField(unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()