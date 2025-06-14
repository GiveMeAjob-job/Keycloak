#!/usr/bin/env bash
set -e
kind create cluster --wait 60s
kubectl wait --for=condition=Ready nodes --all --timeout=60s
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl apply -f k8s/dev/
./verify_health.sh
