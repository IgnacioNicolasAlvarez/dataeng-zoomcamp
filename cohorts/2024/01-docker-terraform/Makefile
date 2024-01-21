run-postgres:
	docker run -it -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -v ./postgres-db-volume:/var/lib/postgresql/data postgres:13.1

run-pgcli:
	pgcli -h localhost -U myuser -d mydatabase -W