SERVICE_NAME = bff-authors-service

.PHONY: install
install: ## install the code locally including all development dependencies)
	. .venv/bin/activate && \
	pip install -e .[dev]


.PHONY: clean
clean: ## (clean up temp & local build files)
	find . -type d -name __pycache__ -exec rm -r {} +
	rm -rf *.egg-info
	rm -rf .mypy_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf tmp/
	rm -rf .pytest_cache/
	rm -rf *.log


.PHONY: format
format: ## run auto formatting tools
	isort -l 119 ./
	black --line-length 119 ./


.PHONY: freeze
freeze: ## Freeze requirements
	. .venv/bin/activate && \
	pip-compile requirements.in > requirements.txt


.PHONY: lint
lint: ## run linters
	. .venv/bin/activate && \
	flake8 ./ && \
	mypy .


.PHONY: image
image: ## run linters
	docker build -f backend.dockerfile -t $(SERVICE_NAME) ./


.PHONY: container
container: ## run linters
	docker run -d --rm -p 8000:80 $(SERVICE_NAME):latest


.venv/bin/activate:
	`which python` -m venv .venv
	. $@
	touch $@
