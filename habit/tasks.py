from datetime import datetime, timedelta

from celery import shared_task


from habit.models import Habit
from habit.services import send_tg


@shared_task
def user_send_tg():
    """ Рассылка привычки в телеграм """

    time_now = datetime.now()
    habits1 = Habit.objects.all()

    if habits1:
        for habit in habits1:
            if (habit.time.strftime("%Y-%m-%d %H:%M") ==
                    time_now.strftime("%Y-%m-%d %H:%M")):
                if habit.owner.tg_chat_id:
                    send_tg(habit)
                    habit.time += timedelta(days=habit.number_of_executions)
                    habit.save()
