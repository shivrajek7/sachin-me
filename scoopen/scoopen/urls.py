from django.contrib import admin
from django.urls import path,include
from pythonbatch import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('python/',include("pythonbatch.urls")),
    path('show/', views.show),
    path('edit/<int:econtact>', views.edit),
    path('update/<int:econtact>',views.update),
    path('delete/<int:econtact>',views.destroy),
    path('stud/', views.applandingpage),

]

