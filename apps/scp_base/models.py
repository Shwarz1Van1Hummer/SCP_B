from django.db import models
from scp.settings import MEDIA_ROOT
from static.static_root import SAFE


class SCP(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPEuclid(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPKetter(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPThaumiel(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'id',

        )
