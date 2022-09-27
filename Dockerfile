FROM python:3.10
RUN apt-get -y update
RUN apt-get install -y libnss3
WORKDIR /WorldOfGames
COPY *.py /WorldOfGames/
COPY requirements.txt /WorldOfGames/requirements.txt
COPY Scores.txt /WorldOfGames/Scores.txt
RUN pip3 install -r /WorldOfGames/requirements.txt
EXPOSE 5000
CMD ["python", "MainScores.py"]
