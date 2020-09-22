# MyLyrics
This repository contains an API that provides the lyric of songs from two internet catalogue (AZlyrics, Elyrics)

## Prerequisites
To be able to build and test the application on your local environment, you need to have:

- Python 3.x (https://www.python.org/)

All the test has been done with Python 3.7 and macOS Catalina 10.15.6. We suggest to install the requirements in a python virtual environment to avoid packages errors (https://docs.python.org/3/library/venv.html).
We need the following packages:

- BeautifulSoup
- Requests

## Features
Print lyrics in Terminal.
Save lyrics in a .txt file if required.

## Installation
In order to install the required packages run the following command:
```sh
$ pip install -r requirements.txt
```      

## Usage
The application will run on cmd and it accept the following parameters:
```sh
$ python mylyrics.py -a "red hot chili peppers" -l "californication" -p "azlyrics" -s
```
```sh
$ python mylyrics.py [-h] [-a ARTIST] [-l LYRIC] [-p PROVIDER] [-s SAVE]

$ [-h] [--help] : help
$ [-a] [--artist] : artist (required)
$ [-l] [--lyric] : lyric (required)
$ [-p] [--provider] : provider [ azlyrics , elyrics ]
$ [-s] [--save] :  save a .txt file with the lyric
```
## Future implementation
Next will be implemented unit test to help in debug and trubleshooting and later integration test with the two source of information.
