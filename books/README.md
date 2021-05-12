# Books Service

## Description

This is Books API service that implements CRUD interface for working with Books objects.

## Installation

```bash
$ python -m venv .venv
$ make install
```

## Running the app

You can run the app either locally or via docker container

Locally:

```bash
vicorn main:app --reload
```

Docker:

```bash
make image
make container
```

Once app is running you can access it's documentation via http://127.0.0.1:8000/docs
