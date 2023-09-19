# Pleco-to-Anki

An AddOn for the Anki flashcard app to import bookmark files from the chinese dictionary app Pleco.

# Motivation

Anki and Pleco are great tools for learning Chinese. However, they do not work very well together.
When learning new words, I usually look them up in Pleco and add them to my Pleco bookmarks. However, when I want to practice these words, I use Anki. This means that I have to manually copy the words from Pleco to Anki. This is a very tedious process and I often end up not doing it.

This project aims to solve this problem by providing a tool to import Pleco bookmarks into Anki.
This tool will import all information stored in the Pleco Bookmarks, such as the Chinese characters, pinyin, definition, and example sentences and sort them into corresponding fields in Anki.

# What this tool does

The Pleco app allows for users to store bookmarks and to export these bookmarks to a textfile. This tool will parse the textfile and import the bookmarks into Anki. 
The bookmarks will be sorted into corresponding fields in Anki, such as the Chinese characters, pinyin, definition, and example sentences.

After importing the Bookmarks, one only has to give the cards a final touch in Anki to ones liking, for example by deleting redundantly much information, adding pictures, or changing the note type.

Since the information stored in Pleco bookmark is not well sorted, this tool does not work perfectly, sometimes the formatting of the information will be off or sorted in the wrong field. However, it still speeds up the process of building high quality anki cards, since it automates most of the work and adds some clever HTML formatting to the notes.

Additionally, this Add-On can add example sentences from [Spoonfed Chinese](https://promagma.gumroad.com/l/IEmpwF) to the Anki cards.
This feature is **turned off by default** and can be turned on in the settings.
The add on will add sentences from the Spoonfed Chinese anki deck that contain the word at hand to the card.
Since the Spoonfed decks contain thousands of sentences with audio files from native speakers, this is a great way to learn and practice chinese pronounciation from context.
In order for this feature to work, the Spoonfed anki deck need to be loaded in your Anki decks. The deck can be bought on the website of Spoonfed Chinese (https://promagma.gumroad.com/l/IEmpwF).

## Example of a card being imported from Pleco to Anki

![img_19.png](README_media/img_19.png)
1) Bookmark in Pleco
2) Raw Data after exporting the Pleco Bookmarks
3) Card after importing the Pleco Bookmarks into Anki using this tool
4) Card after manually editing the card in Anki

# Installation

## Requirements

# Usage

## A) Export Pleco Bookmarks in the Pleco app

1. In the pleco app got to `Import / Export` - `Export Bookmarks`

2. Make sure to match the `File Format`and `Include Data`options from the screenshot below. As for the `Character Set`, you can choose `traditional` or `simplified`.

![img_4.png](README_media/img_4.png)

Then `Begin Export`.

3. Go to the file manager and send the file to your computer, e.g. via Messenger, AirDrop, E-Mail etc.
![img_6.png](README_media/img_6.png)

## B) Import Pleco Bookmarks into Anki using this AddOn



## C) Reformat the cards to your liking

Example of a card after importing the Pleco bookmarks. In red the example sentences from Pleco, in green the example sentences from Spoonfed Chinese.

![img.png](README_media/img.png)

View of the note in anki while editing. Either edit the note in the standard view or click on the button to the top right of each field to edit the HTML code directly.
![img_2.png](README_media/img_2.png)

Same card after manual editing.
![img_3.png](README_media/img_3.png)

# Features

## Sort information into fields

The defintion with examples in pleco bookmarks are not sorted or seperated in any way. This tool tries to identify example sentences and sort them into a seperate field.

e.g. the definition of `中國` is 'China `中國大陸 zhōngguó dàlù Chinese mainland; mainland of China ....`
This string will be split into two fields:
definition: `China`
Example: `中國大陸 zhōngguó dàlù Chinese mainland; mainland of China ....`

This also works for words with multiple definitions and examples.

The tool creates notes with the fields `Chinese`, `Pinyin`, `Definition`, `Example` (and `Spoonfed` if the feature is turned on).

## Format information

### Prettier Pinyin

Pleco bookmarks contain numerical pinyin (e.g. `ni3 hao3`). This tool converts the numerical pinyin to pinyin with tone marks (e.g. `nǐ hǎo`).
For this feature, we use a custom fork of the open source [tones](https://github.com/em-shea/tones) respository. 

### Reformatting example sentences

HTML tags will be added to the example sentences to make them look nicer in Anki. 
Most importantly the pinyin and translation of an example sentence will be hidden behind the Chinese characters and only be shown when clicking on the Chinese characters. 
The motivation for this is to make it easier to practice reading Chinese characters and not to rely on the pinyin and translation too much.

For example, the example sentence `中國大陸 zhōngguó dàlù Chinese mainland; mainland of China` of the word `中國` after importing to Anki will look like this:

![img_9.png](README_media/img_9.png)
![img_12.png](README_media/img_12.png)
![img_13.png](README_media/img_13.png)


### Reformat Keywords
Pleco notes can contain some keywords such as `verb`, `idiom`, `(TW)` etc. This tool will reformat these keywords to make them look nicer in Anki by replacing them and adding HTML tags for styling.

For example here ![img_14.png](README_media/img_14.png)
the keywords verb and adjective are replaced by *v.* and *SV*.

The replacement of keywords can be customised by changing the keyword_replacements.py file in the config\pleco folder.

## Add Spoonfed sentences
If you have the [Spoonfed Chinese](https://promagma.gumroad.com/l/IEmpwF) anki deck loaded in your Anki decks, this tool can add example sentences from the Spoonfed Chinese anki deck to the Anki cards.
The tool adds up to 3 example sentences from the Spoonfed deck that contain the word at hand to the card.
The idea is, to chose the sentence that best fits the desired difficulty level and to delete the other sentences.
Then, everytime when reviewing the card, one can listen to the Spoonfed example sentence and try to repeat it.
Both traditional and simplified characters are supported, specify which one you want to use in the settings.
The number of cards can be changed in the settings.
The feature can be turned on
TODO: add example, add settings

In this example, 3 sentences contain the character 藏 but actually, the first and third sentences contain the compound word 收藏  instead of the single character verb 藏 which I want to learn. So I quickly delete the first and third sentence and keep the second one for my notes.  
![img_15.png](README_media/img_15.png)
![img_17.png](README_media/img_17.png)
![img_18.png](README_media/img_18.png)

# Contributing

