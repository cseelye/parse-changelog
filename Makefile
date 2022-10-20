SHELL := /usr/bin/env -S bash -euET -o pipefail -O inherit_errexit

.PHONY: package
package:
	python setup.py sdist
	python setup.py bdist_wheel --universal

.PHONY: test-publish
test-publish: package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: publish
publish:
	twine upload dist/*

.PHONY: clean
clean:
	$(RM) -r build *.egg-info

.PHONY: clobber
clobber: clean
	$(RM) -r dist
