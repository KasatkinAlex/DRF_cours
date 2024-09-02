from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import MyPagination
from habit.serializer import HabitSerializer, HabitCreateSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        """Автоматическое присвоение создатель привычки"""
        serializer.save(owner=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = MyPagination
    permission_classes = (IsOwner, IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(owner=user)


class HabitListPublishedAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated, )


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Детальная информация."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = (IsOwner, IsAuthenticated, )


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner, IsAuthenticated, )
