from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Candidates
    path('candidates/', views.candidates, name='candidates'),
    path('candidates/add/', views.candidate_add, name='candidate_add'),
    path('candidates/<int:pk>/view/', views.candidate_view, name='candidate_view'),
    path('candidates/<int:pk>/edit/', views.candidate_edit, name='candidate_edit'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),

    # Applications
    path('applications/', views.applications, name='applications'),
    path('applications/add/', views.application_add, name='application_add'),
    path('applications/<int:pk>/delete/', views.application_delete, name='application_delete'),

    # Documents
    path('documents/', views.documents, name='documents'),
    path('documents/add/', views.document_add, name='document_add'),
    path('documents/<int:pk>/delete/', views.document_delete, name='document_delete'),

    # Courier
    path('courier/', views.courier, name='courier'),
    path('courier/add/', views.courier_add, name='courier_add'),
    path('courier/<int:pk>/delete/', views.courier_delete, name='courier_delete'),

    # Payments
    path('payments/', views.payments, name='payments'),
    path('payments/add/', views.payment_add, name='payment_add'),
    path('payments/<int:pk>/delete/', views.payment_delete, name='payment_delete'),

    # Invoices
    path('invoices/', views.invoices, name='invoices'),
    path('invoices/add/', views.invoice_add, name='invoice_add'),
    path('invoices/<int:pk>/paid/', views.invoice_mark_paid, name='invoice_mark_paid'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),

    # Legal
    path('legal/', views.legal, name='legal'),
    path('legal/add/', views.legal_add, name='legal_add'),
    path('legal/<int:pk>/delete/', views.legal_delete, name='legal_delete'),

    # B2B
    path('b2b/', views.b2b, name='b2b'),
    path('b2b/add/', views.b2b_add, name='b2b_add'),
    path('b2b/<int:pk>/delete/', views.b2b_delete, name='b2b_delete'),

    # Excel
    path('export/', views.export_excel, name='export_excel'),
    path('import/', views.import_excel, name='import_excel'),
]
