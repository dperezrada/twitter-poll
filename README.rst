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

    easy_install webtest bottle nose lxml
    cd /tmp
    git clone git@github.com:rlisagor/freshen
    cd freshen
    python setup.py install

Tests
=====
::

    nosetests --with-freshen --list-undefined -v
