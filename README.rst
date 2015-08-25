############
News Scraper
############

A web scraping module for Norwegian news sites


Installation
------------


Using pip


.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools

    $ pip install git+git://github.com/matmonsen/news-scraper


Pip via git

.. code-block:: bash

    $ pip install git+ssh://git@github.com/matmonsen/news-scraper.git





Usage
-----

------------------
Scrape a newspaper
------------------

    Scrape headlines from `aftenposten`_ frontpage

    .. code-block:: bash

        $ news_scraper = Scraper('Aftenposten')
        # number of articles from `aftenposten`_
        $ news_scraper.scrape(2)

        $ print(news_scraper.articles[0])
            NewsPaper:
                Name: Aftenposten

                Url: http://www.aftenposten.no

                Tag Class Name: df-article-content

                Subscription Url:

                Title Tag: h3

            Article:
                Title: Krever opprydning i Oslos kamerajungel

                Summary:

                Link: http://www.aftenposten.no/nyheter/iriks/Krever-opprydding-i-Oslos-kamerajungel-8136177.html

                Image: http://ap.mnocdn.no/external/drfront/images/1e7356c603d713a8f32c1fcdc70d706d.jpg


----------------------
Generate documentation
----------------------

Using make
    .. code-block:: bash

            # Navigate to news-scraper/docs
            $ make html

-------
Licence
-------

Please see `LICENSE`_

.. _aftenposten: http://www.aftenposten.no
.. _LICENSE: https://github.com/Matmonsen/news-scraper/blob/master/LICENSE.rst
.. _requirements: https://github.com/Matmonsen/news-scraper/blob/master/requirements.txt
.. _Requests: http://python-requests.org
.. _pip: http://www.pip-installer.org/en/latest/index.html



