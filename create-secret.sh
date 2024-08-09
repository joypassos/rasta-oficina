#!/usr/bin/bash -e

# Create a file with the credentials
echo -n "${OCI_CLI_USER}:${OCI_CLI_TENANCY}:${OCI_CLI_FINGERPRINT}:${OCI_CLI_KEY_CONTENT}:${OCI_CLI_REGION}" > credentials.txt
base64 -w 0 credentials.txt > credentials.base64

# Create the secret
kubectl create secret generic oci-creds -n crossplane-system --from-file=credentials=credentials.base64