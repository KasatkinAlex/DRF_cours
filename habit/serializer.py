from rest_framework import serializers

from habit.models import Habit
from habit.validators import (TowFieldsValidator,
                              TimeCheckValidator,
                              HabitPleasantCheckValidator,
                              PleasantHabitValidator)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            TowFieldsValidator('connection_habit', 'reward'),
            TimeCheckValidator('duration'),
            HabitPleasantCheckValidator('connection_habit'),
            PleasantHabitValidator('habit_is_pleasant')
        ]
