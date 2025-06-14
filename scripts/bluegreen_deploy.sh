#!/bin/bash
set -euo pipefail

COLOR=${COLOR:-green}
RELEASE=${RELEASE:-keycloak}
NAMESPACE=${NAMESPACE:-keycloak}
INGRESS=${INGRESS:-keycloak}

helm upgrade --install "$RELEASE" charts/keycloak \
  --namespace "$NAMESPACE" --create-namespace \
  --set color="$COLOR"

# Gradual traffic shift
kubectl annotate ingress "$INGRESS" \
  nginx.ingress.kubernetes.io/canary=true \
  nginx.ingress.kubernetes.io/canary-weight=10 --overwrite
sleep 30
kubectl annotate ingress "$INGRESS" \
  nginx.ingress.kubernetes.io/canary-weight=100 --overwrite
