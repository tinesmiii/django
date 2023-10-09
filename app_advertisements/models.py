from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField(verbose_name="Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"advertisement(id = {self.id}, title = {self.title}, price = {self.price})"