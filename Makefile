SHELL := /usr/bin/env -S bash -euET -o pipefail -O inherit_errexit

.PHONY: lint
lint:
	pylint bin/* parse_changelog/*
	ruff bin/* parse_changelog*

.PHONY: package
package: write-version
	python setup.py sdist
	python setup.py bdist_wheel --universal

.PHONY: write-version
write-version:
	./write-version-file

.PHONY: test-publish
test-publish: package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: publish
publish:
	twine upload dist/*

.PHONY: clean
clean:
	$(RM) -r build *.egg-info
	$(RM) -r parse_changelog/__pycache__ parse_changelog/VERSION

.PHONY: clobber
clobber: clean
	$(RM) -r dist
