==============
bioinfo_course
==============


.. image:: https://img.shields.io/pypi/v/bioinfo_course.svg
        :target: https://pypi.python.org/pypi/bioinfo_course

.. image:: https://img.shields.io/travis/YuchenXiangEMBL/bioinfo_course.svg
        :target: https://travis-ci.org/YuchenXiangEMBL/bioinfo_course

.. image:: https://codecov.io/gh/YuchenXiangEMBL/bioinfo_course/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/YuchenXiangEMBL/bioinfo_course

.. image:: https://readthedocs.org/projects/bioinfo-course/badge/?version=latest
        :target: https://bioinfo-course.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



-------
Test on EBI course
-------

This is a simple test to let you familirize the use of *cookiecutter* to establish a project, using *poetry* for creating virtual environment and add it to your project **pyproject.toml** file and link to the github repo
Apart from this, this is also a practice for the sphinx text to write the 

Here follows some code to document the command to establish this: 

1. Use cookiecutter to establish a project, specify the MIT licence

``cookiecutter https://github.com/pyOpenSci/cookiecutter-pyopensci.git``

`The reference link for more info on this cookiecutter template <https://cookiecutter-pyopensci.readthedocs.io/en/latest/tutorial.html>`

2. As the proejct has been created already, so then we init the *poetry*, where the pyproject.toml file will be initiated

``poetry init``

3. To add packages to your virtual environment, for instance, the package dependencies can be checked in the poetry.lock file

``poetry add scanpy``

``poetry env info``

``poetry shell``

4. As the cookiecutter has already created a **requirement.txt** file, we can also add it to the poetry init

``poetry add "cat requirements_dev.txt"``

`The reference link can be found on <https://realpython.com/dependency-management-python-poetry/>`_

5. To establish link from the local repository to the Github repo, we need to establish the SSH key link first, for this part, check ChatGPT, it offers good tutorial, afterwards, we establish link to the github repo

``cd bioinfo_course``

``git init .``

``git add .``

``git commit -m "Initial skeleton."``

``git remote add origin git@github.com:YuchenXiangEMBL/bioinfo_course.git``

``git push -u origin main``

6. Now we can check the Github repo for the package

`The link to github <https://github.com/YuchenXiangEMBL/bioinfo_course>`_

7. To update the Github repository with the modified changes

``git add .``

``git commit -m "update 1"``

``git push origin main``

8. `For a better reference to the RestructuredText format <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#external-links>`_

`This link might also help <https://sphinx-tutorial.readthedocs.io/step-1/>`_

9. I am still learning in this process and will keep updating the new knowledge ...






* Free software: MIT license
* Documentation: https://bioinfo-course.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `pyOpenSci/cookiecutter-pyopensci`_ project template, based off `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`pyOpenSci/cookiecutter-pyopensci`: https://github.com/pyOpenSci/cookiecutter-pyopensci
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
