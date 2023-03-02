from django.contrib import admin
from .models import Category,Product,PaymentMaster
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id",'category_name')

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','pname','price','description','quantity','image','cat')

class PaymentMasterAdmin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(PaymentMaster,PaymentMasterAdmin)