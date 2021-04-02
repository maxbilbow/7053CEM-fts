FROM python:3.7-alpine
WORKDIR /fts-server
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./fts-server/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN sh generate-data.sh
EXPOSE 5000
COPY ./fts-server .
CMD ["flask", "run"]