from google.cloud import translate
import os


def translate_text(text, project_id="favorable-order-365522"):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key-translate.json'
    # print(len(text))
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "ta",
            "target_language_code": "en-US",
        }
    )

    for translation in response.translations:

        f = open("temp/english-out.txt", "a")

        lines = translation.translated_text.split("\n")

        string_without_empty_lines = ""

        for line in lines:
            string_without_empty_lines += line + "\n"

        f.write(string_without_empty_lines)
        f.close()

def translate_locale_out():
    tamil_text = ""

    with open('temp/locale-out.txt', 'r') as file:

        line = file.readline()
        cnt = 1
        while line:
            line = file.readline()
            tamil_text = tamil_text + line
            cnt += 1


    l = len(tamil_text)

    while l > 0:
        if l > 30000:
            translate_text(tamil_text[:30000])
            tamil_text = tamil_text[30000:]
            l = len(tamil_text)
        else:
            translate_text(tamil_text)
            l = 0
