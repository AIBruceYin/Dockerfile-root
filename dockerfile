FROM python:3.8-slim-buster
LABEL description="Root user should be allowed to create directories in root directory"
WORKDIR /app
ENV ENV1=Val1 \
    ENV2=Val2
RUN mkdir temp; \
    apt-get update; \
    pip3 install loguru;
COPY . .
ENTRYPOINT ["python3", "container_file.py"]
