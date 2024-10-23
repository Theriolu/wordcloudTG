import ijson
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import string
import random
import os
import sys
import PySimpleGUI as sg

gui_cpm = {'BACKGROUND': '#1E1E2E',
                'TEXT': '#C9CBFF',
                'INPUT': '#11111b',
                'TEXT_INPUT': '#89B4FA',
                'SCROLL': '#FAB387',
                'BUTTON': ('black', '#A6E3A1'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 0,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('CPM', gui_cpm)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('CPM')

layout = [  [sg.Text('Select result.json:', size=(16,1)), sg.Push(), sg.Input(key='tgres', readonly = True, disabled_readonly_background_color = '#11111b'), sg.FileBrowse()],
            [sg.Text('Custom stopwords (optional):', size=(27,1)), sg.Push(), sg.Input(key='cwords', readonly = True, disabled_readonly_background_color = '#11111b'), sg.FileBrowse()],
            [sg.Push(), sg.Text('Resolution:', size=(12,1)), sg.Input(default_text='1920', size=(5,5), key='res_w'), sg.Text('x'), sg.Input(default_text='1080', size=(5,5), key='res_h'), sg.Push()],
            [sg.Push(), sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Telegram Word Cloud Generator', layout)

nltk.download('stopwords')

# Catppuccin Mocha palette colors
catppuccin_mocha_colors = [
    "#89B4FA",  # Blue
    "#F5C2E7",  # Pink
    "#A6E3A1",  # Green
    "#F38BA8",  # Red
    "#FAB387",  # Peach
    "#C9CBFF",  # Lavender
]

# Custom color function using Catppuccin Mocha color palette
def catppuccin_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return random.choice(catppuccin_mocha_colors)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to extract texts from JSON and save to CSV
def extract_text(json_file):
    texts = []

    with open(json_file, 'r', encoding='utf-8') as file:
        parser = ijson.items(file, 'messages.item')

        for message in parser:
            if 'text' in message:
                if type(message['text']) == str and message['text'].strip():
                    texts.append(message['text'])

    df = pd.DataFrame(texts, columns=['text'])
    df.to_csv(resource_path('result.csv'), index=False)

# Function to generate a word cloud using Catppuccin Mocha theme
def gen_cloud(csv_file, cwords, background_color='#1E1E2E', res_w='1920', res_h='1080'):  # Default background as Catppuccin base color
    if cwords:
        if os.path.exists(cwords):
            with open(cwords, 'r', encoding='utf-8') as f:
                custom_stopwords = {line.strip() for line in f if line.strip()}
            print("Using custom stopwords from "+cwords)
        else:
            print(cwords+" not found! Falling back to default stopwords.")
            custom_stopwords = set()
    else:
        custom_stopwords = set()

    # Initialize default stopwords (Russian and English)
    stop_words = set(stopwords.words('russian'))
    stop_words.update(stopwords.words('english'))

    # Add custom stopwords to the default stopwords
    stop_words.update(custom_stopwords)

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Combine all text into a single string
    text = ' '.join(df['text'].dropna())

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove stopwords from the text
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

    # Generate and save the word cloud with the custom color function
    wordcloud = WordCloud(width=int(res_w), height=int(res_h), background_color=background_color, font_path=resource_path('font.otf'), color_func=catppuccin_color_func).generate(text)
    
    # Save the word cloud as an image
    wordcloud.to_file(values['tgres'].rstrip('result.json')+'cloud.png')
    os.remove(resource_path('result.csv'))
    print(f"Word cloud saved as cloud.png")

# Run the functions
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        sg.popup_quick_message('Hang on... processing files....', text_color='#A6E3A1', background_color='#1E1E2E')
        extract_text(values['tgres'])
        gen_cloud('result.csv', values['cwords'], res_w=values['res_w'], res_h=values['res_h'])
        sg.popup_quick_message('Saved as cloud.png into the chat directory', text_color='#A6E3A1', background_color='#1E1E2E')
window.close()


