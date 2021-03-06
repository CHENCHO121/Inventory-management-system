from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('display_desktop', views.display_desktop, name='display_deskop'),
    path('display_laptop', views.display_laptop, name='display_laptop'),
    path('display_mobile', views.display_mobile, name='display_mobile'),
    path('add_laptop', views.add_laptop, name='add_laptop'),
    path('add_desktop', views.add_desktop, name='add_desktop'),
    path('add_mobile', views.add_mobile, name='add_mobile'),

    path('edit_laptop/<int:pk>',views.edit_laptop,name="edit_laptop"),
    path('edit_mobile/<int:pk>', views.edit_mobile, name="edit_mobile"),
    path('edit_desktop/<int:pk>', views.edit_desktop, name="edit_desktop"),

    path('delete_laptop/<int:pk>', views.delete_laptop, name="delete_laptop"),
    path('delete_desktop/<int:pk>', views.delete_desktop, name="delete_desktop"),
    path('delete_mobile/<int:pk>', views.delete_mobile, name="delete_mobile"),

]



