from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Категория {self.title}'


class Task(models.Model):
    LOW = 'LW'
    MIDDLE = 'MD'
    HIGH = 'HG'

    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MIDDLE, 'Средний'),
        (HIGH, 'Высокий'),
    ]

    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(
        null=True,
        blank=True
    )
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=LOW
    )
    done = models.BooleanField(default=False)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    class Meta:
        ordering = ['deadline', '-done']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача {self.title}'
