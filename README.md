# Powerflex Challenge

This codebase is a basic REST API server, fulfilling the specs for the challenge proposed by the Powerflex recruiting team

## About

The proposed solution is a basic REST API server bootstraped using Django + Django REST Framework, on Python 3.10.10, and using poetry as a package and dependency manager. Everything is set up using docker-compose creating an enviroment with the server and a PostgreSQL database. The envorment provides a simple API for fictional Sprocket Factories.

## Installation

The container enviroment may be set up using the command:

    docker-compose up --build

This will build/download the Docker image dependencies and load the containers

## Usage

After installation the API may be accessed using the URL:

    http://localhost:8000/api/

A UI generated by Django REST Framework for API Exploration will show up if you load this from a web browser.

Here are some examples using the specifications from the provided document of the challenge:

### 1st Requirement

"An endpoint that returns all sprocket factory data"

For this requirement we can use the endpoint:

    curl --location 'http://localhost:8000/api/factory/'

And it will show us the data from all factories.

### 2nd Requirement

"An endpoint that returns factory data for a given factory id"

For this requirement we can use the endpoint:

    curl --location 'http://localhost:8000/api/factory/1'

Where "1" may be substituted by the desired factory id.

### 3rd Requirement

"An endpoint that returns sprockets for a given id"

For this requirement we can use the endpoint:

    curl --location 'http://localhost:8000/api/sprocket/factory/1'

Where "1" may be substituted by the desired factory id, this will show us all the sprockets for a given factory.

### 4th Requirement

"An endpoint that will create new sprocket"

For this requirement we can use the endpoint with the data using POST:

    curl --location 'http://localhost:8000/api/sprocket/' \
         --header 'Authorization: Token e91cbf3a845802314e7b0c2a41b783f6baf76cee' \
         --header 'Content-Type: application/json' \
         --data '{
             "factory": 2,
             "sprocket_type": 1
         }'

This operations creates a new sprocket, it required the factory id and sprocket type id, the sprocket types may be from 1 to 3, as per the seeded data

The response for this operation will be the newly created sprocket, which may be queried using the returned id on this service using a GET request:

    curl --location 'http://localhost:8000/api/sprocket/1'

Which will respond:

    {
        "id": 6,
        "sprocket_type": {
            "id": 1,
            "name": "A",
            "teeth": 5,
            "pitch_diameter": "5.0000",
            "outside_diameter": "6.0000",
            "pitch": 1
        },
        "created_at": "2023-08-28T02:54:14.247946Z",
        "factory": 2
    }

### 5th Requirement

"An endpoint that will update sprocket for a given id"

We can use a PUT operation on an existing sprocket:

    curl --location --request PUT 'http://localhost:8000/api/sprocket/' \
         --header 'Authorization: Token e91cbf3a845802314e7b0c2a41b783f6baf76cee' \
         --header 'Content-Type: application/json' \
         --data '{
             "factory": 2,
             "sprocket_type": 2
         }'

This example will edit the sprocket type:

    {
        "id": 1,
        "sprocket_type": {
            "id": 2,
            "name": "B",
            "teeth": 5,
            "pitch_diameter": "5.0000",
            "outside_diameter": "6.0000",
            "pitch": 1
        },
        "created_at": "2023-08-28T02:54:04.661407Z",
        "factory": 2
    }

## Credits

This codebase was made by Jaime Jaramillo using open source tools for the challenge proposed by the Powerflex interview team.