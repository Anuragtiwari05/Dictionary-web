from flask import Flask, render_template, request
import requests
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize variables
    word = ""
    meaning = ""
    example = ""
    script_word = ""

    if request.method == "POST":
        word = request.form.get("word").lower()
        lang = request.form.get("lang")

        # Transliteration for Hindi/Urdu
        if lang == "hindi":
            script_word = transliterate(word, sanscript.ITRANS, sanscript.DEVANAGARI)
            meaning = f"Converted word: {script_word} (dictionary lookup not available yet)"
        elif lang == "urdu":
            script_word = transliterate(word, sanscript.ITRANS, sanscript.URDU)
            meaning = f"Converted word: {script_word} (dictionary lookup not available yet)"
        else:  # English
            script_word = word
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()[0]
                meanings = data.get("meanings", [])
                if meanings:
                    definitions = meanings[0].get("definitions", [])
                    if definitions:
                        meaning = definitions[0].get("definition", "No definition found")
                        example = definitions[0].get("example", "")
            else:
                meaning = "Word not found!"

    # Render template
    return render_template(
        "index.html",
        word=word,
        meaning=meaning,
        example=example,
        script_word=script_word
    )

if __name__ == "__main__":
    app.run(debug=True)
