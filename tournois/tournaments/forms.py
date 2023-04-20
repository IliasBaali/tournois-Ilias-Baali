from django.forms import ModelForm
from .models import Commentaire

class CommentForm(ModelForm):
    class Meta:
        model = Commentaire
        exclude = ['author', 'match', 'date_time']
        labels = {'content':"Commentez"}