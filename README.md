run git clone `git clone https://github.com/OksanaBelotelova/Terms_of_Reference_JuniorAQA_Python.git`

run tests image build `docker build -t junior-aqa-tests ./`

pull selenoid/chrome:128.0 image `docker pull selenoid/chrome:128.0`

run docker composed container `docker compose -f 'docker-compose.yml' up -d --build`
