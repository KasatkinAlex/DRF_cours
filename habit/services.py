import requests

from rest_framework import status

from config import settings


def send_tg(habit):
    """Отправляет сообщение через телеграм с напоинанием о привычке"""
    time_habit = habit.time.strftime("%H:%M")
    message = (f"{habit.action} запланировано на сегодня "
               f"на {time_habit}")
    chat_id = habit.owner.tg_chat_id
    params = {"text": message, "chat_id": chat_id}

    response = requests.get(
        f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
        data=params
    )
    if response.status_code != status.HTTP_200_OK:
        print(f"Ошибка при отправке сообщения в Telegram: {response.text}")
