import json
import re
import sys
sys.path.append('Dictionaries/')
def clarify_response(response):
    with open('Dictionaries/words_dictionary.json', 'r') as f:
        text = json.load(f)
    with open('Dictionaries/text_numbers.txt', 'r') as f:
        words_to_numbs = f.read().split('\n')

    response = response.lower()
    split_phrases = ''
    count = 0

    remove_number = ''
    replace_number = ''
    for i in range(len(words_to_numbs)):
        if words_to_numbs[i] in response and len(words_to_numbs[i]) > 0:
            remove_number = words_to_numbs[i]
            replace_number = str(i)

    response = response.replace(remove_number, replace_number)

    for word in text['poor_words']:
        if word in response:
            response = response.replace(word, ' ')

    response = ' '.join(response.split())

    for phrase in text['threading']:
        if phrase in response:
            split_phrases += phrase + '|'
            count += 1
    if count > 0:
        split_phrases = split_phrases[:-1]
        return re.split(split_phrases, response)
    else:
        return response.split("*******")

        
