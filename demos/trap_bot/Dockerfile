

# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /trap_bot

COPY requirements.txt /trap_bot
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /trap_bot


ENTRYPOINT ["python3"]
CMD ["app.py"]

