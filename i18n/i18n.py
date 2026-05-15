import json
import locale
import os

# Supported languages: en_US (English), ar_SA (Arabic)
SUPPORTED_LANGUAGES = ["en_US", "ar_SA"]


def load_language_list(language):
    with open(f"./i18n/locale/{language}.json", "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            # Check environment variable first (e.g. set VIRALS_LANGUAGE=ar_SA)
            env_lang = os.environ.get("VIRALS_LANGUAGE", "").strip()
            if env_lang and os.path.exists(f"./i18n/locale/{env_lang}.json"):
                language = env_lang
            else:
                language = locale.getdefaultlocale()[0]
        if not language or not os.path.exists(f"./i18n/locale/{language}.json"):
            language = "en_US"
        self.language = language
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
