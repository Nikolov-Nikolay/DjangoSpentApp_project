from django.urls import re_path
from SpentApp import views

urlpatterns = [
    re_path(r'^product$',views.productapi),
    re_path(r'^product/([0-9]+)$',views.productapi),
]