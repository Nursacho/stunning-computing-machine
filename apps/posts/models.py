from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название место'
    )
    image = models.ImageField(
        upload_to='department',
        null=True, blank=True,
        verbose_name='Изображение заведения'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )
    create_at = models.DateTimeField(
        verbose_name='Дата созданий',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title

