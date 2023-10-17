from django.contrib import admin
from django.forms import DateTimeField
from .models import Banner,Category,Brand,Color,Size,Product,ProductAttribute,CartOrder,CartOrderItems,ProductReview,WishList,UserAddressBook,SaleSummary
from django.db.models import Max,Min,Avg,Count,Sum
from django.db.models.functions import Trunc
# Register your models here.

admin.site.register(Brand)
admin.site.register(Size)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','brand','color','size','status','is_featured')
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)



class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ('paid_status','order_status')
    list_display = ('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)

admin.site.register(WishList)


class UserAddressBookAdmin(admin.ModelAdmin):
    list_display = ('id','user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)




class OrderSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'sale_summary_change_list.html'
    # date_hierarchy = 'created'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )


        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        metrics = {
            'total': Count('id'),
            'total_sales': Sum('price'),
        }
        response.context_data['summary'] = list(
            qs
            .values('id')
            .values('item')
            .annotate(**metrics)
            .order_by('-total_sales')
        )
        
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        list_filter = (
        'device',
        )
        
        
        
        
        
        return response
admin.site.register(SaleSummary,OrderSummaryAdmin)








