"""NASA URL Configuration

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
from instanasa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasa/date_selecter/', views.date_selecter.as_view()),
    path('nasa/make_comment/', views.instanasaCreateView.as_view(), name = 'make_comment'),
    path('nasa/list_comments', views.instanasaListView.as_view(), name = "list_comments"),
    path('nasa/comment_details/<int:pk>', views.instanasaDetailView.as_view(), name = 'comment_details'),
    path('nasa/delete_comment/<int:pk>', views.instanasaDeleteView.as_view(), name = 'delete_comment'),
    path('nasa/update_comment/<int:pk>', views.instanasaUpdateView.as_view(), name = 'update_comment')
]
