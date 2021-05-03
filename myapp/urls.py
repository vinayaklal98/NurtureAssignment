from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('users/register',views.register,name='register'),
    path('users/login',views.login,name='login'),
    path('users/<int:user_id>/advisor',views.get_advisor,name='get_advisor'),
    path('users/<int:user_id>/advisor/<int:advisor_id>',views.book_call,name='book_call'),
    path('users/<int:user_id>/advisor/booking',views.get_bookings,name='get_bookings'),
    path('admin/advisor',views.add_advisor,name='add_advisor'),
]