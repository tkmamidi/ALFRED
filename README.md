# ALFRED

ALFRED is a Python conversation project that uses the microphone to listen and repeat what it hears. It is built using Docker for easy setup and deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

### Installing

1. Clone the repository
```
git clone https://github.com/tkmamidi/ALFRED.git
```

2. Navigate to the project directory
```
cd ALFRED
```

3. Build the Docker image
```
docker build -t alfred .
```

4. Run the Docker container
```
docker run -it --name alfred alfred
```

## Running the tests

The tests are located in the `tests` directory. To run the tests, navigate to the project directory and run the following command:
```
python -m unittest discover tests
```

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Docker](https://www.docker.com/) - Used for containerization

## Authors

* **Tarun Mamidi** - *Initial work* - [tkmamidi](https://github.com/tkmamidi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
