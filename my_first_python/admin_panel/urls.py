
from django.conf.urls import url
from admin_panel import views 

from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$',views.login),
    url(r'^admin_login/',views.admin_login),
    url(r'^admin_login_action/$',views.admin_login_action),
    url(r'^teacher_register/',views.rdData),
    url(r'^register_action/',views.check),
    url(r'^add_class/',views.add_class),
    url(r'^add_class_action/',views.add_class_action),
    url(r'^add_section/',views.add_section),
    url(r'^add_section_action/',views.add_section_action),
    # url(r'^lgChk/',views.login)
]
