# bookshelf/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Book

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth"
    )
    profile_photo = forms.ImageField(
        required=False,
        label="Profile Photo"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 2025}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return author