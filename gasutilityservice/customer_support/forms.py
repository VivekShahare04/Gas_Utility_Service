from django import forms
from .models import SupportTicket
from django.contrib.auth import get_user_model

User = get_user_model()

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['assigned_to', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_support_rep=True)