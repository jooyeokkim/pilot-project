from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email, username, password): # 재정의
        if not username or not email or not password:
            raise ValueError("fill all blanks")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password): # 재정의
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractUser): # 일반 사용자가 관리자가 될 수도 있기 때문에 모두 상속
    objects = UserManager()
    email = models.EmailField('EMAIL', max_length=255, unique=True)
    username = models.CharField('USERNAME', max_length=150, unique=True)

    def __str__(self):
        return self.email

# 이메일만 따로 저장하는 테이블을 만들까 고민했었는데, 이메일 필드에 unique를 주고 is_active를 False로 주기만 하면 될 것 같다고 생각함