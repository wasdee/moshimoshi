format:
	pre-commit run --all-files

publish:
	poetry build -f wheel
	poetry publish
