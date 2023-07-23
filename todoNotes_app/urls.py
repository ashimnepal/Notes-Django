from django.urls import path
from todoNotes_app import views


urlpatterns = [
    path("",views.todo_list),
    path("add-todo/",views.add_todo),
    path("delete-todo/<int:pk>/",views.delete_todo),
    path("edit-todo/<int:pk>/",views.item_update),
    
]
