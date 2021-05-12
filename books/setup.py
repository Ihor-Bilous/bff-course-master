import setuptools

dev_dependencies = [
    "mypy",
    "flake8",
    "black",
    "isort",
    "pip-tools",
    "uvicorn",
]


requirements = open("requirements.txt").readlines()


setuptools.setup(
    name="authors",
    description="Books Service.",
    version="0.1",
    packages=["app", "app.api", "app.core", "app.db"],
    install_requires=requirements,
    extras_require={"dev": dev_dependencies},
)
