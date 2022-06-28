.PHONY: init

init:
	make down
	make up
	make ps
	make migrate
down:
	docker-compose down --volumes --remove-orphans
build:
	docker-compose build
up:
	docker-compose up -d
migrations:
	@make up
	docker exec -it core python manage.py makemigrations
migrate:
	@make up
	docker exec -it core python manage.py migrate
su:
	@make up
	docker exec -it core python manage.py createsuperuser
test:
	@make up
	docker exec core python manage.py test .
bash:
	@make up
	docker exec -it core python manage.py shell
format:
	@make up
	docker exec -it core black .
lint:
	@make up
	docker exec -it core black . --check
prune:
	make down
	docker volume prune -f
	docker system prune -f
logs:
	docker-compose logs -f --tail 100
