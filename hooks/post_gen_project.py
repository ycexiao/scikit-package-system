def main():
    """Execute when user runs cookiecutter."""

    print(
        f"""
    Congratulations! A new Python project is created!
    Enter the directory with `cd {{cookiecutter.project_name}}`.
    Run `pip install -e .` to install the package in editable mode.
    To ensure the package is installed correctly, run `pytest`

    For more info, please refer to the official documentation on Level 4 of sharing.
    """
    )


if __name__ == "__main__":
    main()
