from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name="create_user_view"),
    path('update/', views.UpdateUserView.as_view(), name="update_user_view"),
    path('delete/', views.DeleteUserView.as_view(), name="delete_user_view"),
]