import ijson
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
import numpy as np
from PIL import Image
from nltk.corpus import stopwords
import string
import random
import os
import sys
import webbrowser
from scipy.ndimage import gaussian_gradient_magnitude
import PySimpleGUI as sg

icon_base64='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'

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

layout = [
    [sg.Text('Exported result.json:', size=(22,1)), sg.Push(), sg.Input(key='tgres', readonly=True, disabled_readonly_background_color='#11111b'), sg.FileBrowse()],
    [sg.Text('Custom stopwords (optional):', size=(27,1)), sg.Push(), sg.Input(key='cwords', readonly=True, disabled_readonly_background_color='#11111b'), sg.FileBrowse()],
    [sg.Push(), sg.Text('Resolution:', size=(12,1)), sg.Input(default_text='1920', size=(5,5), key='res_w'), sg.Text('x'), sg.Input(default_text='1080', size=(5,5), key='res_h'), sg.Push()],
    [sg.Checkbox('Advanced', key='-SHOW_ADVANCED-', enable_events=True)],
    [sg.Text('How to use?', key='-HOWTOUSE-', text_color='#F5C2E7', enable_events=True, font=(None, 12, 'underline')), sg.Push(), sg.Button('Go'), sg.Button('Exit')],
    
    # The advanced options wrapped in a column, initially hidden
    [sg.Column([
        [sg.Push(), sg.Text('Advanced options', font=(None, 12), text_color='#FAB387'), sg.Push()],
        [sg.Text('Cloud mask:', size=(12,1)), sg.Checkbox(text='Inherit color', key='inherit_mask'),sg.Push(), sg.Input(key='maskpath', readonly=True, disabled_readonly_background_color='#11111b'), sg.FileBrowse()],
        [sg.Text('Custom font (OTF or TTF):', size=(27,1)), sg.Push(), sg.Input(key='cfont', readonly=True, disabled_readonly_background_color='#11111b'), sg.FileBrowse()],
        [sg.Push(), sg.Text('Max words:', size=(12,1)), sg.Input(default_text='200', size=(5,5), key='maxwords'), sg.Text('Font size(min/max)', size=(20,1)), sg.Input(default_text='4', size=(5,5), key='font_min'), sg.Text('/'), sg.Input(default_text='0', size=(5,5), key='font_max'), sg.Checkbox(text='Repeat words', key='repeat'), sg.Checkbox(text='Transparent', key='transparent'), sg.Checkbox(text='Only custom stopwords', key='onlycwords'), sg.Push()]
    ], key='-ADVANCED-', visible=False)]
]
window = sg.Window('Telegram Word Cloud Generator', layout, icon=icon_base64)

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
        base_path = os.path.dirname(os.path.abspath(__file__))
        #base_path = os.path.abspath(".")

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
    df.to_csv(json_file.rstrip('result.json')+'result.csv', index=False)

# Function to generate a word cloud using Catppuccin Mocha theme
def gen_cloud(csv_file, cwords, transparent=False, mask=None, inherit_mask=False,cfont=None, repeat=False, maxwords=200, font_min=4, font_max=0,onlycwords = False, res_w='1920', res_h='1080'):  # Default background as Catppuccin base color
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
    

    if onlycwords == False:    
        # Initialize default stopwords (Russian and English)
        stop_words = set(stopwords.words('russian'))
        stop_words.update(stopwords.words('english'))

        # Add custom stopwords to the default stopwords
        stop_words.update(custom_stopwords)
    else:
        stop_words.set(custom_stopwords)
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Combine all text into a single string
    text = ' '.join(df['text'].dropna())

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove stopwords from the text
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    if font_max == None or font_max == '' or font_max == '0':
        font_max=None
    else:
        font_max=int(font_max)
    font_min = int(font_min)
    if transparent:
        background_color = None
        mode = 'RGBA'
    else:
        background_color = '#1E1E2E'
        mode = 'RGB'
    

    if cfont == None or cfont == '':
        cfont=resource_path('font.otf')
    # Generate and save the word cloud with the custom color function

    if mask != None and mask != '':
        mask_pil=Image.open(mask)
        mask=np.asarray(mask_pil)
        if inherit_mask:
            mask_color = mask
            mask=mask_color.copy()
            mask[mask.sum(axis=2) == 0] = 255
            edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
            mask[edges > .08] = 255
            wc = WordCloud(width=int(res_w), height=int(res_h), max_font_size=font_max, min_font_size=font_min, background_color=background_color, mask=mask, mode=mode, font_path=cfont, max_words=int(maxwords), repeat=repeat)
            wc.generate(text)
            image_colors = ImageColorGenerator(mask_color)
            wc.recolor(color_func=image_colors)
            wc.to_file(values['tgres'].rstrip('result.json')+'cloud.png')
            os.remove(csv_file)
            print(f"Word cloud saved as cloud.png")
            return
    else:
        mask = None

    wordcloud = WordCloud(width=int(res_w), height=int(res_h), max_font_size=font_max, min_font_size=font_min, background_color=background_color, mask=mask, mode=mode, font_path=cfont, max_words=int(maxwords), repeat=repeat, color_func=catppuccin_color_func).generate(text)
    
    # Save the word cloud as an image
    wordcloud.to_file(values['tgres'].rstrip('result.json')+'cloud.png')
    os.remove(csv_file)
    print(f"Word cloud saved as cloud.png")

# Run the functions
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == '-HOWTOUSE-':
        webbrowser.open('https://github.com/Theriolu/wordcloudTG/blob/Windows/README.md#how-to-use')
    if event == 'Go':
        sg.popup_quick_message('Processing files.... this might take a while...', text_color='#A6E3A1', background_color='#1E1E2E')
        extract_text(values['tgres'])
        gen_cloud(values['tgres'].rstrip('result.json')+'result.csv', values['cwords'], res_w=values['res_w'], res_h=values['res_h'], font_max=values['font_max'], font_min=values['font_min'],transparent=values['transparent'], mask=values['maskpath'], inherit_mask=values['inherit_mask'], cfont=values['cfont'], repeat=values['repeat'], maxwords=values['maxwords'], onlycwords=values['onlycwords'])
        sg.popup_quick_message('Saved as cloud.png into the chat directory', text_color='#A6E3A1', background_color='#1E1E2E')
    
    # Toggle visibility of the advanced options
    if event == '-SHOW_ADVANCED-':
        window['-ADVANCED-'].update(visible=values['-SHOW_ADVANCED-'])    
window.close()


