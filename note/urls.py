from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('<int:note_id>/', views.note, name='note'),
    path('add/', views.add_note, name='add_note'),
    path('<int:note_id>/memo/add', views.add_memo, name='add_memo'),
    path('<int:note_id>/<int:memo_id>/deactivate', views.deactivate_memo, name='deactivate_memo')
]