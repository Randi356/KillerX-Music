FROM rendyprojects/music:python3.10-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - sudo apt-get install -y nodejs
RUN python3 -m pip install --upgrade pip
RUN pip install --ignore-installed PyYAML 
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start

