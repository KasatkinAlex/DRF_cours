from datetime import timedelta

from django.db import models

from users.models import User


class Habit(models.Model):
    # НЕ ЗАБЫТЬ УБРАТЬ null blank

    EXECUTIONS_WEEK = [
        (1, "раз в неделю"),
        (2, "два раза в неделю"),
        (3, "три раза в неделю"),
        (4, "четыре раза в неделю"),
        (5, "пять раз в неделю"),
        (6, "шесть раз в неделю"),
        (7, "каждый день")
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name="Создатель", related_name="user_habit")
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name="Место выполнения")
    time = models.TimeField(blank=True, null=True, verbose_name="Время выполнения")
    action = models.CharField(max_length=100, verbose_name="Действие", blank=True, null=True,)
    habit_is_pleasant = models.BooleanField(default=True, verbose_name="Признак приятной привычки")
    connection_habit = models.ForeignKey("self", on_delete=models.CASCADE,
                                         blank=True, null=True,
                                         verbose_name="Связанная привычка", related_name="habit_connect")
    number_of_executions = models.IntegerField(default=1, choices=EXECUTIONS_WEEK,
                                               verbose_name="Количество выполнений в неделю")
    duration = models.DurationField(default=timedelta(seconds=120),
                                    verbose_name="Продолжительность выполнения (в сукундах)")
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")
    reward = models.CharField(
        max_length=100, verbose_name="Вознаграждение", blank=True, null=True
    )

    def __str__(self):
        return f"Действие: {self.action} (создатель {self.owner})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["owner"]
