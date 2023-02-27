from django.forms.models import ModelForm
from .models import Webtoon

class WebtoonForm(ModelForm):

    class Meta:
        model = Webtoon
        fields ="__all__"
        