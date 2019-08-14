from django.urls import path, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('image/', views.my_image, name='image'),
    re_path(r'^(?!api).*', views.index, name='index'),
    re_path(r'api/process/$', views.process, name='process'),
    re_path(r'^api/ping/$', views.ping, name='ping'),
    re_path(r'^api/result/$', views.result, name='result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
