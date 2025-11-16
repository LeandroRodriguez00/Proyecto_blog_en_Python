from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path('', views.inbox, name='inbox'),                      
    path('sent/', views.sent, name='sent'),                   
    path('new/', views.new_message, name='new_message'),      
    path('<int:pk>/', views.message_detail, name='detail'),   
    path('<int:pk>/reply/', views.reply_message, name='reply'),  
    path('<int:pk>/delete/', views.delete_message, name='delete'),

]
