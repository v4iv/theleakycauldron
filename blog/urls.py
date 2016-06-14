from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.utils import timezone

from blog.forms import SignInForm
from . import views

urlpatterns = [
                  url(r'^signin/$',
                      'django.contrib.auth.views.login',
                      {
                          'template_name': 'blog/signin.html',
                          'authentication_form': SignInForm,
                          'extra_context':
                              {
                                  'title': 'Sign In',
                                  'year': timezone.now().year,
                              }
                      },
                      name='signin'),

                  url(r'^signout$',
                      'django.contrib.auth.views.logout',
                      {
                          'next_page': '/',
                      },
                      name='signout'),
                  url(r'^$', views.home, name='home'),
                  url(r'^article/(?P<pk>[0-9]+)/$', views.full_article, name='article'),
                  url(r'^article/new/$', views.new_article, name='new_article'),
                  url(r'^article/(?P<pk>[0-9]+)/edit/$', views.edit_article, name='edit_article'),
                  url(r'^article/(?P<pk>[0-9]+)/delete/$', views.delete_article, name='delete_article'),
                  url(r'^about/$', views.about_me, name='about_me'),
                  url(r'^about/(?P<pk>[0-9]+)/update/$', views.update_profile, name='update_profile'),
                  url(r'^contact/messages/$', views.messages, name='messages'),
                  url(r'^contact/$', views.contact_me, name='contact_me'),
                  url(r'^contact/(?P<pk>[0-9]+)/delete/$', views.delete_contact, name='delete_contact'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
