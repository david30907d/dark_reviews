# Dark Reviews ![Docker Image CI](https://github.com/david30907d/dark_reviews/workflows/Docker%20Image%20CI/badge.svg)

## Install

1. Python dependencies:
    1. `virtualenv venv; . venv/bin/activate`
    2. `pip install poetry`
    3. `poetry install`
2. Npm dependencies, for linter, formatter and commit linter (optional):
    1. `brew install npm`
    2. `npm ci`

## Run

```bash
scrapy crawl jkforum -o output.json
```

## Test

please check [.github/workflows/dockerimage.yml](.github/workflows/dockerimage.yml)