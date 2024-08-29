from datetime import timedelta

from django.db import models

from users.models import User


class Habit(models.Model):

    EXECUTIONS_WEEK = [
        (1, "один день"),
        (2, "два дня"),
        (3, "три дня"),
        (4, "четыре дня"),
        (5, "пять дней"),
        (6, "шесть дней"),
        (7, "семь дней")
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              blank=True, null=True,
                              verbose_name="Создатель",
                              related_name="user_habit")
    place = models.CharField(max_length=100,
                             blank=True, null=True,
                             verbose_name="Место выполнения")
    time = models.DateTimeField(verbose_name="Время выполнения "
                                             "начала выполнения "
                                             "'YYYY-MM-DD HH:MM'")
    action = models.CharField(max_length=100,
                              verbose_name="Действие",
                              blank=True, null=True,)
    habit_is_pleasant = models.BooleanField(verbose_name="Признак "
                                                         "приятной привычки")
    connection_habit = models.ForeignKey("self", on_delete=models.CASCADE,
                                         blank=True, null=True,
                                         verbose_name="Связанная привычка",
                                         related_name="habit_connect")
    number_of_executions = models.IntegerField(default=1,
                                               choices=EXECUTIONS_WEEK,
                                               verbose_name="Следующее "
                                                            "выполнение "
                                                            "через __ дней")
    duration = models.DurationField(default=timedelta(seconds=120),
                                    verbose_name="Продолжительность "
                                                 "выполнения (в сукундах)")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Признак публичности")
    reward = models.CharField(max_length=100,
                              verbose_name="Вознаграждение",
                              blank=True, null=True)

    def __str__(self):
        return f"Действие: {self.action} (создатель {self.owner})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["time"]
