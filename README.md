# ML API з FastAPI та Docker

Цей проект містить API для машинного навчання, який класифікує квіти ірису за допомогою натренованої моделі Random Forest.

## Структура проекту

```
deployment/
├── model/                 # Папка з артефактами моделі
│   ├── model.joblib       # Натренована модель
│   └── target_names.json  # Назви класів
├── app.py                 # FastAPI додаток
├── Dockerfile             # Docker конфігурація
├── requirements.txt       # Python залежності
├── model.py               # Скрипт для тренування моделі
└── README.md              # Цей файл
```

## Встановлення та запуск

### Крок 1: Підготовка моделі

Натренуйте модель запустивши скрипт у кореневій папці:

```bash
python model.py
```

Це створить папку `model/` з файлами:
- `model/model.joblib` - натренована модель
- `model/target_names.json` - назви класів

### Крок 2: Збірка Docker образу

Зберіть Docker образ:

```bash
docker build -t ml-iris-api .
```

### Крок 3: Запуск контейнера

Запустіть контейнер з API:

```bash
docker run -d -p 8000:8000 --name iris-api ml-iris-api
```

Параметри команди:
- `-d` - запуск у фоновому режимі
- `-p 8000:8000` - прокидання порту 8000 з контейнера на хост
- `--name iris-api` - назва контейнера
- `ml-iris-api` - назва образу

## Використання API

### Перевірка роботи

Відкрийте браузер та перейдіть за адресою:
```
http://localhost:8000
```

Ви побачите повідомлення: `{"message": "Welcome to the ML Model API"}`

### Інтерактивна документація

FastAPI автоматично генерує документацію:
```
http://localhost:8000/docs
```

### Виконання прогнозу

Відправте POST запит на `/predict/` з даними квітки:

```bash
curl -X POST "http://localhost:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{
       "features": [5.1, 3.5, 1.4, 0.2]
     }'
```

Відповідь буде містити клас квітки:
```json
{"class": "setosa"}
```

### Приклад з Python

```python
import requests

url = "http://localhost:8000/predict/"
data = {
    "features": [6.3, 2.9, 5.6, 1.8]
}

response = requests.post(url, json=data)
print(response.json())  # {"class": "virginica"}
```

## Керування контейнером

### Перегляд логів

```bash
docker logs iris-api
```

### Зупинка контейнера

```bash
docker stop iris-api
```

### Видалення контейнера

```bash
docker rm iris-api
```

### Видалення образу

```bash
docker rmi ml-iris-api
```

## Налагодження

### Перевірка запущених контейнерів

```bash
docker ps
```

### Підключення до контейнера

```bash
docker exec -it iris-api /bin/bash
```

### Перевірка портів

```bash
netstat -tulpn | grep :8000
```

## Запуск без Docker

Для локального запуску без Docker:

```bash
# Встановіть залежності
pip install -r requirements.txt

# Запустіть сервер
uvicorn app:app --reload
```

## Технічні деталі

- **Framework**: FastAPI
- **Server**: Uvicorn
- **ML Model**: Random Forest Classifier
- **Dataset**: Iris flowers
- **Python Version**: 3.12
- **Port**: 8000

## Характеристики моделі

Модель класифікує квіти ірису на 3 класи:
- `setosa` - Ірис щетинистий
- `versicolor` - Ірис різнобарвний  
- `virginica` - Ірис віргінський

Вхідні дані (features) - це 4 параметри квітки:
1. Довжина чашолистка (sepal length)
2. Ширина чашолистка (sepal width)
3. Довжина пелюстки (petal length)
4. Ширина пелюстки (petal width)

## Підтримка

Якщо виникають проблеми:
1. Перевірте, чи встановлений Docker
2. Переконайтеся, що порт 8000 не зайнятий
3. Перевірте логи контейнера
4. Переконайтеся, що папка `model/` існує та містить необхідні файли 