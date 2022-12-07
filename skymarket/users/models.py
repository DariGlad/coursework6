from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, USER),
        (ADMIN, ADMIN)
    )


class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(
        max_length=64,
        verbose_name="имя",
        help_text="введите имя (максимальное количество символов - 64)"
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name="фамилия",
        help_text="введите фамилию (максимальное количество символов - 64)"
    )
    phone = PhoneNumberField(
        max_length=128,
        verbose_name="телефон",
        help_text="укажите номер телефона"
    )
    email = models.EmailField(
        verbose_name="электронная почта",
        unique=True,
        help_text="укажите адрес электронной почты"
    )
    role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="роль",
        help_text="выберите роль пользователя"
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="фото",
        help_text="разместите ваше фото",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name="аккаунт активен",
        help_text="укажите активность аккаунта"
    )

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
