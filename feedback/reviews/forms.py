from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
#     email = forms.EmailField(label="Your Email", max_length=100, error_messages={
#         "required": "Your email must not be empty",
#         "max_length": "Please enter a shorter email"
#     })

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
            'email': 'Your Email'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty',
                'max_length': 'Please enter a shorter name'
            },
            'email': {
                'required': 'Your email must not be empty',
                'max_length': 'Please enter a shorter email'
            }
        }