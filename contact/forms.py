from django import forms


class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Wedding Package', 'Wedding Package'),
    ]

    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
    email = forms.EmailField(label='Your Email')
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
