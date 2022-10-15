from google.cloud import translate
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'  


def translate_text(text , project_id="favorable-order-365522"):

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

        f = open("english-out.txt", "a")
        f.write(translation.translated_text)
        f.close()


with open('text.txt', 'r') as file:

    line = file.readline()
    cnt = 1
    while line:
        line = file.readline()
        translate_text(line)
        cnt += 1
