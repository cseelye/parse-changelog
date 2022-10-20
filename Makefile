SHELL := /usr/bin/env -S bash -euET -o pipefail -O inherit_errexit


.PHONY: clean
clean:
	$(RM) -r dist *.egg-info
