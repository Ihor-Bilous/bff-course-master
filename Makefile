.PHONY: build-all
build-all: ## Build all images
	$(MAKE) -C books image && \
	$(MAKE) -C authors image && \
	$(MAKE) -C frontend-agr image && \
	$(MAKE) -C frontend-agr-mobile image && \
	$(MAKE) -C push-gw image && \
	$(MAKE) -C api-gateway-frontend image && \
	$(MAKE) -C api-gateway-mobile image && \
	$(MAKE) -C clients image
