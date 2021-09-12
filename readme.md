# Django Ecommerce Website

## common commands

> ## to save dependencies

```
pip freeze > requirements.txt
```

---

> ## to set up project dependencies and virual environment (freshly downloaded)

### globally

```
python3 -m pip install virtualenv
pip3 install virtualenv # alternative way
```

### locally

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

> ## to run django project

```
python manage.py migrate
python manage.py runserver
```

---
