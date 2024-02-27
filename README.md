# second_test_task

Присожение - интернет магазин. Подключается к платежной системе stripe.

Запуск приложения с использованием Docker Compose
Этот репозиторий содержит Docker Compose файл для удобного запуска приложения в контейнере. Следуйте этим инструкциям, чтобы развернуть и запустить приложение.

Предварительные требования
Docker должен быть установлен на вашем компьютере.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Шаги по установке и запуску
1. Склонируйте репозиторий:

  ```bash
  git clone https://github.com/your-username/your-repository.git
  ```

2. Перейдите в директорию проекта:

  ```bash
  cd your-repository
  ```

3. Создайте файл .env.docker и укажите необходимые переменные окружения. Пример можно посмотреть в .env.example.
 

4. Запустите приложение с использованием Docker Compose:

  ```bash
  docker-compose up --build
  ```

Приложение будет доступно по адресу http://localhost:8000/ или http://127.0.0.1:8000/. Но рабочие url там другие. Их можно посмотреть в products/urls.py.

Для завершения работы приложения, выполните следующую команду:

  ```bash
  docker-compose down
  ```

Примечание
Если это первый запуск, убедитесь, что база данных инициализирована. Вы можете использовать команду docker-compose exec app python manage.py migrate для применения миграций.

Если необходимо внести изменения в код приложения, остановите контейнер (docker-compose down), внесите изменения и повторно запустите контейнер (docker-compose up).

# Приложение также можно запустить вручную, без docker-compose
1. Установка зависимостей:
Убедитесь, что у вас установлены все зависимости вашего проекта. Обычно для этого используется виртуальное окружение:
  
  ```bash
  # Создание виртуального окружения
  python -m venv venv
  
  # Активация виртуального окружения (Windows)
  .\venv\Scripts\activate
  
  # Активация виртуального окружения (Unix или MacOS)
  source venv/bin/activate
  ```

После активации виртуального окружения, установите зависимости:

  ```bash
  pip install -r requirements.txt
  ```

2. Создайте и заполните .env. Пример можно посмотреть в .env.example.


3. Применение миграций:
Примените миграции, чтобы создать необходимые таблицы в базе данных:

  ```bash
  python manage.py migrate
  ```

4. Создание суперпользователя:

  ```bash
  python manage.py migrate
  ```

5. Запуск сервера:

  ```bash
  python manage.py runserver
  ```

Приложение будет доступно по адресу http://localhost:8000/. Рабочие url там такие:

```bash
urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='detail'),  # Страница просмотра товара
    path('buy/<int:pk>/', page_with_pay_link, name='buy'),  # Страница со ссылкой на оплату
    path('success/<int:pk>/', success_page),  # Страница успешной оплаты товара
    path('basket/', orders_create, name='basket'),  # Страница сбора корзины
    path('basket/<int:pk>/', basket_pay_link, name='buy_basket'),  # Страница со ссылкой на оплату
    path('basket_success/', basket_success_page),  # Страница успешной оплаты корзины
]
```
