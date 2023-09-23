import time

# for AddOn
from aqt import mw
col = mw.col

# for testing in console
#from anki.collection import Collection
#col = Collection("C:/Users/Paulo/AppData/Roaming/Anki2/Chinesisch/collection.anki2")
from anki_addon.Configuration import Configuration

from anki_addon.notetype import NOTE_TYPE
notetype = NOTE_TYPE

def create_anki_cards(configs):

    new_notetype = initialize_note_type(notetype)

    deck_name = "pleco::" + time.strftime("%Y-%m-%d")
    deck_id = mw.col.decks.id(deck_name)

    tag ="pleco::" + time.strftime("%Y-%m-%d")

    note_note = {}
    note_note.update({"Hanzi": "泡茶"})
    note_note.update({"Pinyin": "paocha"})
    note_note.update({"Definition": "to make tea"})
    note_note.update({"Examples": "diese anderen details"})
    note_note.update({"Spoonfed": ""})

    note = mw.col.new_note(new_notetype)


    if mw.col.find_notes(note_note.get('Hanzi')) == []:
        print( "note does not exist in collection yet" )
    else:
        print("note already exists in collection")
        note.tags.append('dublicate')

    note.fields[0] = note_note.get("Hanzi")
    note.fields[1] = note_note.get("Pinyin")
    note.fields[2] = note_note.get("Definition")
    note.fields[3] = note_note.get("Examples")
    note.fields[4] = note_note.get("Spoonfed")

    note.tags.append(tag)
    mw.col.add_note(note, deck_id)

def initialize_note_type(notetype):

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
#col.close()