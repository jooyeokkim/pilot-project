from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password): # 재정의
        if not username or not email or not password:
            raise ValueError("fill all blanks")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password): # 재정의
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField('EMAIL', max_length=255, unique=True)
    username = models.CharField('USERNAME', max_length=150, unique=True)

    def __str__(self):
        return self.email
