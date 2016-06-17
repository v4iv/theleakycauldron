import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ArticleForm, ContactForm, AboutForm
from .models import Article, Contact, About


# Create your views here.
def home(request):
    article_list = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    recent_posts = Article.objects.order_by('-published_date')[:5]
    paginator = Paginator(article_list, 9)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page('1')
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'title': 'Home', 'year': timezone.now().year, 'articles': articles, 'recents': recent_posts,
               'archives': article_list}
    return render(request, 'blog/index.html', context)


def full_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article.html',
                  {'title': article.title, 'article': article, 'year': timezone.now().year})


@login_required(login_url='signin')
def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return HttpResponseRedirect(reverse('article', args=(article.pk,)))
    else:
        form = ArticleForm()
    return render(request, 'blog/edit_article.html',
                  {'title': 'New Article', 'form': form, 'year': timezone.now().year})


@login_required(login_url='signin')
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.last_edited = timezone.now()
            article.save()
            return HttpResponseRedirect(reverse('article', args=(article.pk,)))
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html',
                  {'title': 'Edit Article', 'form': form, 'year': timezone.now().year})


@login_required(login_url='signin')
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('/')


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.contact_date = timezone.now()
            contact.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('contact_me'))
    else:
        form = ContactForm()
        return render(request, 'blog/contact.html',
                      {'title': 'Get In Touch', 'year': timezone.now().year, 'form': form})


@login_required(login_url='signin')
def messages(request):
    contact_list = Contact.objects.filter(contact_date__lte=timezone.now()).order_by('-contact_date')
    paginator = Paginator(contact_list, 9)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page('1')
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/messages.html',
                  {'title': 'Messages', 'year': timezone.now().year, 'contacts': contacts})


@login_required(login_url='signin')
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('/')


def about_me(request):
    about = About.objects.get()
    return render(request, 'blog/about.html', {'title': 'About Me', 'year': timezone.now().year, 'about': about})


@login_required(login_url='signin')
def update_profile(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.last_edited = timezone.now()
            about.save()
            return HttpResponseRedirect(reverse('about', args=(about.pk,)))
    else:
        form = AboutForm(instance=about)
    return render(request, 'blog/update_profile.html',
                  {'title': 'Update Profile', 'form': form, 'year': timezone.now().year})
