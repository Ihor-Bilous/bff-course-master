.PHONY: build-all
build-all: ## Build all images
	$(MAKE) -C books image && \
	$(MAKE) -C authors image && \
	$(MAKE) -C push-gw image && \
	$(MAKE) -C clients image
