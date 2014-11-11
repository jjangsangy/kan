init:
	pip install -r requirements.txt

test:
	nosetests

.PHONY: clean

rst:
	pandoc --from=markdown_github --to=rst README.md -o README.rst

build:
	python setup.py build

dist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

install:
	pip2 install kan
	pip3 install kan

uninstall:
	pip3 uninstall kan
	pip2 uninstall kan

publish:
	pandoc --from=markdown_github --to=rst README.md -o README.rst
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel upload -r pypi

clean:
	rm -rf kan/*.pyc
	rm -rf __pycache__
	rm -rf kan/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist

