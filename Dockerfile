FROM python:latest
RUN apt-get -y update
RUN apt-get install -y libnss3
# From https://www.2daygeek.com/install-google-chrome-browser-on-linux/
RUN wget -y https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
WORKDIR /WorldOfGames
COPY *.py /WorldOfGames/
COPY requirements.txt /WorldOfGames/requirements.txt
COPY Scores.txt /WorldOfGames/Scores.txt
RUN pip3 install -r /WorldOfGames/requirements.txt
EXPOSE 5000
CMD ["python", "MainScores.py"]
