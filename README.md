# 7053CEM-fts Course Finder

## Prerequisites
* Docker
* docker-compose v3
* node > v12
* python 3

## Running the App
### Building Assets:

 ```shell script
sh fts-build.sh
```

### Starting the server
Start the server with docker-compose
 ```shell script
 docker-compose up -d
 ```
Check all is OK by navigating to http://localhost:5000

### Generate Test Data:

 ```shell script
sh fts-generate-data.sh
```


### Stopping the server
 ```shell script
 docker-compose stop
 ```

### Clean up
 ```shell script
 docker-compose down
 ```

## Testing
Run tests on both server and web-app with:
 ```shell script
sh fts-test.sh
```