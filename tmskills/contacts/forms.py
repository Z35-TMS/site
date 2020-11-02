from django import forms
from contacts.models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            "fullname",
            "email",
            "phone",
            "message",
        ]

    