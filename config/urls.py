from django.contrib import admin
from django.urls import path,include

urlpatterns =[
    path('admin/',admin.site.urls),
    path('unity_web/',include('unity_web.urls')),
]