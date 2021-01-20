from .  import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('fuctions/',views.plot),
    path('Deletefuction/<int:delete_id>/',views.delete),
    path('clear/',views.clear),
    path('rules/',views.rules),
    

]