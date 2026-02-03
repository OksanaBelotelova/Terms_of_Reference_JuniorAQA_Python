run tests image build `docker build -t junior-aqa-tests ./`

pull selenoid/chrome:128.0 image `docker pull selenoid/chrome:128.0`

run docker composed container `docker compose -f 'docker-compose.yml' up -d --build`