<h1 align="center">wordcloudTG</h1>
<p align="center">
  <img width="800" src="https://github.com/user-attachments/assets/22a15262-6b59-425e-9770-e6aafd1fb5c4" alt="Example word cloud of Pavel Durov's channel without masking and coloring">
</p>
<p align="center">
  <sup>Example word cloud of Pavel Durov's channel without masking and coloring.</sup>
</p>
<h2 align="center">Generate stunning word clouds for Telegram chats, groups and channels!</h2>


## Installation
Preffered installation method is Python, but you can use which ever you like.
### Windows executable
Go to the [**Releases**](https://github.com/Theriolu/wordcloudTG/releases) tab and download the **wordcloudTG-Windows.exe** file from the latest one.
Open it and proceed as explained in [**How to use**](https://github.com/Theriolu/wordcloudTG#how-to-use)

### Linux AppImage
Go to the [**Releases**](https://github.com/Theriolu/wordcloudTG/releases) tab and download the **wordcloudTG-x86_64.AppImage** file from the latest one.

Make sure it has execution permissions by running
```
$ chmod +x ./wordcloudTG-x86_64.AppImage
```
Then you can open it and proceed as explained in [**How to use.**](https://github.com/Theriolu/wordcloudTG#how-to-use)

### Any Platform (Python)
Make sure you have [**git**](https://git-scm.com/) installed, then navigate to where you want to download the program and run 
```
$ git clone https://github.com/Theriolu/wordcloudTG.git && cd ./wordcloudTG
```
Then you have to install all of the required libraries in order for it to work:
```
$ python -m pip install -r requirements.txt
```
## How to use
![GUI](https://github.com/user-attachments/assets/9527aea1-5504-484a-b0bb-2f7835c7d035)
### 1. Export chat data
Install the [**Telegram desktop app**](https://desktop.telegram.org/) on your computer.
In the Telegram desktop app, open the chat that you want to make the word cloud of.
Click on the **three-dot** icon at the top and select **“Export chat history”** from the menu.
Drag the slider to set the **maximum size** limit, **uncheck** everything and set the format to **Machine-readable JSON**.

### 2. Launch the program
Depending on your installation method launch the program by either **opening the .exe file**, opening the **.AppImage** or using
```
$ python main.pyw
```
in the program's root directory.

### 3. Generate the word cloud!
This step is pretty intuitive but i'll walk you through anyways.

In the first field you have to select the **result.json** file that you've exported from Telegram.

In the second field you *can* add your own list of [**stop words**](https://en.wikipedia.org/wiki/Stop_word), for example specific to your language. You can find them [**here**](https://github.com/stopwords-iso/). You can also set a custom resolution for the resulting image. Your stop words will be added to the built-in ones. If you don't want this you can turn this off in the [**advanced settings.**](https://github.com/Theriolu/wordcloudTG#advanced-settings-%EF%B8%8F)

Then you can click on **Go** and the word cloud will be <ins>**saved to the directory where the result.json is stored**</ins> in .PNG format.

<details>
<summary><h2>Advanced settings 🛠️</h2></summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/c87ebdbf-bbcd-4edd-a3bb-facd686ff687" alt="Advanced GUI">
</p>

Advanced settings let you tweak your word cloud to get a better looking result and add aditional generation options:
  
* **Mask** - Makes the words flow in a custom shape.
  * When using a mask the resulting image will be the same resolution as the mask.
  * Mask can be any color you want, where masked out area shold be **#FFFFFF** white.
* **Mask Color Inheritance** - Makes the words inherit their color from the mask based on their position.

<img src="https://github.com/user-attachments/assets/69dae8a0-175c-4ce9-a8ba-81e3fde92f2c" width="500" alt="Example word cloud of Pavel Durov's channel with masking and coloring">

<sup>Example word clouds of Pavel Durov's channel with masking and coloring</sup>

* **Custom Font Support** - Use a custom font in OTF or TTF format.
* **Word Limit** - Define the maximum amount of words used.
* **Font Size** - Define a range of font sizes.
* **Repeat Words** - Repeat already used words until the maximum word limit is reached.
* **Transparent Background** - Only render the words, without the background.
* **Only Use Custom Stopwords** - Use only the stopwords that you've added. (without the built-in ones)
</details>

## Credits
### SF Pro font by Apple
San Francisco is an Apple designed typeface that provides a consistent, legible, and friendly typographic voice. Across all Apple products, the size-specific outlines and dynamic tracking ensure optimal legibility at every point size and screen resolution. Numbers have proportional widths by default, so they feel harmonious and naturally spaced within the time and data-centric interfaces people use every day.

https://developer.apple.com/fonts/

### Catppuccin color palette
Catppuccin is a community-driven pastel theme that aims to be the middle ground between low and high contrast themes. It consists of 4 soothing warm flavors with 26 eye-candy colors each, perfect for coding, designing, and much more!

https://github.com/catppuccin/catppuccin
