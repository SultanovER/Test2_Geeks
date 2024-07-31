from django.db import models

class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    name = models.CharField(max_length=100, verbose_name='Название')
    duration = models.DurationField(verbose_name='Продолжительность')
    director = models.CharField(max_length=100, verbose_name='Режиссёр')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.name

