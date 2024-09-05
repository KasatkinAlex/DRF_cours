ПРОЕКТ ТРЕКЕР ПОЛЕЗНЫХ ПРИВЫЧЕК С ИСПОЛЬЗОВАНИЕМ DRF.

Описание Трекер полезных привычек. Создайте привычку и Вы будете получать уведомление о ней в телеграм

Технологии

Python
Django
DRF
PostgreSQL
Redis
Celery
Docker
Для работы с проектом необходимо.

Клонировать репозиторий на компьютер используя SSH ключ.
На компьютере должен быть установлен Docker и docker-compose (инструкции по установке на сайте https://www.docker.com/)
Создайте контейнер командой docker-compose build
и последующий запуск контейнера командой docker-compose up -d

В файл .env внесите свои данные (необходимые переменные перечислены в файле .env.sample)


создайте телеграмма бота (Чтобы зарегисрировать бота находим в поисковике BotFather)
Зарегисрируйте usera не забыв предать id телеграмма (как получить чтобы получить ид находим в поиске теленрам бота Get ID)
Добавляем привычки и ожидаем сообщение от бота

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/docs/