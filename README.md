# FastAPI Hexagonal Architecture Example

This project is a REST API built with FastAPI, following the Hexagonal Architecture (Ports and Adapters) pattern.
It is designed to be modular, testable, and easy to evolve.

## Architecture

The project uses Hexagonal Architecture, separating:

- **Adapters:** External implementations (HTTP, database, etc.);
- **Application:** Services, validators and application exceptions;
- **Config:** Framework-related configurations (error handling, dependency injection, etc.)
- **Domain:** Core business rules and entities;
- **Ports:** Inbound and outbound protocols that define application boundaries.

This approach keeps the business logic independent of frameworks and external services.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Poetry
- Pytest for testing
- Testcontainers for integration tests
- Docker (optional, for containers)

## Running locally

### Via IDE

1. Run the command below to install the project dependencies:

   ```bash
   poetry install --no-root
   ```

2. Start a PostgreSQL (run the command below to start it in Docker);

    ```bash
    docker compose up -d postgres
    ```

3. Change the following environment variables if needed:
   
   | ENV         | Type | Default Value | Description               |
   |-------------|------|---------------|---------------------------|
   | DB_HOST     | str  | localhost     | Database host address     |
   | DB_PORT     | int  | 5432          | Database port             |
   | DB_NAME     | str  | hexagonal     | Database name             |
   | DB_USER     | str  | postgres      | Database username         |
   | DB_PASSWORD | str  | root          | Database user password    |
   | SHOW_SQL    | bool | false         | Enables SQL query logging |
   
   *Obs.: the default values correspond to the `compose.yaml` configuration*

4. Start the application with your favorite IDE or run command below via terminal:
   
   ```bash
   fastapi dev src/main.py
   ```

## Testing

This project uses **Testcontainers** to spin up real infrastructure dependencies (PostgreSQL)
during integration tests, ensuring production-like behavior.

Before running the API tests with `pytest`, be sure to have `Docker` running. Then run the command:

```bash
poetry run pytest
```

Or if you want to see test coverage:

```bash
poetry run pytest --cov
```
