from django.db import models

class File(models.Model):
    file = models.FileField(upload_to= 'files/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(verbose_name='Обработан', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'