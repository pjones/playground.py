# Python Playground

This repository is my playground while learning Python.

## Components

  * [SQLAlchemy](https://docs.sqlalchemy.org/en/13/index.html)

    - [Column Types](https://docs.sqlalchemy.org/en/13/core/type_basics.html#generic-types)

  * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

    Simple and small web application framework.

    - [Minimal Example](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)

    - [SQLAlchemy in  Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/)

## Other Reference Material

  * [How to Structure Python Programs](https://docs.python-guide.org/writing/structure/)

  * [The Python Import System](https://docs.python.org/3/reference/import.html)

  * [Python Typing Hints](https://docs.python.org/3/library/typing.html)

## Running this Tool

Start the flask server:

```
python -m playground
```

### Fetching All Users

```
$ curl http://127.0.0.1:5000/users | jq
```
```json
{
  "users": [
    {
      "addresses": [
        {
          "display_text": "Mandalore",
          "id": 1,
          "label": "Home",
          "user_id": 1
        },
        {
          "display_text": "Razor Crest",
          "id": 2,
          "label": "Work",
          "user_id": 1
        }
      ],
      "id": 1,
      "name": "The Mandalorian"
    },
    {
      "addresses": [
        {
          "display_text": "Alderaan",
          "id": 3,
          "label": "Home",
          "user_id": 2
        }
      ],
      "id": 2,
      "name": "Cara Dune"
    }
  ]
}
```

### Fetching the "Mando" User

```
$ curl http://127.0.0.1:5000/mando | jq
```
```json
{
  "addresses": [
    {
      "display_text": "Mandalore",
      "id": 1,
      "label": "Home",
      "user_id": 1
    },
    {
      "display_text": "Razor Crest",
      "id": 2,
      "label": "Work",
      "user_id": 1
    }
  ],
  "id": 1,
  "name": "The Mandalorian"
}
```
