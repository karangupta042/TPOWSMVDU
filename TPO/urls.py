from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header="Welcome To TPOWSMVDU"
admin.site.index_title="TPOWSMVDU Administration"
admin.site.site_title="TPOWSMVDU Admin"