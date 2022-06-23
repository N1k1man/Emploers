from django.db import models
from django.urls import reverse

CHOICES = (
    (True, 'Посетил(а)'),
    (False, 'Отсутствовал(а)')
)


class Position(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employers/')
    stack = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('employer', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    visited = models.BooleanField(choices=CHOICES)
    time_start = models.TimeField(blank=True, null=True, default='00:00')
    time_end = models.TimeField(blank=True, null=True, default='00:00')
    reason = models.CharField(max_length=255, default='-----', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Сотрудник {self.employer.name}'

    class Meta:
        ordering = ['-date']




