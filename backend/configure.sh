#!/bin/bash
# configure stuff
# set -e
# set -x
# set -o pipefail
# # set -u
echo "Configuring stuff"

cat /dev/null > .env

echo "================="
echo "== AWS Secrets =="
echo "================="

GENAI_TUTOR_SECRET="${GENAI_TUTOR_SECRET:-arc/genai-tutor}"
ARC_LDAP_SECRET="${ARC_LDAP_SECRET:-arc/ldap_insight_gsu_edu}"

aws secretsmanager get-secret-value --secret-id $GENAI_TUTOR_SECRET \
| jq -r ".SecretString" | jq . \
| jq -r 'to_entries | .[] | "export \(.key | ascii_upcase)=\"\(.value)\""' \
>> .env

cat << EOF >> .env
export DB_HOST="${DB_HOST}"
export CHROMADB_PORT="${CHROMADB_PORT}"
export POSTGRES_PORT="${POSTGRES_PORT}"
export AUTHENTICATION_PORT="${AUTHENTICATION_PORT}"
export AI_APPLICATION_PORT="${AI_APPLICATION_PORT}"
export CHROMADB_BASE_URL="${CHROMADB_BASE_URL}"
export OLLAMA_BASE_URL="${OLLAMA_BASE_URL}"
export AI_APPLICTATION_BASE_URL="${AI_APPLICTATION_BASE_URL}"
export CHROMADB_STORAGE="${CHROMADB_STORAGE}"
export POSTGRES_STORAGE="${POSTGRES_STORAGE}"
EOF
echo "================"
echo "Done."
