from . import views 
from django.urls import path,include
from django.conf.urls import url

app_name='groups'

url_patterns=[
    path("",views.ListGroups.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single')
]