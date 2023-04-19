from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(  
        label="Commentaire :",
        max_length=500,
        widget=forms.TextInput(attrs={"placeholder": "..."}),
    )
