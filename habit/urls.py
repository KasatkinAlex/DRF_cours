from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitListAPIView,
                         HabitRetrieveAPIView,
                         HabitCreateAPIView,
                         HabitUpdateAPIView,
                         HabitDestroyAPIView,
                         HabitListPublishedAPIView)

app_name = HabitConfig.name

urlpatterns = [
    path('list_user/', HabitListAPIView.as_view(), name='habit_list_user'),
    path('', HabitListPublishedAPIView.as_view(), name='habit_list_published'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(),
         name='habit_update'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(),
         name='habit_delete'),
]
