import os

def load_text_files(folder_path):
    """/text/"""
    text_contents = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as file:
                text_contents.append(file.read())
    return text_contents

def search_disease_treatment(query, text_contents):
    """Search for disease treatment information."""
    results = []
    for text in text_contents:
        if query in text:
            results.append(text)
    return results
def search_treatment(query,text_contents):
    result=''
    for text in text_contents:
        if query in text:
            result=result+text
    return result

def disease_treatment(query):
    folder_path='search_disease/text'
    text_contents = load_text_files(folder_path)
    search_results = search_disease_treatment(query, text_contents)
    return search_results





