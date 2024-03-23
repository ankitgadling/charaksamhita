# urls.py in myapp
from django.urls import path
from .views import home, search ,viewEbook

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path("viewebooks/", viewEbook, name='view')
]
