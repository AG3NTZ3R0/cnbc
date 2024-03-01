# Contributing to CNBC

## Welcome!

Thank you for considering contributing to CNBC. We're thrilled you're here and want to ensure that your contribution process is as smooth and enjoyable as possible. Whether you're fixing a bug, adding a feature, or improving documentation, every contribution is valuable.

## Getting Started

### Step 1: Set Up Your Environment

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
    ```bash
    git clone https://github.com/your-username/cnbc.git
    ```
3. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
4. **Install the development dependencies**:
    ```bash
    pip install -r requirements_dev.txt
    ```

### Step 2: Make Your Changes

1. Create a new branch for your changes:
    ```bash
    git checkout -b name-of-your-branch
    ```
2. Make your changes. Add tests if you're adding code, and make sure all tests pass.
3. Install the package locally and ensure the package functions properly.
4. Follow the coding standards and guidelines described in the next section.

## Coding Standards

- **Follow PEP 8** - This is the style guide for Python code. Use tools like `pylint` to check your code.
- **Write meaningful commit messages** - Describe what your changes do and why.
- **Include tests** - Your contributions should pass all tests. Add new tests for new features.

## Pull Request Process

1. **Push your changes** to your fork:
    ```bash
    git push origin name-of-your-branch
    ```
2. **Submit a pull request** through the GitHub website using your branch. Link the issue you're addressing, if applicable.
3. **Review and address comments** - Maintainers might suggest changes. Discuss, revise, and push the necessary commits to your branch.
4. Once approved, a project maintainer will merge your changes.

## Reporting Issues

Before creating a new issue, please check if it has already been reported. If you're reporting a bug, include detailed steps to reproduce, the expected outcome, and the actual outcome.

## Questions?

If you have any questions or need further guidance, feel free to open an issue for discussion.
