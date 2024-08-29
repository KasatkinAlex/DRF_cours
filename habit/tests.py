from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="test1@mail.ru",
                                        tg_chat_id="598849306")
        self.habit = Habit.objects.create(number_of_executions=4,
                                          is_published=True,
                                          habit_is_pleasant=False,
                                          duration="00:01:00",
                                          time="2024-08-29 12:00",
                                          owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habit:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('is_published'), self.habit.is_published
        )

    def test_habit_create(self):
        url = reverse("habit:habit_create")
        data = {
            "time": '2024-08-29 21:19',
            "habit_is_pleasant": False,
            "number_of_executions": 7,
            "duration": "00:01:00",
            "reward": "выспаться",
            'is_published': True
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        url = reverse("habit:habit_update", args=(self.habit.pk,))
        data = {
            'is_published': True
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('is_published'), True
        )

    def test_lesson_delete(self):
        url = reverse("habit:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("habit:habit_list_user")
        response = self.client.get(url)
        data = {'count': 1, 'next': None, 'previous': None,
                'results': [{'id': 6, 'place': None,
                             'time': '2024-08-29T12:00:00Z',
                             'action': None, 'habit_is_pleasant': False,
                             'number_of_executions': 4,
                             'duration': '00:01:00',
                             'is_published': True,
                             'reward': None, 'owner': 5,
                             'connection_habit': None}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(response.json(), data)
