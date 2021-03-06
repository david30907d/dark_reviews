FROM python:3.7.6-alpine3.11

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'
COPY . /app
WORKDIR /app
RUN apk --update --no-cache add gcc g++ git nginx postgresql-dev libffi-dev libxml2-dev libxslt-dev \
    # 1. if you don't need postgres, remember to remove postgresql-dev and sqlalchemy
    # 2. libffi-dev is required by poetry
    # 3. libxml2-dev libxslt-dev are for BeautifulSoup4
    && pip install --no-cache-dir poetry \
    && poetry install --no-interaction --no-ansi --no-dev \
    # Cleaning poetry installation's cache for production:
    && rm -rf "$POETRY_CACHE_DIR" \
    && apk del gcc git \
    && pip uninstall -yq poetry \
    && rm -rf /tmp/* /var/cache/apk/*

CMD ["server"]