
from django.conf.urls import url
from teacher import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    url(r'^$',views.login_teacher),
    url(r'^login_action/',views.login_check),
    url(r'^edit_teacher/',views.edit_teacher),
    url(r'^add_student/',views.add_student),
    url(r'^register_student/',views.register_student),
    url(r'^profile_edit/$',views.profile_edit),
    url(r'^view_students/$',views.view_students),
    # url(r'^lgChk/',views.login)
]
