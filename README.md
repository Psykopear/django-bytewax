# Djangowax
This is an example django app, and a bytewax dataflow that has access to the django orm.

Run the usual setup commands:
```bash
python -m venv .venv
source .venv/bin/activate
pip install django bytewax
cd djangowax
python manage.py migrate
python manage.py load_test_data
python -m bytewax.run dataflow
```