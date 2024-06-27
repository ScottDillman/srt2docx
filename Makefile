setup:
	@python -m venv pyenv; \
	source ./pyenv/bin/activate; \
	pip install -r requirements.txt; \
	echo activate env with: source ./source-me
requirements:
	@pip freeze > requirements.txt
lint:
	@ruff check .
fix:
	@ruff check . --fix
format:
	@ruff format .
git-show:
	@git log --graph --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%an%C(reset)%C(bold yellow)%d%C(reset) %C(dim white)- %s%C(reset)' --all