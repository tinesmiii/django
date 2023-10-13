from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
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
    
    @admin.display(description="дата создания")
    def created_date(self):
 
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>",created_time)
        else:
            return self.created_at.strftime("%d:%m%y в %H:%M")

    @admin.display(description="дата обновления")
    def update_date(self):
    
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>", update_time)
        else:
            return self.update_at.strftime("%d:%m%y в %H:%M")

