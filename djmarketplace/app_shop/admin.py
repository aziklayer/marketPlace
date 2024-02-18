from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'status_flag']
    list_filter = ['status_flag']

class CategoryAdmin(admin.ModelAdmin):
    model = GoodCategory
    list_display = ['name']

class GoodInLine(admin.TabularInline):
    model = Good
    extra = 1

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GoodInLine]

class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'price', 'amount']
    list_filter = ['shop', 'category', 'activity_flag']
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, queryset):
        queryset.update(activity_flag='a')

    def mark_as_inactive(self, queryset):
        queryset.update(activity_flag='i')

    mark_as_active.short_description = 'Пометить как активная'
    mark_as_inactive.short_description = 'Поместить в стоп лист'


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'good', 'good_num', 'payment_flag']
    list_filter = ['user', 'good', 'payment_flag']

# class GoodsCartInLine(admin.TabularInline):
#     model = GoodCart.good.through

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    # inlines = [GoodsCartInLine]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(GoodCategory, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(GoodCart, CartAdmin)
admin.site.register(Order, OrderAdmin)
