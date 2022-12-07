from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="название товара",
        help_text="введите название товара"
    )
    price = models.PositiveIntegerField(
        verbose_name="цена товара",
        help_text="укажите цену товара"
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="описание товара",
        help_text="опишите ваш товар"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="автор",
        help_text="укажите автора"
    )
    image = models.ImageField(
        upload_to="ads/photos/",
        verbose_name="фото объявления",
        help_text="разместите фото для объявления",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время создания"
    )

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"
        ordering = ("-created_at",)


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="текст комментария",
        help_text="введите текст комментария"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="автор",
        help_text="укажите автора"
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="объявление",
        help_text="объявление,к которому относится комментарий"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время создания"
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ("-created_at",)
