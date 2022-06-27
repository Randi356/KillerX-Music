# UPGRADE DOCKER
FROM rendyprojects/killerx-music:latest
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b dev https://github.com/Randi356/KillerX-Music/
COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN pip install --ignore-installed PyYAML 
RUN pip3 install -r https://raw.githubusercontent.com/Randi356/KillerX-Music/dev/requirements.txt
CMD [ "bash", "start" ]
