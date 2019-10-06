# PythonGoogleTTSClient
By using googles text to speech api, this client allows the user to input a text with the given parameters and receive an audio output.

## Links
- Supported Voices: https://cloud.google.com/text-to-speech/docs/voices
- Reference to Client Library: https://cloud.google.com/text-to-speech/docs/reference/libraries

## Prerequisite
- Python 3.6.7
- Credentials Json File

## Credentials Json File
In order to be able to use this client application you have to generate yourself a credentials json file with the google console, there fore you need to follow the steps in the reference to the client library link under "Setting up authentication"
Place the json file in your application folder with the given name: "credentials.json"

## Installation
- Create a new virtual environment
- Activate the environment
- Install python package of googles tts api: "pip install --upgrade google-cloud-texttospeech"
- Validate the installation: "pip list"

## Usage
- Open cmd in the project folder
- Activate the created virtual environment
- Enter "python main.py"
- Choose one of the following options

## Options
1. List the avaible voices: Prints all the voices avaible in the Google Text to Speech API
2. Convert the given text: Input the file name, your text, the language code and the voice name to receive an audio output
3. Convert the given json file: Input path to json file, with all the required informations to generate audio ouputs
4. Escape: Stops the program execution
