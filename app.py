from flask import Flask, render_template, request
import requests
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

# 🔹 Function to lookup English word using dictionary API
def lookup_english(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()[0]
            meanings = data.get("meanings", [])
            if meanings:
                definitions = meanings[0].get("definitions", [])
                if definitions:
                    meaning = definitions[0].get("definition", "No definition found")
                    example = definitions[0].get("example", "")
                    return meaning, example
        return "Word not found!", ""
    except Exception as e:
        return f"Error occurred: {str(e)}", ""

# 🔹 Function to transliterate Hindi from Hinglish
def transliterate_hindi(word):
    try:
        return transliterate(word, sanscript.ITRANS, sanscript.DEVANAGARI)
    except Exception as e:
        return f"Error in transliteration: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def home():
    word = ""
    meaning = ""
    example = ""
    script_word = ""

    if request.method == "POST":
        word = request.form.get("word").lower()
        lang = request.form.get("lang")

        # 🔹 Hindi transliteration
        if lang == "hindi":
            script_word = transliterate_hindi(word)
            meaning = f"Converted word: {script_word} (dictionary lookup not available yet)"

        # 🔹 English dictionary lookup
        else:
            script_word = word
            meaning, example = lookup_english(word)

    # Render template with all variables
    return render_template(
        "index.html",
        word=word,
        meaning=meaning,
        example=example,
        script_word=script_word
    )

if __name__ == "__main__":
    print("Starting Flask Dictionary App...")
    app.run(debug=True)
