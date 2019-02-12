VENV_DIR 	= venv

ifeq ($(OS),Windows_NT)
    PYTHON_BIN = $(VENV_DIR)/Scripts
else
    PYTHON_BIN = $(VENV_DIR)/bin
endif

FLASK		= $(PYTHON_BIN)/flask
FLASK_APP	= {{cookiecutter.package_name}}.app
NODE		= frontend/node_modules


install: $(VENV_DIR)
	@$(PYTHON_BIN)/pip install -e backend

uninstall:
	@rm -r $(VENV_DIR)

run: $(VENV_DIR)
	@FLASK_APP=$(FLASK_APP) $(PYTHON_BIN)/flask run --host=0.0.0.0

webpack: $(NODE)
	@cd frontend && node_modules/.bin/webpack

$(VENV_DIR):
	@mkdir -p $@ && virtualenv --python=python3 $@

$(NODE):
	@cd frontend && npm install
