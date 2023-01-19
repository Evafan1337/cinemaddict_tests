#FROM python:3.10.6
FROM ubuntu:18.04

RUN  apt-get update \
  && apt-get install -y wget \
     gnupg2

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install selenium==3.141.0
RUN pip3 install behave==1.2.6
RUN pip3 install allure-behave==2.12.0

RUN mkdir docker && cd ./docker && mkdir python && cd ./python \
    mkdir features \
    mkdir output_data \
    cd output_data \
    mkdir allure_reports \
    mkdir scroots
ADD index.py /docker/python

#hardcode getting of src code of tests
#ADD /home/user1/Github/cinemaddict_tests/features /docker/python/features
ADD features /docker/python/features
RUN ls /docker/python/features

WORKDIR /docker/python
CMD behave --no-capture -f allure_behave.formatter:AllureFormatter -o ./output_data/allure_reports
#CMD ["behave", "--no-capture"]
#CMD ["behave", "--no-capture", "-f allure_behave.formatter:AllureFormatter", "-o ./output_data/allure_reports"]
#CMD ["python3", "/docker/python/index.py"]
#CMD ["python3", "/opt/venv/bin/python/index.py"]
#CMD [ "python", "/workspace/index_test.py" ]
#CMD ["behave"]