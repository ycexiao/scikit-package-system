# Scikit-Package-System

Here is the template for Level 4 of sharing code in `scikit-package`. Please visit the latest developments and the official documentation [here](https://github.com/Billingegroup/scikit-package).

Notes for future contributors:

The goal of Level 4 is to ensure the package is easily installable locally and to share the code with colleagues.

- The goal is to work on a private GitHub repository with CI passing.
- Users learn to use `pyproject.toml`.
- Users learn to use GitHub CI (no news check or Codecov).

Other notes from the very first PR in [this link](https://github.com/Billingegroup/scikit-package-system/pull/2):

- We assume that the latest Python version supported by `skpkg` is used in Level 4. If the user needs to specify the Python version, we encourage them to use Level 5.
- We have decided not to support the namespace package structure in Level 4.
- We would like users to configure `test-on-pr` CI without Codecov. Ideally, Level 4 should focus on hosting the project on GitHub.
- We want the `README.rst` to contain quick installation instructions.
- We would like to have `LICENSE.rst` to encourage the good habit of taking care of this legal file.
- We do not provide documentation since users are focused on writing the actual code.
- We do not provide complicated examples for tests and docstrings in the current `calculator.py` and `test_calculator.py` demo code.
- We do not provide `AUTHORS.rst`, `CODE_OF_CONDUCT.rst`, `MANIFEST.rst`, or `CHANGELOG.rst`, which are provided in Level 5.

Are there any things that we need to maintain when we have new updates?

- We currently use `np.dot` in `src/calculator.py`. We doubt this API will change anytime soon.
- We don't need to worry about the latest Python version support since when users create a new conda environment, it will create the highest Python version compatible with `scikit-package`.
