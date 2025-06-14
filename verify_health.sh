#!/usr/bin/env bash
set -e
for i in {1..30}; do
  status=$(curl -sf http://localhost/health || true)
  if [[ "$status" == "ok" ]]; then
    echo "healthy"; exit 0
  fi
  sleep 2
done
exit 1
