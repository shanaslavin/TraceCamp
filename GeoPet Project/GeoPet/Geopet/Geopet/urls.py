"""Geopet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from findpet import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geopet/create_post', views.descriptionCreateView.as_view(), name = 'creat_post'),
    path('geopet/post_created/<int:pk>', views.descriptionDetailView.as_view(), name = 'post_created'),
    path('geopet/list_inputs', views.descriptionListView.as_view(), name = 'list_view'),
    path('geopet/update/<int:pk>', views.descriptionUpdateView.as_view(), name = 'update'),
    path('geopet/delete/<int:pk>', views.descriptionDeleteView.as_view(), name = 'delete'),
    path('geopet/map', views.map.as_view()),
    path('geopet/api/<int:map_id>', views.animal_list_api),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
