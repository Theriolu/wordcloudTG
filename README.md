# wordcloudTG
Generate word clouds for Telegram chats, groups and channels!


![Example word cloud of Pavel Durov's channel](https://github.com/user-attachments/assets/22a15262-6b59-425e-9770-e6aafd1fb5c4 "Example word cloud of Pavel Durov's channel")
<sup>Example word cloud of Pavel Durov's channel</sup>
## Installation
Preffered installation method is Python, but you can use which ever you like.
### Windows executable
Go to the **Releases** tab and download the **.exe** file from the latest one.
Open it and proceed as explained in [How to use](https://github.com/Theriolu/wordcloudTG#how-to-use)

### Any Platform (Python)
Make sure you have [git](https://git-scm.com/) installed, then navigate to where you want to download the program and run 
```
$ git clone https://github.com/Theriolu/wordcloudTG.git && cd ./wordcloudTG
```
Then you have to install all of the required libraries in order for it to work:
```
$ python -m pip install -r requirements.txt
```
## How to use
![GUI](https://github.com/user-attachments/assets/21f33601-4b64-49b8-a570-fa9063143bd4)
### 1. Export chat data
Install the [Telegram desktop app](https://desktop.telegram.org/) on your computer.
In the Telegram desktop app, open the chat that you want to make the word cloud of.
Click on the **three-dot** icon at the top and select **“Export chat history”** from the menu.
Drag the slider to set the **maximum size** limit, **uncheck** everything and set the format to **Machine-readable JSON**.

### 2. Launch the program
Depending on your installation method launch the program by either **opening the .exe file** or using
```
$ python main.pyw
```
in the program's root directory.

### 3. Generate the word cloud!
This step is pretty intuitive but i'll walk you through anyways.

In the first field you have to select the **result.json** file that you've exported from Telegram.

In the second field you *can* add your own list of [stop words](https://en.wikipedia.org/wiki/Stop_word), for example specific to your language. You can find them [here](https://github.com/stopwords-iso/). You can also set a custom resolution for the resulting image.

Then you can click on **Go** and the word cloud will be <ins>**saved to the directory where you've exported the chat**</ins> in .PNG format.
