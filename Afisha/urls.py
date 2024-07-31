from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page_view, name='movie_list'),
    path('movie/<int:id>/', views.movie_detail_view, name='movie_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

