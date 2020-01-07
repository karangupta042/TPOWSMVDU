from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<int:post_id>',views.detail,name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)