from django.contrib import admin
from .models import POS
admin.site.site_header = 'Waaneiza POS system'
class POSAdmin(admin.ModelAdmin):
	list_display = ['customer_name','customer_phone', 'items', 'price', 'showroom','date']
	list_filter = ['customer_name','customer_phone', 'price', 'showroom','date']
	search_fields = ['customer_name','customer_phone', 'items', 'price', 'showroom','date']
admin.site.register(POS, POSAdmin)
