# Selenoid

Слушает на порту 4444 (http://127.0.0.1:4444/wd/hub), конфиг лежит в ~/.aerokube/selenoid/browsers.json

Разворачивается в контейнере

```cm selenoid configure/start/stop/status```

https://aerokube.com/selenoid/latest/ - документация

selenoid-ui слушает по порту 8080

*Как запускать selenoid, чтобы он увидел контейнер с приложением (передать капабилити):*

Sometimes you may need to link browser container to application container running on the same host machine. 
This allows you to use cool URLs like http://my-cool-app/ in tests. 
To achieve this simply pass information about one or more desired links via capability:
Type: array, format: <container-name>[:alias]

```applicationContainers: ["spring-application-main:my-cool-app", "spring-application-gateway"]```


### При написании кода смотреть лекцию 8!

# Jenkins
Развернут на порту 8888

```systemctl start/stop jenkins.service```

# Docker
```docker run -p9000:9000 --name mock -d vk_api:latest``` - запустить мок
 http://0.0.0.0:9000/vk_id/artnovopolsky - на нем живет mock на flask 

```docker inspect CONTAINER_NAME | grep "IPAddress"``` - узнать ip контейнера

```docker-compose up``` - запустить контейнеры
```docker-compose down``` - остановить и удалить контейнеры
```docker-compose up --abort-on-container-exit``` - запустить контейнеры и выйти сразу же, как только один из контейнеров завершится


# MySQL 
root_password=admin

```sudo kill $(sudo lsof -t -i:3306)``` - принудительно закрыть 3306 порт

```docker run --name mysql_db -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 -d percona:latest``` - запустить контейнер с бд

```mysql -h127.0.0.1 -P3306 -uroot -padmin``` - подключиться к базе данных

DB_MYAPP - база данных 
test_users - таблица

```CREATE USER 'test_qa'@'%' IDENTIFIED BY 'qa_test';``` - создание пользователя

```GRANT ALL PRIVILEGES ON * . * TO 'test_qa'@'%';```- предоставление ему неограниченных прав

```FLUSH PRIVILEGES;``` - изменения вступили в силу

```SELECT user,host FROM mysql.user WHERE user LIKE "%%";``` - посмотреть права пользователей mysql


# Запуск приложения
```docker run --name cool_app -v /home/artnovopolsky/mailru-course/my-repos/final_project:/project -p 9999:9999 --link mysql_db:mysql_db --link mock:mock -d myapp /app/myapp --config=/project/myapp.conf```


# Вопросы
При прогоне тестов должны создаваться новые контейнеры? (Логично, что да)


# Баги
1. В форме регистрации при неправильном вводе более одного поля сообщение об ошибке отображается некорректно
2. При вводе username валидной длины русскими буквами (c учётом, что остальные поля введены верно) сервер отвечает 500 ошибкой (Internal Server Error). 
3. Если при регистрации пользователем указывается email, который уже есть в БД, сервер отвечает 500 (Internal Server Error)
4. При регистрации у полей Email и Repeat password нет атрибута required (если нажать кнопку Register не вылетит нотификейшн "Заполните это поле")
5. При попадании на главную страницу не отображается findMeError.js, выдаёт 404 ошибку
6. При отсутствии у пользователя VK ID поле на странице заполнено пробелами (?)
7. Кнопки Python и Python history открывают сторонние ссылки не в соседней вкладке (?)
8. Кнопка Download Centos7 ведёт на скачивание Fedora
9. start_active_time в БД после выхода не проставляется в NULL (? возможно этого и не должно быть, в доке написано только про access)
10. 
11. 
