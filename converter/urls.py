from django.urls import path
from .views import convert_pdf_to_doc, convert_doc_to_pdf

urlpatterns = [
    path('pdf-to-doc/', convert_pdf_to_doc, name='convert_pdf_to_doc'),
    path('doc-to-pdf/', convert_doc_to_pdf, name='convert_doc_to_pdf'),
]
