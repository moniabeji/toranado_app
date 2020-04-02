```
docker run -p 5432:5432 --name pg postgres

docker run -p 5555:80 --name pgadmin -e PGADMIN_DEFAULT_EMAIL="monia" -e PGADMIN_DEFAULT_PASSWORD="password"  dpage/pgadmin4

test it with "localhost:5555"