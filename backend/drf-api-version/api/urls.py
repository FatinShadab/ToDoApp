from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateTodoEP.as_view()),
    path('all/', views.GetAllTodoEP.as_view()),
    #path('get/', views.GetOneTodoEP.as_view()),
    #path('update/', views.UpdateTodoEP.as_view()),
    path('delete/', views.DeleteTodoEP.as_view())
]