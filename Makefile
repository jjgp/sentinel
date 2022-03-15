.PHONY: help
help:
	@echo "make clean:\n    remove build/runtime artifacts\n"

.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d \
		-name "*.egg-info" \
		-name __pycache__ \
		-name .ipynb_checkpoints \
		-name venv \
		-delete
