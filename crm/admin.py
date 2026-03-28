from django.contrib import admin
from .models import Candidate, Application, Payment, Invoice, Document, CourierEntry, LegalRecord, B2BClient

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name','phone','country','position','status','medical_status','visa_status','staff_name']
    search_fields = ['name','phone','passport_number','country']
    list_filter = ['status','medical_status','visa_status','candidate_type']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['candidate','country','job_category','status','application_date']
    list_filter = ['status']
    search_fields = ['candidate__name','country']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['candidate','amount','mode','purpose','date']
    list_filter = ['mode','purpose']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number','domain','candidate','amount','status','date']
    list_filter = ['status','domain']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['candidate','doc_type','is_original','is_attested','is_verified']

@admin.register(CourierEntry)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['entry_type','candidate','courier_company','tracking_number','date']

@admin.register(LegalRecord)
class LegalAdmin(admin.ModelAdmin):
    list_display = ['candidate','agreement_signed','refund_eligible','cancellation_status']

@admin.register(B2BClient)
class B2BAdmin(admin.ModelAdmin):
    list_display = ['company_name','contact_person','country','contract_status']
