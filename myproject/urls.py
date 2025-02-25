"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomPasswordChangeView, SignUpView
from myapp.views import home, about, contact, chart, new_music, news, album_detail, UserMessageCreateView, \
    add_review_view, ReviewUpdateView, ReviewDeleteView, see_all_reviews_view, NewsDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('chart/', chart, name='chart'),
    path('new-music/', new_music, name="new-music"),
    path('news/', news, name='news'),
    path('album/<album_id>', album_detail, name='album-detail'),
    path('usermessage/', UserMessageCreateView.as_view(), name='user-message'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password', CustomPasswordChangeView.as_view(), name='change-password'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add-review/<album_id>', add_review_view, name='add-review'),
    path('edit-review/<pk>', ReviewUpdateView.as_view(), name='edit-review'),
    path('delete-review/<pk>', ReviewDeleteView.as_view(), name='delete-review'),
    path('reviews/<post_id>', see_all_reviews_view, name='reviews'),
    path('news-details/<pk>', NewsDetails.as_view(), name="news-details")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)