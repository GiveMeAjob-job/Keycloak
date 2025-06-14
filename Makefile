kind-test:
	./scripts/kind-test.sh

helm-package:
	mkdir -p dist/charts
	helm lint ./charts/*
	helm package ./charts/* -d dist/charts
