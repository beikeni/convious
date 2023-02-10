===
API
===

Restaurant CRUD
-------------

List
""""

.. code-block::

	GET /api/v1/restaurants/

Response 200

.. code-block::

	[
		{
			"id" : 12,
			"name": "restaurant name",
		},
	]

-----------------------------------

Create
""""""

.. code-block::

	POST /api/v1/restaurants/

:name: String

Response 201

.. code-block::

	{
		"id": 3,
		"name": "restaurant name",
	}

-----------------------------------

Update
""""""

.. code-block::

	PUT /api/v1/restaurants/<int:pk>/

:name: String

Response 200

.. code-block::

	{
		"id": 3,
		"name": "restaurant name",
	}


-----------------------------------

Delete
""""""

.. code-block::

	DELETE /api/v1/restaurants/<int:pk>/

Response 204

-----------------------------------

Vote Endpoint
-------------

Votes made through this endpoint are automatically assigned the current datetime. No past or future voting is allowed.

.. code-block::

	POST /api/v1/vote

:user: Int
:restaurant: Int

Response 201

.. code-block::

	{'Success': 'Vote successfully registered'}

Response 403

.. code-block::

    {'Error': 'Daily vote count exceeded for this user'}


Result Query Endpoint
---------------------

Both parameters are optional.
If no date is indicated the date of today is assumed.
If no period length is indicated it defaults to 0.
To return a list of past results indicate the start date and the length of the desired period.

:date: String
:period_length: Int

.. code-block::

	GET /api/v1/result/


Response 200

.. code-block::

	[
		{
			"date": "2023-02-09",
			"winner": {
				"score": 7.75,
				"restaurant_id": 8,
				"distinct_users": 6,
				"restaurant_name": "Restaurant 8"
			}
		}
	]

.. code-block::

	GET /api/v1/result/?date=2023-01-27


Response 200

.. code-block::

	[
		{
			"date": "2023-01-27",
			"winner": {
				"score": 7.75,
				"restaurant_id": 8,
				"distinct_users": 6,
				"restaurant_name": "Restaurant 8"
			}
		}
	]

.. code-block::

	GET /api/v1/result/?date=2023-01-01&period_length=3


Response 200

.. code-block::

	[
		{
			"date": "2023-01-03",
			"winner": {
				"score": 7.75,
				"restaurant_id": 8,
				"distinct_users": 6,
				"restaurant_name": "Restaurant 8"
			}
		},
		{
			"date": "2023-01-02",
			"winner": {
				"score": 7.25,
				"restaurant_id": 9,
				"distinct_users": 6,
				"restaurant_name": "Restaurant 9"
			}
		},
		{
			"date": "2023-01-01",
			"winner": {
				"score": 7.0,
				"restaurant_id": 7,
				"distinct_users": 6,
				"restaurant_name": "Restaurant 7"
			}
		}
	]

