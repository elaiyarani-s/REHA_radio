# REHA Radio 🎧

A real-time Django-based radio streaming and communication platform built with Django Channels, Daphne, Redis, and REST APIs.

---

## 🚀 Features

- ✅ Django 5.x with ASGI support
- 📡 Real-time communication using **WebSockets** via **Django Channels**
- 🔄 Live browser reload during development
- 🔗 CORS support for frontend-backend integration
- 🌐 RESTful API using Django REST Framework
- 🧹 Auto file cleanup with WhiteNoise static files support

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework, Channels, Daphne
- **Real-time**: Channels + Redis + Daphne (ASGI server)
- **Deployment**: Render / Docker-ready
- **Static Handling**: WhiteNoise
- **Dev Tools**: `django-browser-reload`, `python-decouple`

---

## 📦 Requirements

See [`requirements.txt`](./requirements.txt) for the full list of dependencies.

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/elaiyarani-s/REHA_radio.git
cd REHA_radio
```

### 2. Setup environment

Create a `.env` file (or use `python-decouple`) and add:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-postgres-url
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 3. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

Or for ASGI (WebSockets):

```bash
daphne reha_radio.asgi:application
```

---

## 🌐 WebSocket Setup

If using Channels:

```python
# In settings.py
ASGI_APPLICATION = "reha_radio.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
```


---

## 📁 Folder Structure

```bash
.
└── reha_radio
    ├── Procfile
    ├── chat    # Chat app logic
    ├── core    # Main app logic
    ├── manage.py
    ├── reha_radio  # Django project settings
    ├── static
    ├── templates
    └── requirements.txt

```

---

## 📤 Deployment (Render / Heroku)

1. Add a `Procfile`:
   ```
   web: daphne reha_radio.asgi:application --port $PORT
   ```

2. Add environment variables in Render dashboard.

3. Set `DEBUG=False` and configure `ALLOWED_HOSTS`.

---

## ✨ Credits

Developed by [@elaiyarani-s](https://github.com/elaiyarani-s).
