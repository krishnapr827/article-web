from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('article/<int:id>',views.article, name='article'),
    path('about',views.about, name='about'),
    path('contactus',views.contact, name='contact'),
]


#path converter-->  <datatype:var>