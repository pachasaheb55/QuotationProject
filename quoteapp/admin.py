""" admin file for quote app"""
from django.contrib import admin
from quoteapp.models import Customer, Vehicle, CoverageInfo, Quotation
from quoteapp.tasks import pdf_generator_task


class QuotationAdmin(admin.ModelAdmin):
    """ Admin model for Quotaion"""

    # admin action with description
    @admin.action(description='Send Email to Customer')
    def send_email_to_customer(modeladmin, request, queryset):
        """ admin action for sending email """
        for quote in queryset:
            # call celery task
            pdf_generator_task.delay(quote.id)

    actions = [send_email_to_customer, ]  # <-- Add the list action function here

# register the models
models = [Customer, Vehicle, CoverageInfo]
admin.site.register(models)
# regitstr for admin action
admin.site.register(Quotation, QuotationAdmin)
