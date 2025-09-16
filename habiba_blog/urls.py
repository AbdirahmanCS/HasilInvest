from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Homepage and main pages
    path('blog/', include('blog.urls')),  # Blog functionality
    path('users/', include('users.urls')),  # Authentication (includes logout)
    path('newsletter/', include('newsletter.urls')),  # Newsletter
    path('analytics/', include('analytics.urls')),  # Analytics (optional)
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor uploads
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)