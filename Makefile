format:
	pre-commit run --all-files

publish: format
	poetry build -f wheel
	poetry publish
