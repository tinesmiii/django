from django.contrib import admin
from .models import Advertisement
# Register your models here.

class AdvertisemntAdmin(admin.ModelAdmin):
    list_display=["id", "title", "description", "price", "auction", "created_date", "update_date"]
    list_filter = ["auction", "price", "created_at"]
    
    actions = ["make_auction_as_false", "make_auction_as_true"]

    fieldsets = (
        ("Общее", {
            "fields": ("title", "description")
        }),
        ("Финансы", {
            "fields": ("price", "auction"),
            "classes":["collapse"]
        })

    )

    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    


    @admin.action(description="добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)


admin.site.register(Advertisement, AdvertisemntAdmin)