from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from .choices import USER_TYPE


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.user_type = 'user'
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.user_type = 'user'
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField('Фото профиля', upload_to='user_avatar/', null=True, blank=True)
    passport_photo = models.ImageField('Фото пасспорта', upload_to='user_passport_photo/', blank=True, null=True)
    created = models.DateField('Дата создания', auto_now_add=True, null=True, blank=True)
    updated = models.DateField('Дата обновления', auto_now=True, null=True, blank=True)
    username = models.CharField('Имя пользователя', max_length=255, unique=True)
    fullname = models.CharField('Полное имя', max_length=255, null=True, blank=True)
    address = models.TextField(verbose_name='Адрес прописки', null=True, blank=True)
    phone = models.CharField(max_length=200, verbose_name='Номер телефона', null=True, blank=True)
    email = models.CharField('Email', max_length=255, null=True, blank=True)
    birth_day = models.DateField(verbose_name='Дата рождение', max_length=255, null=True, blank=True)
    user_type = models.CharField('Тип пользователя', max_length=255, choices=USER_TYPE)
    salary = models.FloatField(verbose_name='Зарплата', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return str(self.fullname) if self.fullname else str(self.username)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
