from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Flowers(models.Model):
    title = models.CharField("Цветы", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категории")
    company = models.CharField("ZAMI_flowers", max_length=100)
    price = models.CharField("Цена", max_length=80, default="без опыта")
    description = models.TextField("Описание")
    image = models.CharField("URL-фото", max_length=500)
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефон", max_length=14)
    email = models.CharField("E-mail", max_length=100)
    created_ad = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Цветы"
        verbose_name_plural = "Цветы"

    def __str__(self):
        return self.title

class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    descriptions = models.TextField("Описание гайда")
    image = models.CharField("URL-фото", max_length=500)
    crеated_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Гайд"
        verbose_name_plural = "Гайды"

    def __str__(self):
        return self.title