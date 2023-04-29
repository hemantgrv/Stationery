from django.contrib import admin
from .models import *
# from django.urls import reverse
# from django.utils.safestring import mark_safe

"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    admin.site.register(Catagory,CategoryAdmin)
"""
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)

# class MyModelAdmin(admin.ModelAdmin):
#     actions = ['generate_report_action']

#     def generate_report_action(self, request, queryset):
#         url = reverse('admin:generate_report')
#         return mark_safe(f'<form method="POST" action="{url}">'
#                          f'<button type="submit">Generate Report</button>'
#                          f'</form>')

#     generate_report_action.short_description = "Generate Report"
