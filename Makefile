kind-test:
	./scripts/kind-test.sh

helm-package:
	mkdir -p dist/charts
	helm lint ./charts/*
	helm package ./charts/* -d dist/charts

rollback:
	@if [ -z "$(ENV)" ] || [ -z "$(REVISION)" ]; then \
		echo "Usage: make rollback ENV=prod REVISION=1"; exit 1; \
	fi
	helm rollback keycloak $(REVISION) -n $(ENV)
