import pandas as pd

import time

# for AddOn
from aqt import mw
col = mw.col

# for testing in console
#from anki.collection import Collection
#col = Collection("C:/Users/Paulo/AppData/Roaming/Anki2/Chinesisch/collection.anki2")
from Configuration import Configuration

from notetype import NOTE_TYPE
notetype = NOTE_TYPE

def create_anki_cards(configs):


    new_notetype = initialize_note_type(col, notetype)

    deck_name = "pleco::" + time.strftime("%Y-%m-%d")
    deck_id = col.decks.id(deck_name)

    tag ="pleco::" + time.strftime("%Y-%m-%d")

    note_pd_slice = pd.Series()
    note_pd_slice['Hanzi'] = '泡茶'
    note_pd_slice['Pinyin'] = 'paocha'
    note_pd_slice['Definition'] = 'to make tea'
    note_pd_slice['Examples'] = 'diese anderen details'
    note_pd_slice['Spoonfed'] = ''

    note = col.new_note(new_notetype)


    if col.find_notes(note_pd_slice['Hanzi']) == []:
        print( "note does not exist in collection yet" )
    else:
        print("note already exists in collection")
        note.tags.append('dublicate')

    note.fields[0] = note_pd_slice["Hanzi"]
    note.fields[1] = note_pd_slice["Pinyin"]
    note.fields[2] = note_pd_slice["Definition"]
    note.fields[3] = note_pd_slice["Examples"]
    note.fields[4] = note_pd_slice["Spoonfed"]

    note.tags.append(tag)
    col.add_note(note, deck_id)

def initialize_note_type(col, notetype):

    if col.models.by_name(notetype['name']) is not None:
        print("notetype already exists in collection")
        notetype = col.models.by_name(notetype['name'])

    if col.models.by_name(notetype['name']) is None:
        print("notetype does not exist in collection yet")
        col.models.add_dict(notetype)
        col.models.save(notetype)
        notetype = col.models.by_name(notetype['name'])

    return notetype

configs = Configuration()

create_anki_cards(configs)

#for testing in console
col.close()