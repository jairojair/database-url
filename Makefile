clean:
	@find . -name "*.pyc" -delete
	@find . -name "*__pycache__" -delete

	@rm -rf ".coverage" 
	@rm -rf "build"
	@rm -rf "dist"
	@rm -rf "py_database_url.egg-info"

tests: clean fmt lint
	@pytest --cov=py_database_url

lint:
	@pycodestyle --ignore=E501 .

fmt:
	@black .

publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
