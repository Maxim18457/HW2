
from django.contrib import admin
from .models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','price','title','updated_at','auction','description','get_html_image','updated_date']
    list_filter = ['price','updated_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = (
        ('Общее',{
            'fields':('title','description','image'),
            'classes':['collapse']
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать все торги')
    def make_auction_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Проставить возможность торгов')
    def make_auction_true(self, request, queryset):
        queryset.update(auction = True)
  

admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.


#   list_display = ['created_at','price','title','updated_at','auction','description']
#     list_filter = ['price','updated_at']
#     actions = ['make_auction_false','make_auction_true']
#     fieldsets = (
#         ('Общее',{
#             'fields':('title','description'),
#             'classes':['collapse']
#         }),
#         ('Финансы',{
#             'fields':('price','auction'),
#             'classes':['collapse']
#         })
#     )

#     @admin.action(description='Убрать все торги')
#     def make_auction_false(self, request, queryset):
#         queryset.update(auction = False)

#     @admin.action(description='Проставить возможность торгов')
#     def make_auction_true(self, request, queryset):
#         queryset.update(auction = True)