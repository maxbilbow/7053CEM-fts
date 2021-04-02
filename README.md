# 7053CEM-fts Course Finder

## Prerequisites
* Docker
* node > v12
* python 3

## Building Assets:

 ```shell script
sh fts-build.sh
```

## Starting the server
Start the server with docker-compose
 ```shell script
 docker-compose up -d
 ```
Check all is OK by navigating to http://localhost:5000

## Stopping the server
 ```shell script
 docker-compose stop
 ```

## Clean up
 ```shell script
 docker-compose down
 ```