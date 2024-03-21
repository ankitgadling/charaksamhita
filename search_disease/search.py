import os
from pathlib import Path
from googletrans import Translator


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def categorize_paragraphs(text, disease_word):
    categorized_paragraphs = []

    # Tokenize text into paragraphs
    paragraphs = text.split('\n\n')

    for paragraph in paragraphs:
        if disease_word in paragraph:
            categorized_paragraphs.append(paragraph)

    return categorized_paragraphs

def categorize_paragraphs_folder(input_folder,disease_word):
    combined_text = []

    files = os.listdir(input_folder)
    for file_name in files:
        if file_name.endswith('.txt'):  # Assuming text files
            input_file_path = os.path.join(input_folder, file_name)

            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                text = input_file.read()
                paragraphs_containing_disease = categorize_paragraphs(text, disease_word)

                if paragraphs_containing_disease:
                    # combined_text += '\n\n'.join(paragraphs_containing_disease) + '\n\n'
                    combined_text.append(paragraphs_containing_disease[0])

    return combined_text


def disease_treatment(query):
    folder_path = os.path.join(BASE_DIR, 'media', 'text')
    search_results=categorize_paragraphs_folder(folder_path,query)
    return search_results



def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text





