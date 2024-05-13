#
# Definitions
#

# Docker compose which the services are defined.
COMPOSE_FILE = docker-compose.yml

# Utility
RUN_IN_CONTAINER = docker compose -f $(COMPOSE_FILE) exec $(CONTAINER_BASE) $(COMMAND)

#
# Application
#
up:   ## Start application (default)
	docker compose -f $(COMPOSE_FILE) up -d


down:  ## Stop application
	docker compose -f $(COMPOSE_FILE) down

#
# Documentation function (thanks for https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html)
#
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
