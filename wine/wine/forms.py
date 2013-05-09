from django import forms
from registration.forms import RegistrationFormUniqueEmail

class NewUserRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(label=u"First Name", required=True)
    last_name = forms.CharField(label=u"Last Name", required=True)
    avatar = forms.URLField(label=u"Avatar", required=False)
