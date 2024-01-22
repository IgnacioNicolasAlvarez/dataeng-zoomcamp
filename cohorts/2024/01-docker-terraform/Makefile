run-postgres:
	docker run -it --name pg-database --network=pg-network -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -v ./postgres-db-volume:/var/lib/postgresql/data postgres:13.1

run-pgcli:
	pgcli -h localhost -U myuser -d mydatabase -W

run-pgadmin:
	docker run --network=pg-network -p 8080:80 -e 'PGADMIN_DEFAULT_EMAIL=test@test.com' -e 'PGADMIN_DEFAULT_PASSWORD=password' dpage/pgadmin4
