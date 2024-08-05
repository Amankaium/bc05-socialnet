# Как развернуть проект?
git clone ...
create and activate venv
pip install -r requirements.txt
создать БД в postgres и прописать в settings.py
python manage.py migrate
python manage.py runserver