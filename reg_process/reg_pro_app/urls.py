from django.conf.urls import url,include
from reg_pro_app import views

app_name='reg_pro_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^loginpage/$',views.loginfunc,name='login'),
    ]
