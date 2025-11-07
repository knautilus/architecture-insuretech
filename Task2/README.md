## Запуск а Windows 11

Установить и запустить Docker Desktop.

Установить minikube (например, с помощью Chocolatey).

Поднять локальный кластер Kubernetes в Minikube:

```bash
minikube start
```

Активировать metrics-server:

```bash
minikube addons enable metrics-server
```

Создать неймспейс:

```bash
kubectl create namespace sprint8
```

Установка locust (необходимо выполнять из директории Task2)

```bash
pip install locust
```

Применить манифесты. В директории Task2 выполнить команды:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Проброс портов:

```bash
kubectl port-forward svc/scaletestapp-svc 8080:8080
```

Запуск locust (необходимо выполнять из директории Task2):

```bash
locust
```

После запуска Locust открыть веб-браузер и ввести адрес http://localhost:8089. В веб-интерфейсе Locust можно настроить параметры теста: количество пользователей и hatch rate — скорость, с которой генерируются новые пользователи

Открыть дашборд Kubernetes:

```bash
minikube dashboard
```

Без нагрузки:

![Screenshot1](./Screenshot1.jpg)

Под нагрузкой:

![Screenshot2](./Screenshot2.jpg)
