# Yandex.Cloud. Serverless-функция для переноса кластеров баз данных в другие сети
1. [Создать сервисный аккаунт](https://cloud.yandex.ru/docs/iam/operations/sa/create)
1. [Выдать права доступа к кластерам БД](https://cloud.yandex.ru/docs/iam/operations/sa/assign-role-for-sa)
1. [Создать функцию](https://cloud.yandex.ru/docs/functions/quickstart/function-quickstart) 
Для запуска кода из репозитроия необходимо сохранить его содержимое в zip-архив и передать в форме редактирования после указания соответствующего метода загрузки.
1. Запуск и тестирование:

`curl -s -XPOST 'https://functions.yandexcloud.net/{function_id}?cluster_id={cluster_id}&network_id={network_id}&subnet_id={subnet_id}' -H "Authorization: Bearer $(yc iam create-token)"`

Query-Параметры для запуска:
1. *cluster_id* - ID изменяемого кластера
1. *network_id* - ID сети VPC, в которой будет располагаться новый кластер
1. *subnet_id* - ID подсети VPC, в которой будет располагаться новый кластер
1. (opt.) *redis_password* - Пароль для подключения (только для RedisDB)
1. (opt.) *new_name* - имя, под которым будет создан новый кластер. Без указания данного параметра, новый кластер будет называться, как и старый