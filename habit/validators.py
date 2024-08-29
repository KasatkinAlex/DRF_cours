from datetime import timedelta

from rest_framework import serializers


class TowFieldsValidator:
    """ Проверка на установку двух полей в раз:
    habit_is_pleasant,  connection_habit"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        val2 = dict(value).get(self.field2)
        if val1 and val2:
            raise serializers.ValidationError("Может быть указано "
                                              "тольо одно из полей:"
                                              " 'Указания вознаграждения'"
                                              " 'Связанная привычка'")


class TimeCheckValidator:
    """ Время выполнения должно быть не больше 120 секунд. """

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        if val1 is None:
            val1 = timedelta(seconds=120)
        if val1 > timedelta(seconds=120):
            raise serializers.ValidationError("Время на выполнение "
                                              "не может привышать "
                                              "120сек ")


class HabitPleasantCheckValidator:
    """ В связанные привычки могут попадать только привычки
    с признаком приятной привычки. """

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        val1 = dict(value).get(self.field1)
        if val1:
            if not val1.habit_is_pleasant:
                raise serializers.ValidationError(
                    "В связанные привычки "
                    "могут попадать только привычки"
                    " с признаком приятной привычки")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            our_value = dict(value)
            if (our_value.get("reward") is not None
                    or our_value.get("connection_habit") is not None):
                raise ValidationError("У приятной привычки не может"
                                      " быть вознаграждения или "
                                      "связанной привычки")
