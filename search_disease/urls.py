# urls.py in myapp
from django.urls import path
from .views import home, search ,viewEbook,about,contact

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path("viewebooks/", viewEbook, name='view'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
