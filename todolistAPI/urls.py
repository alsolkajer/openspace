"""todolistAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views


from django.conf.urls.static import static
from django.conf import settings

from todo.views import ToDoViewSet, APIIncrement, APIDecrement, APIDefault

urlpatterns = [
    path('', views.Landing_Page.as_view(), name='landing_page'),
    path('inc',APIIncrement, name='apiincrement'),
    path('dec',APIDecrement, name='apidecrement'),
    path('def',APIDefault, name='apidefault'),
    path('main', views.Main_Page.as_view(), name='main_page'),
    path('admin/', admin.site.urls),
    path('api/<slug:user>/todo/', ToDoViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('api/<slug:user>/todo/<int:pk>/', ToDoViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
