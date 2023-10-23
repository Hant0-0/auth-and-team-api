# Тестове завдання

Цей проект реалізує автентифікацію через API Google та Facebook і створює REST API з кінцевими точками CRUD для "команд" і "людей в цих командах".

## Завдання

1. **Автентифікація через API Google та Facebook**

   Реалізувати автентифікацію через API Google та Facebook. 

2. **REST API для "команд" і "людей в цих командах"**

Створення REST API з кінцевими точками CRUD (створення, читання, оновлення, видалення) для "команд" і "людей в цих командах".

   - Кінцева точка `/api/teams` дозволяє керувати об'єктами "команда". Можливі операції включають створення нових команд, читання інформації про команди, оновлення даних команд та видалення команд.
   
   - Кінцева точка `/api/peoples` дозволяє керувати об'єктами "людина". Можливі операції включають створення нових людей, читання інформації про людей, оновлення даних про людей та видалення людей.

## Реалізовано обидва пункти тестового завдання

## Встановлення та Запуск

1. Клонуйте репозиторій:

   ```bash
   git clone https://github.com/Hant0-0/auth-and-team-api.git

2. Встановіть всі залежності
    
    ```bash
    pip install -r requirements.txt

3. Виконайте міграції до бази даних, виконавши команду

   ```bash
   python manage.py migrate
   
4. Запустіть сервер
   
   ```bash
   python manage.py runserver