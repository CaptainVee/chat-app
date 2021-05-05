release: python manage.py migrate
web: daphne zuri-chat.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=zuri-chat.settings -v2