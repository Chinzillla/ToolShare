# set -e stops when command fails and set -u fails when required variable is missing
set -eu

alias_name="local"

# Connecting MiniIO client to server
mc alias set \
  "$alias_name" \
  "$MINIO_ENDPOINT" \
  "$MINIO_ROOT_USER" \
  "$MINIO_ROOT_PASSWORD"

# Create the buckets
for bucket in \
  "$EQUIPMENT_PHOTOS_BUCKET" \
  "$PICKUP_PHOTOS_BUCKET" \
  "$RETURN_PHOTOS_BUCKET" \
  "$DISPUTE_EVIDENCE_BUCKET"
do
# Makes creation repeatable and removes public access
  mc mb --ignore-existing "$alias_name/$bucket"
  mc anonymous set none "$alias_name/$bucket"
done

mc ls "$alias_name"