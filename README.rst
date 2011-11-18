Authors
=======

* Luis Felipe Álvarez (@lfalvarez)
* Nicolás Dujovne (@ndujovne)
* Daniel Pérez (@dperezrada)
* Felipe Valverde (@fvalverd)

Requirements
============
* webtest
* freshen (from GitHub, most recent version)
* bottle
* nose
* lxml

To install
----------
::

    git clone git@github.com:dperezrada/twitter-poll.git
    cd twitter-poll
    python setup.py develop
    cd /tmp
    git clone git@github.com:rlisagor/freshen
    cd freshen
    python setup.py install

Tests
=====
::

    nosetests --with-freshen --list-undefined -v
