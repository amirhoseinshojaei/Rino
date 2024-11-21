from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not first_name:
            raise ValueError('نام خود را وارد کنید')

        if not last_name:
            raise ValueError('نام خانوادگی خودرا وارد کنید')

        if not email:
            raise ValueError('ایمیل خود را وارد کنید')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # SuperUser section
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# Custom User
class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    user_name = models.CharField(max_length=50, verbose_name='نام کاربری')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    @property
    def username(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.user_name = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True






