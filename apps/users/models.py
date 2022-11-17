from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


# user model creation


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("the email is not valid")
        user = self.model(email=self.normalize_email(email), password=password,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, default='')
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50, null=False, default='')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    class Meta:
        ordering = ['first_name']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perms(self, perm, obj=None):
        return self.is_admin
