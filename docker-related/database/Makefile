# Windows		:	mingw32-make
# linux/macOS	:	make
# https://opensource.com/article/18/8/what-how-makefile
# https://docs.docker.com/compose/profiles/
# https://stackoverflow.com/questions/50379839/connection-java-mysql-public-key-retrieval-is-not-allowed

.PHONY: compose_up stop # define all the targets that are not files so that make will not get confused
# all: say_hello generate # run more than one target
# .DEFAULT_GOAL := clean # run specific target

phpadmin = 0
help:
	@echo "compose_up, compose_down, compose_stop, compose_remove, compose_remove_all, compose_start, clean_all, clean_others, clean_container, clean_images"
	@echo "argument: phpadmin = 1 or 0 (default=0)"

compose_up:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug --env-file .sql.env up ;\
	else\
		docker compose -f mysql.yaml --env-file .sql.env up ;\
	fi;
compose_down:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug down ;\
	else\
		docker compose -f mysql.yaml down ;\
	fi;

compose_stop:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug stop ;\
	else\
		docker compose -f mysql.yaml stop ;\
	fi;

compose_remove:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug rm --force --stop ;\
	else\
		docker compose -f mysql.yaml rm --force --stop ;\
	fi;
compose_remove_all:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug rm --force --stop --volumes;\
	else\
		docker compose -f mysql.yaml rm --force --stop --volumes;\
	fi;

compose_start:
	@if [ $(phpadmin) = 1 ]; then\
		docker compose -f mysql.yaml --profile debug --env-file .sql.env start ;\
	else\
		docker compose -f mysql.yaml --env-file .sql.env start ;\
	fi;

clean_all:
	docker stop $(shell docker ps -aq)
	docker rm -f $(shell docker ps -aq)
	docker rmi -f $(shell docker images -aq)
	docker system prune -a --force
	docker network prune --force
	docker volume prune --force
	docker container prune --force
	docker image prune --force

clean_others:
	docker network prune --force
	docker volume rm $(shell docker volume ls -q -f dangling=true)
	docker volume prune --force

clean_container:
	docker stop -f $(shell docker ps -aq)
	docker rm -f $(shell docker ps -aq)
	docker container prune --force

clean_images:
	docker rmi -f $(shell docker images -aq)