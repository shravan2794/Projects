from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
from myapp


router=routers.DefaultRouter()
router.register(r'registerapi',views.RegisterViewset)
router.register(r'Signapi',views.SignViewset)
router.register(r'Sessionapi',views.SessionViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='myapp-home'),
    path('blog/',views.blog,name='myapp-blog'),
    path('register/',views.form_view,name='myapp-register'),
    path('success/',views.success,name='success'),
    path('show/',views.show,name='show'),
    path('api/',views.LoginList.as_view()),
    path('student',views.student_view,name='myapp-student'),
    path('studentapi',views.Studentlist.as_view()),
    path('random',views.RandomView.as_view())

]