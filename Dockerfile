FROM python:3

ADD twitter_stream_to_csv.py /

RUN pip install tweepy

CMD ["python", "./twitter_stream_to_csv.py"]