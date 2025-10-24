from myshop.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home/', views.homepage, name="homepage"),
    path('contactus/', views.contactpage, name="contactpage"),
    path('UserList/', views.listpage, name="userlistpage")
]