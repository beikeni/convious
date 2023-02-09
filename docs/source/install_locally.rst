==========
Install Locally
==========

1. `Clone repo <https://github.com/beikeni/convious.git>`_

2. Add .env file at root level

.. code-block::

	DEVELOPMENT=true
	POSTGRES_USER=postgres
	POSTGRES_PASSWORD=postgres
	POSTGRES_DB=postgres
	DJANGO_SECRET_KEY=851de20a-1ab1-4107-9a09-acc77ed068e1

3. Startup Docker Compose

.. code-block::

	docker compose up --build

4. Migrate Database

.. code-block::

	docker exec web python manage.py migrate

5. Run seed script

.. code-block::

	docker exec web python manage.py seed


