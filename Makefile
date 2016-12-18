init:
	pip install -r requirements.txt

test:
	nosetests --with-coverage --cover-package=hpds
