clean:
	@find . -name "*.pyc" -delete
	@find . -name "*__pycache__" -delete

	@rm -rf ".coverage" 
	@rm -rf "build"
	@rm -rf "dist"
	@rm -rf "py_database_url.egg-info"

tests: clean fmt lint
	@PYTHONPATH=py_database_url pytest --cov=py_database_url tests/

lint:
	@pycodestyle --ignore=E501 .

fmt:
	@black .

publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
