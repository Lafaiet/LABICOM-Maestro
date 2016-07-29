"""labicommaestro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from room_scheduling.views import main_page_view, request_reservation_view, profile_view, contact_view, calendar_view
from room_scheduling.forms import LoginForm

urlpatterns = [
    url(r'^$', main_page_view, name='main_page'),
    url(r'^reservar$', request_reservation_view, name='reservation_page'),
    url(r'^contato$', contact_view, name='contact'),
    url(r'^calendario$', calendar_view, name='calendar'),

    url(r'^admin/', admin.site.urls),

    url(r'^accounts/profile/$', profile_view),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/accounts/login/'}),
]
