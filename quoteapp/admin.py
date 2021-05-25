from django.contrib import admin
from .models import *
from quoteapp.tasks import pdf_generator_task

# Register your models here.


class QuotationAdmin(admin.ModelAdmin):
    """ Admin model for Quotaion"""

    # admin action with description
    @admin.action(description='Send Email to Customer')
    def send_email_to_customer(modeladmin, request, queryset):
        for quote in queryset:
            pdf_generator_task.delay(quote.id)
            
    actions = [send_email_to_customer, ]  # <-- Add the list action function here

# register the models
models = [Customer, Vehicle, CoverageInfo]
admin.site.register(models)
admin.site.register(Quotation, QuotationAdmin)
