from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picture')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'category'

    def __str__(self):
        return '{}'.format(self.name)

# Create your models here.
