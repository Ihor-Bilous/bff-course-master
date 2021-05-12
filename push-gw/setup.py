import setuptools

dev_dependencies = [
    "mypy",
    "flake8",
    "black",
    "isort",
    "pip-tools",
    "uvicorn[standard]",
]


requirements = open("requirements.txt").readlines()


setuptools.setup(
    name="push-service",
    description="Push notifications api service.",
    version="0.1",
    packages=["app", "app.api", "app.core"],
    install_requires=requirements,
    extras_require={"dev": dev_dependencies},
)
