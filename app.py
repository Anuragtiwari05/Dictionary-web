from flask import Flask, render_template, request  ## Import Flask modules: Flask for app, render_template to render HTML, request to get form data
import requests  ## Import requests to make HTTP calls to the dictionary API
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate ##for hindi and urdu 

app = Flask(__name__)  ## Create a Flask app instance

@app.route("/", methods=["GET", "POST"])  ## Define the main route "/" and allow GET (page load) and POST (form submission)
def home():
    ## Initialize variables to pass to the HTML template
    word = ""             ## The word entered by the user
    meaning = ""          ## Meaning of the word
    example = ""          ## Example sentence (if available)
   

    if request.method == "POST":  ## Check if user submitted the form
        word = request.form.get("word").lower()  ## Get the word from the form and convert to lowercase
        lang = request.form.get("lang")  ## Get the selected language from the form

       # 🔹 Transliteration step
        if lang == "hindi":
            script_word = transliterate(word, sanscript.ITRANS, sanscript.DEVANAGARI)
        elif lang == "urdu":
            script_word = transliterate(word, sanscript.ITRANS, sanscript.URDU)
        else:
            script_word = word   # English stays same

        # 🔹 API only supports English
        if lang == "english":
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

        ## Call the API
        response = requests.get(url)

        if response.status_code == 200:  ## If the API returns success
            data = response.json()[0]    ## Get the first item from the JSON response

            ## Extract meanings
            meanings = data.get("meanings", [])  ## Get the 'meanings' list
            if meanings:                        ## If meanings exist
                definitions = meanings[0].get("definitions", [])  ## Get first part of definitions
                if definitions:                                 ## If definitions exist
                    meaning = definitions[0].get("definition", "No definition found")  ## Get the definition
                    example = definitions[0].get("example", "")  ## Get example if available

            
           

        else:  ## If the word is not found
            meaning = "Word not found!"
    else:
            # For Hindi/Urdu → just show converted script (no API support yet)
            meaning = f"Converted word: {script_word} (dictionary lookup not available yet)"

    ## Render the HTML template and pass variables
    return render_template(
        "index.html",
        word=word,
        meaning=meaning,
        example=example,
        script_word=script_word
    )

## Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  ## Run in debug mode so changes auto-reload and errors are visible
