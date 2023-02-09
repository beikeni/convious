===
API
===

Provider CRUD
-------------

List
""""

.. code-block::

	GET /api/v1/providers/

Response

.. code-block::

	[
		{
			"id" : 12,
			"currency": "eur",
			"email": "email@email.com",
			"language": "english",
			"name": "provider_1",
			"phone": "123456"
		},
	]

-----------------------------------

Create
""""""

.. code-block::

	POST /api/v1/providers/

:name: String
:email: String
:language: Language
:currency: Currency
:phone: String

Response

.. code-block::

	{
		"id" : 12,
		"currency": "usd",
		"email": "asdd@asddd.ddd",
		"language": "english",
		"name": "prov1",
		"phone": "123123"
	}

-----------------------------------

Update
""""""

.. code-block::

	PUT /api/v1/providers/<int:pk>/

:name: String
:email: String
:language: Language
:currency: Currency
:phone: String

Response

.. code-block::

	{
		"id": 3,
		"currency": "usd",
		"email": "asdd@asddd.ddd",
		"language": "english",
		"name": "prov1",
		"phone": "123123"
	}


-----------------------------------

Delete
""""""

.. code-block::

	DELETE /api/v1/providers/<int:pk>/

Response 204

-----------------------------------

Service Area CRUD
-------------

List
""""

.. code-block::

	GET /api/v1/serviceareas/


Response

.. code-block::

	[
		{
			"id": 25,
			"name": "test",
			"price": "123",
			"geojson": ...,
			"provider": Provider id
		},
		...
	]

-----------------------------------

Create
""""""

.. code-block::

	POST /api/v1/serviceareas/

:name: String
:price: String
:geojson: Geojson coordinates
:provider: Provider id

Response

.. code-block::

	{
		"id": 29,
		"geojson": {
			...
    		},
		"name": "test",
		"price": 999.0,
		"provider": 1
	}

-----------------------------------

Update
""""""

.. code-block::

	PUT /api/v1/serviceareas/<int:pk>

:name: String
:price: String
:geojson: Geojson coordinates
:provider: Provider id

Response

.. code-block::

	{
		"id": 88,
		"geojson": {
			...
			},
		"name": "test2",
		"price": 999.0,
		"provider": 1
	}

-----------------------------------

Delete
""""""

.. code-block::

	DELETE /api/v1/serviceareas/<int:pk>

Response 204

-----------------------------------

Get Polygons Endpoint
---------------------

.. code-block::

	POST /api/v1/get-polygons

:lat: Float
:long: Float

Response

.. code-block::

	[
		{
			"name": "Italy",
			"price": 18.440960484948576,
			"provider": {
				"currency": "eur",
				"email": "email@email.com",
				"language": "english",
				"name": "provider_1",
				"phone": "123456"
			}
		}
	]
