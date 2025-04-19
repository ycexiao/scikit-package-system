|title|_
=========

.. |title| replace:: {{ cookiecutter.conda_pypi_package_dist_name }}
.. _title: https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.github_repo_name }}

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.conda_pypi_package_dist_name }}
        :target: https://pypi.org/project/{{ cookiecutter.conda_pypi_package_dist_name }}/


Installation
------------

Once a new project folder, cd into the package directory ::

        cd {{ cookiecutter.project_name }}

Then create a new conda environment and activate it ::

        conda create -n {{ cookiecutter.conda_pypi_package_dist_name }}_env {{ cookiecutter.conda_pypi_package_dist_name }}
        conda activate {{ cookiecutter.conda_pypi_package_dist_name }}_env

Install the package in editable mode ::
        pip install -e .

Then ensure that the package is installed correctly by running the tests ::
        pytest
