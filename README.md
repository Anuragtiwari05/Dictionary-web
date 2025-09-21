# Dictionary App

A simple web application built with **Python and Flask** that allows users to look up English word meanings and convert Hinglish words to **Hindi script**. Designed to be minimal, responsive, and easy to use.

---

## Features

- **English Dictionary Lookup** – Fetch word definitions and example sentences using the free [Dictionary API](https://dictionaryapi.dev/).  
- **Hindi Transliteration** – Convert Hinglish input into Devanagari script using the **Indic Transliteration library**.  
- **Responsive Design** – Works well on both desktop and mobile devices.  

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **APIs & Libraries:** Dictionary API, indic-transliteration  

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YourUsername/dictionary-app.git
cd dictionary-app
Install dependencies:

bash
Copy code
pip install flask requests indic-transliteration
Run the app:

bash
Copy code
python app.py
Open the app in your browser at:

cpp
Copy code
http://127.0.0.1:5000
Usage
Enter a word in the input box.

Select the language:

English → Get dictionary meaning

Hindi → Get Hinglish word converted to Devanagari

Click Search to see the result below.
