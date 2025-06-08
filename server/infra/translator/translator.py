from deep_translator import GoogleTranslator, MyMemoryTranslator


def get_supported_language_google(language: str):
    languages = {
        'english': 'en',
        'french': 'fr',
        'spanish': 'es',
        'german': 'de',
        'portuguese': 'pt',
    }

    return languages.get(language)


def translate_google(text: str, target_language: str):
    translation = GoogleTranslator(source="auto", target=target_language).translate(text)
    return translation


def translate_user_input_google(text: str, target_language: str):
    try:
        target_language_symbol = get_supported_language_google(target_language)
        translation = translate_google(text, target_language_symbol)
        print(f"Tradução: {translation}")
    except Exception as e:
        print(f"Erro na tradução: {e}")


def get_supported_language_my_memory(language: str):
    languages = {
        'english': 'en-US',
        'french': 'fr-FR',
        'spanish': 'es-ES',
        'german': 'de-DE',
        'portuguese': 'pt-BR',
    }

    return languages.get(language)


def translate_my_memory(text: str, target_language: str):
    translation = MyMemoryTranslator(source="pt-BR", target=target_language).translate(text)
    return translation


def translate_user_input_my_memory(text: str, target_language: str):
    try:
        target_language_symbol = get_supported_language_my_memory(target_language)
        translation = translate_my_memory(text, target_language_symbol)
        print(f"Tradução: {translation}")
    except Exception as e:
        print(f"Erro na tradução: {e}")


def translator_chatbot():
    print("Olá! Sou um chatbot de tradução. Digite \"sair\" para encerrar.")

    while True:
        text = input("\nDigite o texto para traduzir: ")
        if text.lower() == "sair":
            print("Até logo!")
            break

        target_language = input(
            'Para qual idioma você quer traduzir? (idiomas suportados: english, french, german, portuguese, spanish): ')

        translator_to_use = input('Qual tradutor deseja usar? (tradutores disponíveis: Google, MyMemory) ')

        if translator_to_use.lower() == "google":
            translate_user_input_google(text, target_language)
        elif translator_to_use.lower() == "mymemory":
            translate_user_input_my_memory(text, target_language)
        else:
            print(f"Um tradutor inválido foi escolhido")


if __name__ == "__main__":
    translator_chatbot()
