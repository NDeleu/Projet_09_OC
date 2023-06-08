from django import forms

from . import models


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

"""
    def clean(self):
        ticket = self.cleaned_data.get('ticket')
        user = self.cleaned_data.get('user')
        print(ticket)
        print(user)

        if ticket and user:
            review_compared = models.Review.objects.filter(
                Q(ticket__id=str(ticket.id)) & Q(user__id=str(user.id)))
            print(review_compared)
            if review_compared:
                raise forms.ValidationError("Il n'est possible d'éditer qu'une seule critique par utilisateur sur un même ticket. Vous avez déjà une critique éditée sur ce ticket.")
        
        return self.cleaned_data
"""