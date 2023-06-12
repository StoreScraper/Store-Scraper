# Set the base image to Ubuntu
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=nonintercative


# Install python
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv\
    git \
    uvicorn

RUN git clone https://github.com/StoreScraper/Store-Scraper.git

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /code/app

EXPOSE 8000

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]