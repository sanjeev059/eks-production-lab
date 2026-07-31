#!/usr/bin/env bash
#
# create-payments-structure.sh
# Creates the `payments/` project scaffold in the current directory.
#
# Usage:
#   ./create-payments-structure.sh          # creates ./payments
#   ./create-payments-structure.sh mydir    # creates ./mydir/payments
#
set -euo pipefail

BASE="${1:-.}"
ROOT="$BASE/payments"

echo "Creating structure under: $ROOT"

# --- directories ---
mkdir -p "$ROOT/app/tests"
mkdir -p "$ROOT/gitops"
mkdir -p "$ROOT/bootstrap"
mkdir -p "$ROOT/observability/prometheus"
mkdir -p "$ROOT/observability/grafana"
mkdir -p "$ROOT/observability/dashboards"
mkdir -p "$ROOT/docs"

# --- files ---
# app/  <-- Source Code
touch "$ROOT/app/app.py"
touch "$ROOT/app/Dockerfile"
touch "$ROOT/app/requirements.txt"
touch "$ROOT/app/Jenkinsfile"

# gitops/  <-- ArgoCD watches this
touch "$ROOT/gitops/application.yaml"
touch "$ROOT/gitops/deployment.yaml"
touch "$ROOT/gitops/service.yaml"
touch "$ROOT/gitops/ingress.yaml"
touch "$ROOT/gitops/configmap.yaml"
touch "$ROOT/gitops/namespace.yaml"

# bootstrap/  <-- Installation scripts
touch "$ROOT/bootstrap/install-argocd.sh"
touch "$ROOT/bootstrap/install-prometheus.sh"
touch "$ROOT/bootstrap/install-grafana.sh"
touch "$ROOT/bootstrap/install-ingress.sh"
touch "$ROOT/bootstrap/install-jenkins.sh"

# docs/
touch "$ROOT/docs/CRD.md"
touch "$ROOT/docs/ArgoCD.md"
touch "$ROOT/docs/Jenkins.md"
touch "$ROOT/docs/RBAC.md"
touch "$ROOT/docs/Troubleshooting.md"

echo "Done."
echo
# Show the result if 'tree' is available, otherwise fall back to find.
if command -v tree >/dev/null 2>&1; then
  tree "$ROOT"
else
  find "$ROOT" | sort
fi

