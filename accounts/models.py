from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Create user

        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return: User
        """
        if not email:
            raise ValueError("Users must have an email address")

        if not first_name:
            raise ValueError("Users must have a first name")

        if not last_name:
            raise ValueError("Users must have a last name.")

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates super user
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return:
        """
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """
    Class for representing Custom user
    """
    first_name = models.CharField(max_length=20, verbose_name="First name")
    last_name = models.CharField(max_length=20, verbose_name="Last name")
    email = models.EmailField(unique=True, verbose_name="Email address", max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email






