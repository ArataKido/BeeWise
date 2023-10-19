# INSTRUCTIONS

## Getting Started

These instructions will help you get the project up and running on your local environment.

### Prerequisites

Make sure you have the following tools installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ArataKido/BeeWise
    ```

2. Navigate to the project directory:

    ```bash
    cd BeeWise
    ```

3. Create a `.env` file based on the provided `.env.example` file and update it with your configuration values.

4. Build and start the Docker containers using Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

    The `-d` flag runs the containers in the background. If you want to see container logs, omit the `-d` flag.

5. Once the containers are up and running, you can access your application at:

    - Backend: [http://localhost:8000](http://localhost:8000)
    - Database: The database container is not directly accessible but can be reached by other containers within the same Docker network.

## Stopping the Application

To stop and remove the Docker containers, run the following command:

```bash
docker-compose down
```

# TASKS
- [x] Using Docker (preferably - docker-compose), deploy the image with any opensource DBMS (preferably - PostgreSQL). Provide all necessary scripts and configuration (docker/compose) files to deploy the DBMS, as well as instructions for connecting to it. It is necessary to ensure data safety during container restart (i.e. - use volumes to store DBMS files on the host machine.


- [x] Implement a simple web service in Python3 (using FastAPI or Flask, for example) that performs the following functions:
The service should implement a REST API that accepts POST requests with content of the form {"questions_num": integer} ;


- - [x] After receiving the request, the service, in turn, requests from the public API (English-language quiz questions) https://jservice.io/api/random?count=1 the number of questions specified in the received request.
Further, the received answers should be stored in the database from item 1, and at least the following information should be stored (you can choose the name of columns and types of this column, you can also add your own columns): 1. Question ID, 2. Question text, 3. Answer text, 4. - Date the question was created. 
- - [x] In case there is the same question in the database, additional queries should be made to the public API with quizzes until a unique quiz question is retrieved.
- - [x] The answer to the query from 2.a must be the previous saved question for the quiz. If it is not present, it should be an empty object.

- [x] The repository with the assignment should provide instructions on how to build a docker image with the service from item 2., set it up and run it. And also an example of a request to POST API of the service.

- [x] It is desirable if you will use docker-compose, SqlAalchemy, use type annotation when performing the task.


# TODO
- [X] add .env var export to settings