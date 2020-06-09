"""impproj URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from myapp import views

router=routers.DefaultRouter()
router.register(r'registerapi',views.RegisterViewset)
router.register(r'Signapi',views.SignViewset)
router.register(r'Sessionapi',views.SessionViewset)
router.register(r'Studentapi',views.StudentViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.url')),
    path('lock',include(router.urls)),
    
    # 1) The url to be searched in the URL bar on the local server
    # 2) The file that you want to run when the request is matched
]
