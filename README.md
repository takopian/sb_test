# Test assignment
API description is available at `http://localhost:3000/api/docs`

Build docker image:\
`docker build . -t app:latest`

Run container:\
`docker run -d --name app -p 3000:3000/tcp -t app:latest`

Run tests:\
`docker exec  app coverage run -m unittest`

Check code coverage:\
`docker exec  app coverage report -m`