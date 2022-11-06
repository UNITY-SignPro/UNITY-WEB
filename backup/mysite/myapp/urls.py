# from xml.etree.ElementInclude import include
# from django.urls import path

# from . import views
# from myapp.views import SearchFormView

# app_name = 'myapp'

# urlpatterns = [
#     path('',SearchFormView.as_view(),name='search'),
# ]

from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from rest_framework import routers
from myapp.views import TranslateViewSet

app_name = 'myapp'

router = routers.DefaultRouter()
router.register('myapp',TranslateViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(router.urls)),
]


