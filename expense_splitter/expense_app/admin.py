from django.contrib import admin
from .models import Group,Expense,Settlement,Split,ExpensePayment

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['g_name']
    # fields = ['g_name']
admin.site.register(Group)

class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ['e_name']
    fields = ['e_name','total_amount', 'split_type','create_at','paid_by']

admin.site.register(Expense)
admin.site.register(Split)
admin.site.register(Settlement)

admin.site.register(ExpensePayment)