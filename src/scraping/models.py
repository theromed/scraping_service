from django.db import models
from scraping.utils import from_cyrillic_to_eng
from django.utils.text import slugify

class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.CharField(max_length=64, blank=True, unique=True)

    class Meta:
        verbose_name='City name'
        verbose_name_plural = "City names"
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)



class Speciality(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.CharField(max_length=64, blank=True, unique=True)

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Title')
    company = models.CharField(max_length=250, verbose_name='Company name')
    description = models.TextField(verbose_name='Description')
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="City")
    speciality = models.ForeignKey("Speciality", on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = "Vacansies"

    def __str__(self):
        return self.title