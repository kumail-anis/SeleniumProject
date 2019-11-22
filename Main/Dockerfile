FROM selenium/standalone-chrome
WORKDIR /usr/src/app
COPY requirements.txt .
RUN sudo apt-get update
RUN sudo apt-get install google-chrome-stable -y
RUN sudo apt-get install python3.7 -y
RUN sudo apt-get install python3-pip -y
RUN sudo apt-get install python3.7-venv -y
RUN sudo -H pip3 install -U selenium

RUN sudo python3.7 -m venv /usr/bin/virtual
ENV PATH="/usr/bin/virtual:$PATH"

#RUN sudo /usr/bin/virtual/bin/pip install --no-cache-dir -r requirements.txt

COPY . . 
#ENV PATH=/drivers:$PATH
CMD ["python3", "main.py"]