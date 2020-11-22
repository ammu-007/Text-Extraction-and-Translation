from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from pydub import AudioSegment
from pydub.playback import play
import config

authenticator = IAMAuthenticator(config.speech_auth)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(config.speech_api)

class Speech:
    """
    Member functions:

    text_to_speech():
    arguments => (text) string containing text to be converted.
    returns => None
    functionality => plays the translated audio.
    """
    def __init__(self, text):
        self.text = text

    def text_to_speech(self):
        with open('hello_world.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    self.text,
                    voice='en-US_AllisonV3Voice',
                    accept='audio/wav'        
                ).get_result().content)
        song = AudioSegment.from_wav("hello_world.wav")
        play(song)