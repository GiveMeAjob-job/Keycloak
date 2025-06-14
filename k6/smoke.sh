#!/bin/bash
set -e
k6 run k6/scripts/auth-login.js --vus 1 --duration 30s
