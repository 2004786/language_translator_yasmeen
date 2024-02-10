import tkinter as tk
from googletrans import Translator

def translate_text():
    text = entry.get()
    translator = Translator()
    translated_text = translator.translate(text, dest=selected_language.get()).text
    output_label.config(text=translated_text)

# Create the main application window
root = tk.Tk()
root.title("Language Translator")

# Create the input label and entry
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create the language selection dropdow, n
languages = ["en","hi", "bn", "gu", "kn", "km", "gom", "ml", "mni-Mtei", "mr", "ne", "or", "pa", "sa", "sd", "ta","te", "ur", "bho", "sw", "mai", "doi"] 
# Example: 1) Assamese, (2) Bengali, (3) Gujarati, (4) Hindi, (5) Kannada, (6) Kashmiri, (7) Konkani, (8) Malayalam, (9) Manipuri, (10) Marathi, (11) Nepali, (12) Oriya, (13) Punjabi, (14) Sanskrit, (15) Sindhi, (16) Tamil, (17) Telugu, (18) Urdu (19) Bodo, (20) Santhali, (21) Maithili and (22) Dogri.

selected_language = tk.StringVar()
selected_language.set("en")  # Default language: English
language_dropdown = tk.OptionMenu(root, selected_language, *languages)
language_dropdown.pack()

# Create the translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Create the output label
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main event loop
root.mainloop()
