export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

serve: ## Start the development server
	open http://localhost:8000/
	python3 -m http.server 8000

icons: ## Generate icons
	./mk-icns.sh

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo
