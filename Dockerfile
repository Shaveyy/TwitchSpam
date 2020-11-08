# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /usr/src/app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

COPY . .
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get install -y tor
# command to run on container start
CMD [ "python", "./main.py" ]
