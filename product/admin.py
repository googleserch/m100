from django.contrib import admin
from .models import categories , post,order,amount


class categoriesadmin(admin.ModelAdmin):
    list_display=('title','description','url','add_date')
    search_fields=('title',)
   

class postadmin(admin.ModelAdmin):
    list_display=('name','category','type','deals','phone_number','location')
    search_fields=('name','category','phone_number','type','deals')  
    list_filter=('category',)  
    list_per_page=50

   
class order_admin(admin.ModelAdmin):
    list_display=('user','amount','order_id','payment_status','start','date')
class amount_admin(admin.ModelAdmin):
    list_display=('s_amount',)


# Register your models here.


admin.site.register(categories,categoriesadmin)
admin.site.register(post,postadmin)
admin.site.register(order,order_admin)
admin.site.register(amount,amount_admin)