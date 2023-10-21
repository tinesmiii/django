from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField(verbose_name="Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, verbose_name="Пользователь", on_delete=models.CASCADE)

    image = models.ImageField(verbose_name="изображение", upload_to="advertisements/")

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

    @admin.display(description="Изображение")
    def image_mini(self):
        if self.image:
            return format_html("<img src='{}' style = 'width:40px;'>", self.image.url)