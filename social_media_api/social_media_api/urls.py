from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts (auth, profile, follow/unfollow)
    path('api/accounts/', include('accounts.urls')),

    # Posts (CRUD, feed, likes)
    path('api/posts/', include('posts.urls')),

    # Notifications
    path('api/notifications/', include('notifications.urls')),
]

# Media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
