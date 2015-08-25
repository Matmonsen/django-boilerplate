##################
Django Boilerplate
##################

A boilerplate for Django`_


Installation
------------


Using git


.. code-block:: bash

    $ git clone https://github.com/Matmonsen/django-boilerplate




Usage
-----


Using the boilerplate

.. code-block:: bash

    # make a virtualenviroment
    $ mkdir venv
    $ cd venv
    $ which python3
    # returns path for python3
    $ virtualenv -p (insert python3 path) .

    # Activates a virtualenv
    $ source bin/activate

    # Navigate to cloned project

    # Install requirements
    $ pip install -r requirements.txt

    $ cd django_boilerplate

    # Initialize setup
    # -s is optional. It creates a superuser.
    # -g for initialize new git repo
    $ invoke setup -p "project_name" -a "app_name"

    # Run server
    # port defaults to 8000 -p for override
    $ invoke run

    # Ready to tango with Django
    # Open a web browser and goto http://127.0.0.1:8000/


-------
Licence
-------

Please see `LICENSE`_

.. _LICENSE: https://github.com/Matmonsen/django-boilerplate/blob/master/LICENSE.rst
.. _Django: https://www.djangoproject.com/



