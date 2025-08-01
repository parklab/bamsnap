.PHONY: build test

configure:
	pip install --upgrade pip
	pip install poetry

build:
	make configure
	poetry install

update:
	poetry update

test:
	poetry run pytest

help:
	@make info

info:
	@: $(info Here are some 'make' options:)
	   $(info - Use 'make configure' to configure the repo by installing poetry.)
	   $(info - Use 'make build' to install entry point commands.)
	   $(info - Use 'make update' to update dependencies (and the lock file).)

