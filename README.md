# Backend Task - Clean Architecture

This project is a very naive implementation of a simple shop system. It mimics in its structure a real world example of a service that was prepared for being split into microservices and uses the current Helu backend tech stack.

## Goals

Please answer the following questions:

1. Why can we not easily split this project into two microservices?
- The project seems to be tightly coupled. For instance, the database session middleware is directly integrated into 
`app.py`. This means that the database is a shared resource between the user and item services,
making it difficult to separate them into independent microservices. Additionally, the user and item modules are 
both included in the same FastAPI application, which suggests that they are not designed to operate independently.

2. Why does this project not adhere to the clean architecture even though we have seperate modules for api, repositories, usecases and the model?
- For instance, the `get_db` function in `common.py` directly accesses the `request` object, which is a detail of the web 
framework. In clean architecture, such details should be abstracted away from the business logic. Also, 
the `create_item` and `get_all` use cases in `model.api.py` directly depend on the database session, which is another
detail that should be abstracted away.

3. What would be your plan to refactor the project to stick to the clean architecture?
- Abstract away framework details, instead of directly accessing the `request` object or the database session, 
we could create interfaces that hide these details. For instance, we could create a Database interface that provides 
methods for starting and closing a session, and a Request interface that provides methods for getting and setting state.
- Separate the application into distinct layers. We could create separate layers for entities (the business objects), 
use cases (the business rules), and interfaces (the adapters between the business logic and the outside world) and clients
(technical objects/interfaces). Each layer should only depend on the layers beneath it.
- Apply dependency inversion

4. How can you make dependencies between modules more explicit?
- Use dependency injection: This would make it clear what dependencies each module has, as they would be passed in 
as arguments rather than being accessed directly.
- Use a module system that makes dependencies explicit. For example use proper top level imports, import modules 
as modules without importing the logic beneath the module. Never use relative imports beyond the current module.

5*. Concrete suggestions:
- A good DI framework for python: https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html. With this
we could organize the modules nicely, apply the most popular design pattern (factories, singletons, etc). If we stick 
with the monorepo, for each new Microservice we could build up a DAG and create IoC container if need

*Please do not spend more than 2-3 hours on this task.*

Stretch goals:
* Fork the repository and start refactoring
* Write meaningful tests
* Replace the SQL repository with an in-memory implementation

## References
* [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Clean Architecture in Python](https://www.youtube.com/watch?v=C7MRkqP5NRI)
* [A detailed summary of the Clean Architecture book by Uncle Bob](https://github.com/serodriguez68/clean-architecture)

## How to use this project

If you have not installed poetry you find instructions [here](https://python-poetry.org/).

1. `docker-compose up` - runs a postgres instance for development
2. `poetry install` - install all dependency for the project
3. `poetry run schema` - creates the database schema in the postgres instance
4. `poetry run start` - runs the development server at port 8000
5. `/postman` - contains an postman environment and collections to test the project

## Other commands

* `poetry run graph` - draws a dependency graph for the project
* `poetry run tests` - runs the test suite
* `poetry run lint` - runs flake8 with a few plugins
* `poetry run format` - uses isort and black for autoformating
* `poetry run typing` - uses mypy to typecheck the project

## Specification - A simple shop

* As a customer, I want to be able to create an account so that I can save my personal information.
* As a customer, I want to be able to view detailed product information, such as price, quantity available, and product description, so that I can make an informed purchase decision.
* As a customer, I want to be able to add products to my cart so that I can easily keep track of my intended purchases.
* As an inventory manager, I want to be able to add new products to the system so that they are available for customers to purchase.