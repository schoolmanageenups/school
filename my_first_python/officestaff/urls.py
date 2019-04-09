from django.conf.urls import url
from django.contrib import admin
from officestaff import views

urlpatterns = [
    
 
    url(r'^pta/',views.pta),
    url(r'^addpta/',views.addpta),
    url(r'^fees/',views.fees),
    url(r'^addfees/',views.addfees),
    url(r'^achieve/',views.achieve),
    url(r'^addachieve/',views.addachieve),
    url(r'^examnotif/',views.examnotif),
    url(r'^addexamnotif/',views.addexamnotif),
    url(r'^teacher/',views.teach),
    url(r'^teachers/',views.teachers),




   


  

]
