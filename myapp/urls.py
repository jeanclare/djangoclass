from django.urls import path
from myapp import  views

#from DjangoWebClass_Project.urls import urlpatterns

urlpatterns = [
    path ('',views.home),
    path ('about/',views.about)


]