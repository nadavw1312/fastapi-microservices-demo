# Variables
USERS_IMAGE_NAME=nadavw1312/users-service
USERS_ALEMBIC_IMAGE_NAME=nadavw1312/users-alembic-service
DB_IMAGE=postgres:15
NAMESPACE=development
DB_VOLUME_PATH=/run/desktop/mnt/host/c/Users/nadav/postgres_data

# -------------------------------------------
# Docker Commands
# -------------------------------------------

# Build and Push Docker Image (from users_service folder)
update-users-docker:
	cd users_service && docker build -t $(USERS_IMAGE_NAME):latest -f Dockerfile .
	docker push $(USERS_IMAGE_NAME):latest

update-users-migration-docker:
	cd users_service && docker build -t $(USERS_ALEMBIC_IMAGE_NAME):latest -f Dockerfile.alembic .
	docker push $(USERS_ALEMBIC_IMAGE_NAME):latest

update-all-users-dockers: update-users-docker update-users-migration-docker

# -------------------------------------------
# Kubernetes Commands for Development
# -------------------------------------------

# Apply all Kubernetes resources for development
apply-dev-users:
	kubectl apply -f k8s/users/dev

# Delete all Kubernetes resources for development
delete-dev-users:
	kubectl delete -f k8s/users/dev

# Start PostgreSQL with Persistent Volume in development
start-postgres:
	kubectl apply -f k8s/users/dev/db-deployment.yaml
	kubectl apply -f k8s/users/dev/db-service.yaml

# Deploy Users Service in development
deploy-users-service:
	kubectl apply -f k8s/users/dev/deployment.yaml
	kubectl apply -f k8s/users/dev/service.yaml

# Run Alembic Migrations in development
run-migrations:
	kubectl apply -f k8s/users/dev/alembic-migration-job.yaml
	kubectl logs job/users-alembic-migration -n $(NAMESPACE)

# Restart Users Service in development
restart-users-service:
	kubectl rollout restart deployment users-service -n $(NAMESPACE)

# Clean PostgreSQL Data (local)
clean-db:
	rm -rf $(DB_VOLUME_PATH)/*

# Full Deployment Pipeline for development
deploy-all: update-users-docker apply-dev-users run-migrations deploy-users-service

# -------------------------------------------
# Kubernetes Commands for Production
# -------------------------------------------

# Apply all Kubernetes resources for production
apply-prod-users:
	kubectl apply -f k8s/users/prod

# Delete all Kubernetes resources for production
delete-prod-users:
	kubectl delete -f k8s/users/prod

.PHONY: \
	update-users-docker \
	apply-dev-users delete-dev-users \
	start-postgres deploy-users-service run-migrations restart-users-service clean-db deploy-all \
	apply-prod-users delete-prod-users
