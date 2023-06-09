from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    description = forms.CharField(label='description', widget=forms.Textarea)

    class Meta:
        model = models.Ticket
        fields = ['title', 'author', 'description', 'image']


class ReviewForm(forms.ModelForm):
    ratings = [
        ('0', "Très Mauvais"),
        ('1', "Mauvais"),
        ('2', "Passable"),
        ('3', "Bon"),
        ('4', "Très bon"),
        ('5', "Excellent")
    ]
    rating = forms.ChoiceField(
        label='notation', choices=ratings, widget=forms.RadioSelect)
    body = forms.CharField(label='commentaire', widget=forms.Textarea)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class FollowUsersForm(forms.ModelForm):
    follows = forms.CharField(label="Nom d'utilisateur", max_length=128)

    class Meta:
        model = User
        fields = ['follows']

    def clean_follows(self):
        follows = self.cleaned_data['follows']
        
        if not User.objects.filter(username=follows):
            raise forms.ValidationError("Cet utilisateur n'est pas reconnu dans la base de donnée.")

        return follows
