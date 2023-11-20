# create image repository
aws ecr create-repository --repository-name clothing-tfile-images

# login to ecr service
$(aws ecr get-login --no-include-email)

# send docker images in ecr
docker tag clothing-model:latest ${REMOTE_URI}
docker push ${REMOTE_URI}