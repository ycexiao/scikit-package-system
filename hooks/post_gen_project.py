import shutil
from pathlib import Path

# All cookie-cutter hooks run on project root, but good to enforce
ROOT = Path.cwd()


def __gen_init__(module_name):
    """Generate __init__.py file for namespace module."""
    __init__ = f"""#!/usr/bin/env python
##############################################################################
#
# (c) {% now 'utc', '%Y' %} The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo_name }}/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
\"\"\"Blank namespace package for module {module_name}.\"\"\"


from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

# End of file
"""
    return __init__


def __gen_setuppy__():
    base_module_name = "{{ cookiecutter.project_name }}".split('.')[-1].strip()
    setuppy = """#!/usr/bin/env python

# Extensions script for {{ cookiecutter.project_name }}

import os
import re
import sys
import glob
from setuptools import setup
from setuptools import Extension

# Define extension arguments here
ext_kws = {
        'libraries' : [],
        'extra_compile_args' : [],
        'extra_link_args' : [],
        'include_dirs' : [],
}

""" + f"""def create_extensions():
    \"Initialize Extension objects for the setup function.\"
    ext = Extension('{{ cookiecutter.package_dir_name }}.{base_module_name}',
                    glob.glob('src/extensions/*.cpp'),
                    **ext_kws)
    return [ext]


# Extensions not included in pyproject.toml
setup_args = dict(
    ext_modules = [],
)


if __name__ == '__main__':
    setup_args['ext_modules'] = create_extensions()
    setup(**setup_args)

"""
    return setuppy


def add_supermodules(ROOT, name):
    """Add module packages for each leading period."""
    src_dir = ROOT / "src"
    c_dir = src_dir  # Current directory

    package_dir_name = "{{ cookiecutter.package_dir_name }}"
    cp_dir = c_dir / package_dir_name  # Current package directory

    # Get the necessary modules given the period spacings
    module_names = name.split(".")
    for i, module in enumerate(module_names):
        module_names[i] = module.strip().lower()

    # The last module is not a namespace module
    ns_module_names = module_names[:-1]

    # Create a subdirectory for each parsed module
    for ns_module_name in ns_module_names:
        # Create module directory and move files
        d_dir = c_dir / ns_module_name  # Destination directory
        try:
            d_dir.mkdir(parents=False, exist_ok=False)
        # Should never occur as the parent directory is tracked by c_dir
        except FileNotFoundError:
            print(f"Parent directory {c_dir} not found. This is likely an issue with cookiecutter.")
        # Should never occur from how we do our naming
        except FileExistsError:
            print(f"Duplicate directory names {d_dir} found. This is likely an issue with cookiecutter.")
        shutil.move(cp_dir, d_dir)

        # Make __init__.py file
        init_file = d_dir / "__init__.py"
        with open(init_file, "w") as ifile:
            ifile.write(__gen_init__(ns_module_name))
        c_dir = c_dir / ns_module_name
        cp_dir = c_dir / package_dir_name

    # Rename the final destination module
    cp_dir.rename(c_dir / module_names[-1])

def wrapper_setup():
    """Generate setup.py file for C extensions."""
    src_dir = ROOT / "src"
    ext_dir = src_dir / "extensions"
    try:
        ext_dir.mkdir(parents=False, exist_ok=False)
    # Should never occur as the parent directory is src
    except FileNotFoundError:
        print(f"Parent directory {src_dir} not found. This is likely an issue with cookiecutter.")
    # Can occur if user names the package extensions
    except FileExistsError:
        print(f"Duplicate directory names {src_dir} found. You cannot name your project 'extensions*'.")

    # Make __init__.py file
    setuppy_file = ROOT / "setup.py"
    with open(setuppy_file, "w") as spfile:
        spfile.write(__gen_setuppy__())



def main():
    """Execute when user runs cookiecutter."""
    if "." in "{{ cookiecutter.project_name }}":
        add_supermodules(ROOT, "{{ cookiecutter.package_dir_name }}")

    print(f"""
    Congratulations! A new Python project is created!
    Enter the directory with `cd {{cookiecutter.project_name}}`.
    Run `pip install -e .` to install the package in editable mode.
    To ensure the package is installed correctly, run `pytest`
    
    For more info, please refer to the official documentation on Level 4 of sharing.
    """)


if __name__ == '__main__':
    main()
