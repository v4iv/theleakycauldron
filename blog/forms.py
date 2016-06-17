from django import forms
from django.contrib.auth.forms import AuthenticationForm
from tinymce.widgets import TinyMCE

from .models import Article, Contact, About


class SignInForm(AuthenticationForm):
    username = forms.CharField(required=True, max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(required=True, label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content', 'tags',)

    title = forms.CharField(max_length=140,
                            widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'Title'}))
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={
        'rows': 10,
        'class': 'form-control',
        'placeholder': 'Write Article...'}))
    tags = forms.CharField(required=False, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'tags seperated by comma'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)

    name = forms.CharField(required=True,
                           max_length=140,
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Name, eg: John Smith'}))
    email = forms.CharField(required=True,
                            widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'Email, eg: someone@example.com'}))

    message = forms.CharField(required=False,
                              widget=forms.Textarea({
                                  'rows': "5",
                                  'class': 'form-control',
                                  'placeholder': 'Message'}))


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['display_picture', 'name', 'content', 'resume', ]

    display_picture = forms.ImageField(required=False)
    name = forms.CharField(required=True,
                           max_length=140,
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Name'}))
    content = forms.CharField(required=False,
                              widget=forms.Textarea({
                                  'rows': "5",
                                  'class': 'form-control',
                                  'placeholder': 'Some words about yourself...'}))
    resume = forms.URLField(required=True,
                            widget=forms.URLInput({
                                'class': 'form-control',
                                'placeholder': 'eg: http://example.com'}))
