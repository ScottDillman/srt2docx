setup:
	@python3 -m venv pyenv; \
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
test:
	@mkdir -p test; \
	curl -k -L -s -o test/zardoz.zip "https://yifysubtitles.ch/subtitle/zardoz-1974-english-yify-139818.zip"; \
	cd test; \
	unzip -o zardoz.zip; \
	../srt2docx 2>&1 | tee test.log
clean:
	@rm -rf test
git-show:
	@git log --graph --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%an%C(reset)%C(bold yellow)%d%C(reset) %C(dim white)- %s%C(reset)' --all

.PHONY: test git-show format fix lint clean
