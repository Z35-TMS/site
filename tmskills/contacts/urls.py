from django.urls import path
from contacts.views import contacts_page

urlpatterns = [
    path("", contacts_page, name="contacts_page")
]