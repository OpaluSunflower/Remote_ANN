from django . urls import path
from . import views
from django . contrib . auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('test/',views.test,name='test'),
    path('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name ='logout'),
    path('signIn/',views.signIn,name='signIn'),
    path('home/',views.home,name='home')
]
