import json
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

from google.cloud import texttospeech
from google.cloud.texttospeech import enums

def list_voices():
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print('Name: {}'.format(voice.name))

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print('Supported language: {}'.format(language_code))

        ssml_gender = enums.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print('SSML Voice Gender: {}'.format(ssml_gender.name))

        # Display the natural sample rate hertz for this voice. Example: 24000
        print('Natural Sample Rate Hertz: {}\n'.format(
            voice.natural_sample_rate_hertz))

def convert_text(file_name, string_text, lang_code, voice_name):

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text = string_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")new
    # voice = texttospeech.types.VoiceSelectionParams(
    #          name = voice_name,
    #          language_code='en-US',
    #          ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang_code,
        name = voice_name)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open(file_name, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print("Audio content written to file " + file_name)

def convert_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)

        for t in data['texts']:
            print('Name: ' + t['name'])
            print('Text: ' + t['text'])
            print('Code: ' + t['code'])
            print('Voice: ' + t['voice'])
            convert_text(t['name'], t['text'], t['code'], t['voice'])
            print('')

if __name__ == "__main__":

    loop = True

    print("Welcome to the Python Client of Google Text to Speech API")

    while loop:

        print("Choose your options:")
        print("1. List the avaible voices")
        print("2. Convert the given text with the given voice to mp3")
        print("3. Convert the given json file")
        print("4. Escape")

        option_choice = input("Your choice? 1|2|3|4\n")

        if(option_choice == "1"):
            try:    
                list_voices()
            except:
                print("Could not list voices!")

        if(option_choice == "2"):
            name = input("File Name?\n")
            text = input("Text?\n")
            code = input("Language Code?\n")
            voice = input("Voice Name?\n")

            try:
                convert_text(name, text, code, voice)
            except:
                print("Could not convert text!")

        if(option_choice == "3"):
            path = input("File Path?\n")
            
            try:
                convert_file(path)
            except:
                print("Could not convert file!")
        
        if(option_choice == "4"):
            loop = False