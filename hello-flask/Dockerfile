FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev-compat \
    python3-dev \
    pkg-config

WORKDIR /app
COPY . .
RUN pip install flask mysqlclient
EXPOSE 5002
CMD ["python", "app.py"]