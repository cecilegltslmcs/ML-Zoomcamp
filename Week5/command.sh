# create a pipenv
pipenv install numpy scikit-learn flask waitress gunicorn
pipenv install ebawscli --dev

# launch a shell with pipenv
pipenv shell

# run with entering the shell
pipenv run waitress-serve --listen=*:9696 predict:app
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app

# run app with fastAPI & uvicorn
pipenv run uvicorn api:app --reload
uvicorn api:app --reload


# build a docker image from dockerfile
docker build -t zoomcamp-test .

# run docker image
docker run -it -rm -p 9696:9696 zoomcamp-test

# delete docker image
docker builder prune

# init elasticbeantalk
eb init -p "Docker running on 64bit Amazon Linux 2" -r eu-west-3 churn-serving

# test locally
eb local run --port 9696

# create on the cloud
eb create churn-serving-env
