from django.forms import ModelForm
from .models import TeachingRegistration,VolenteerRegistration


class NameForm(ModelForm):
    class Meta:
        model = TeachingRegistration
        fields = "__all__"

class VolenteerForm(ModelForm):
    class Meta:
        model = VolenteerRegistration
        fields = "__all__"
