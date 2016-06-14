from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Article, Contact, About


class SignInForm(AuthenticationForm):
    username = forms.CharField(required=True, max_length=254,
                               widget=forms.TextInput({
                                   'placeholder': 'Username'}))
    password = forms.CharField(required=True, label=("Password"),
                               widget=forms.PasswordInput({
                                   'placeholder': 'Password'}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content', 'tags',)

    title = forms.CharField(max_length=140,
                            widget=forms.TextInput({
                                'placeholder': 'Title'}))
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea({
        'placeholder': 'Write Article...'}))
    tags = forms.CharField(required=False, widget=forms.TextInput({
        'placeholder': 'tags seperated by comma'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)

    name = forms.CharField(required=True,
                           max_length=140,
                           widget=forms.TextInput({
                               'placeholder': 'Name, eg: John Smith'}))
    email = forms.CharField(required=True,
                            widget=forms.TextInput({
                                'placeholder': 'Email, eg: someone@example.com'}))
    message = forms.CharField(widget=forms.Textarea({
        'placeholder': 'Message'}))


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['display_picture', 'dob', 'interests', 'profession', 'expertise', 'resume',]

    display_picture = forms.ImageField(required=False)
    dob = forms.DateField(required=False,
                          widget=forms.DateInput({
                              'placeholder': 'date of birth'}))
    interests = forms.CharField(required=True, widget=forms.Textarea({
        'placeholder': 'your interests seperated by comma'}))
    profession = forms.CharField(required=True,
                                 max_length=140,
                                 widget=forms.TextInput({
                                     'placeholder': 'your profession'}))
    expertise = forms.CharField(required=True, widget=forms.Textarea({
        'placeholder': 'your fields of expertise seperated by comma'}))
    resume = forms.URLField(required=True,
                            widget=forms.URLInput({
                                'placeholder': 'eg: http://example.com'}))
