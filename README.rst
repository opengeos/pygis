=====
pygis
=====

.. image:: https://mybinder.org/badge_logo.svg 
        :target: https://mybinder.org/v2/gh/giswqs/pygis/master

.. image:: https://img.shields.io/pypi/v/pygis.svg
        :target: https://pypi.python.org/pypi/pygis

.. image:: https://img.shields.io/travis/giswqs/pygis.svg
        :target: https://travis-ci.org/giswqs/pygis

.. image:: https://readthedocs.org/projects/pygis/badge/?version=latest
        :target: https://py-gis.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
        :target: https://opensource.org/licenses/MIT


Author: Qiusheng Wu (https://wetlands.io | wqs@binghamton.edu)


**pygis** is a collection of Python snippets for geospatial analysis.

* GitHub repo: https://github.com/giswqs/pygis
* Documentation: https://py-pygis.readthedocs.io.
* PyPI: https://pypi.org/project/pygis/
* Binder: https://gishub.org/pygis-cloud
* Free software: `MIT license`_

.. _`MIT license`: https://en.wikipedia.org/wiki/MIT_License


Features
--------

* Download files from direct URLs or shared files from Google Drive
* Read and write zip files; extract files from zip files

Examples
--------
.. code:: python

  import pygis
  url = "https://github.com/giswqs/lidar/raw/master/examples/lidar-dem.zip"
  pygis.download_from_url(url, file_name='data.zip', unzip=False)
  gfile_url = 'https://drive.google.com/file/d/1c6v-ep5-klb2J32Nuu1rSyqAc8kEtmdh'
  pygis.download_from_gdrive(gfile_url, 'dem.zip')  
  

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
