BUILD_DIR ?= _build/html
DOCS_DIR ?= .

.PHONY: docs strict clean

docs:
	sphinx-build -b html $(DOCS_DIR) $(BUILD_DIR)

strict:
	sphinx-build -W --keep-going -b html $(DOCS_DIR) $(BUILD_DIR)

clean:
	rm -rf _build
