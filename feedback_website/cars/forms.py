from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your own review here',
                            widget=forms.Textarea(attrs={'class' : 'myform2', 'placeholder' : 'Write your review here.', 'rows' : '10', 'cols' : '30' }))

class ReviewForm2(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']

        labels = {
            'first_name' : "Your First Name",
            'last_name' : "Your Last Name",
            'stars' : "Rating"
        }

        error_messages = {
            'stars' : {
                'max_value' : 'Yo! The rating must be smaller than 5.',
                'min_value' : 'Yo! The rating is lesser than 5.'
            }
        }