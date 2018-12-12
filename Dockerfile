FROM python:3.6.6-alpine3.7 AS builder

WORKDIR /usr/src/app/

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    openjpeg-dev \
    openssl-dev \
    zlib-dev

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.6.6-alpine3.7 AS runner

ENV PATH=$PATH:/root/.local/bin

WORKDIR /usr/src/app/

RUN apk add --no-cache --virtual .run-deps \
    openjpeg \
    openssl

EXPOSE 8000/tcp

COPY --from=builder /root/.local/ /root/.local/
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000