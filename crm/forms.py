from django import forms
from .models import Candidate, Application, Payment, Invoice, Document, CourierEntry, LegalRecord, B2BClient
import datetime


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'name','phone','passport_number','country','position','experience',
            'status','medical_status','visa_status','ticket_status','payment',
            'resume_status','resume_file','passport_copy_status','passport_copy_file',
            'offer_letter_status','offer_letter_file',
            'travel_date','reference','remarks','followup_date','staff_name',
            'registration_date','candidate_type',
        ]
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
            'followup_date': forms.DateInput(attrs={'type': 'date'}),
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['registration_date'].initial = datetime.date.today()
        for field in self.fields.values():
            field.required = False
        self.fields['name'].required = True
        self.fields['phone'].required = True


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['candidate','country','job_category','status','application_date','boarding_date','package_amount','amount_paid','remarks']
        widgets = {
            'application_date': forms.DateInput(attrs={'type':'date'}),
            'boarding_date': forms.DateInput(attrs={'type':'date'}),
            'remarks': forms.Textarea(attrs={'rows':2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['application_date'].initial = datetime.date.today()
        for field in self.fields.values():
            field.required = False
        self.fields['candidate'].required = True


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['candidate','amount','mode','purpose','date','reference','notes']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'notes': forms.Textarea(attrs={'rows':2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.date.today()
        for field in self.fields.values():
            field.required = False
        self.fields['candidate'].required = True
        self.fields['amount'].required = True
        self.fields['date'].required = True


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number','domain','candidate','amount','date','status','description']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'description': forms.Textarea(attrs={'rows':2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.date.today()
        for field in self.fields.values():
            field.required = False
        self.fields['invoice_number'].required = True
        self.fields['amount'].required = True


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['candidate','doc_type','is_original','is_attested','is_verified','with_company','notes']
        widgets = {'notes': forms.Textarea(attrs={'rows':2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.fields['candidate'].required = True


class CourierForm(forms.ModelForm):
    class Meta:
        model = CourierEntry
        fields = ['entry_type','candidate','from_person','to_person','courier_company','tracking_number','date','cost','contents','handled_by']
        widgets = {'date': forms.DateInput(attrs={'type':'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.date.today()
        for field in self.fields.values():
            field.required = False
        self.fields['date'].required = True


class LegalForm(forms.ModelForm):
    class Meta:
        model = LegalRecord
        fields = ['candidate','agreement_signed','sop_shared','terms_accepted','refund_eligible','refund_amount','refund_date','cancellation_status','notes']
        widgets = {
            'refund_date': forms.DateInput(attrs={'type':'date'}),
            'notes': forms.Textarea(attrs={'rows':2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.fields['candidate'].required = True


class B2BForm(forms.ModelForm):
    class Meta:
        model = B2BClient
        fields = ['company_name','contact_person','phone','email','country','contract_status','notes']
        widgets = {'notes': forms.Textarea(attrs={'rows':2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.fields['company_name'].required = True
