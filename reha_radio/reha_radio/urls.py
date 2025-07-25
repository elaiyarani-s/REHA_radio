"""
URL configuration for reha_radio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from core import views as core_views
from chat.views import AdminChatView


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('', include('core.urls')),
    path('', include('chat.urls')),
    path("chat/", AdminChatView.as_view(template_name="admin_chat.html"), name="admin_chat")

]


