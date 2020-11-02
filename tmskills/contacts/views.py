from django.shortcuts import render
from django.shortcuts import redirect

def contacts_page(request):
    if request.method == "POST":
        print(request.POST)
        redirect("/contacts/")
    return render(request, template_name="contacts.html", context={})