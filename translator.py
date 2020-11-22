import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import config

authenticator = IAMAuthenticator(config.translate_auth)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(config.lang_api)

class Translator:
    """
    Member functions:
    
    display():
    arguments => target_lang for the target language
    returns => translated text from english to target_lang

    language_list():
    arguments => None
    returns => list containing all supported languages
    """
    
    def __init__(self, text):
        self.text = text
    
    def display(self, target_lang):
        target_lang = target_lang.capitalize()
        languages = language_translator.list_languages().get_result()
        for k, v in languages.items():
            for i in v:
                if i['language_name'] == target_lang:
                    lang_code = i['language']
        model_id = 'en-'+str(lang_code)
        translation = language_translator.translate(
            text=self.text,
            model_id=model_id).get_result()
        return translation['translations'][0]['translation']

    def language_list(self):
        languages = language_translator.list_languages().get_result()
        lang_list = []
        for k, v in languages.items():
            for i in v:
                lang = i['language_name']
                lang_list.append(lang)
        return lang_list