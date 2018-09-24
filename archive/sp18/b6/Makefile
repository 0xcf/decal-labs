venv:
	virtualenv -ppython3 venv
	. venv/bin/activate && pip install -r requirements.txt

.PHONY: run
run: venv 
	export FLASK_APP=app.py && venv/bin/python -m flask run --host=0.0.0.0
