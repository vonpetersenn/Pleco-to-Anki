from anki.collection import Collection
from anki_addon.notetype import NOTE_TYPE
notetype = NOTE_TYPE
import time

def initialize_note_type(col, notetype):
    if col.models.by_name(notetype['name']) is not None:
        print("notetype already exists in collection")
        notetype = col.models.by_name(notetype['name'])

    if notetype['id'] is None:
        print("notetype does not exist in collection yet")
        col.models.add(notetype)
        col.models.save(notetype)
        notetype = col.models.get(notetype['id'])

    return notetype
########################

col = Collection("C:/Users/Paulo/AppData/Roaming/Anki2/Chinesisch/collection.anki2")
notetype = initialize_note_type(col, notetype)

note_dict = {"Hanzi": "泡茶", "Pinyin": "paocha", "Definition": "to make tea",
             "Examples": "diese anderen details", "Spoonfed": "", "Picture": "", "Audio": ""}


def add_note_to_collection(note_dict, config):

    today = time.strftime("%Y-%m-%d")
    deck_name = 'pleco::' + today
    tags = ['pleco::' + today]

    deck_id = col.decks.id(deck_name)

    if col.find_notes(note_dict['Hanzi']) == []:
        print( "note does not exist in collection yet" )
    elif config.existing_notes == 'skip':
        return
    elif config.existing_notes == 'dublicates':
        tags.append('dublicate')



print(note_dict["Hanzi"])
deck_name = "pleco::15asdasdffasdf"
tag = "tagitaggen"
deck_id = col.decks.id(deck_name)


if col.find_notes(note_dict['Hanzi']) == []:
    print( "note does not exist in collection yet" )

note = col.new_note(notetype)
note.fields[0] = note_dict["Hanzi"]
note.fields[1] = note_dict["Pinyin"]
note.fields[2] = note_dict["Definition"]
note.fields[3] = note_dict["Examples"]
note.fields[4] = note_dict["Spoonfed"]



note.tags = tag
col.add_note(note, deck_id)


col.close()

#initialize new note
#note = col.new_note(notetype)

#deck_id = col.decks.id(deck_name)
#note.fields = {note_dict["Front"]: "Front", note_dict["Back"]: "Back", note_dict["Details"]: "Details"}
#note.tags = ["pleco::2021-01-01"]
#col.add_note(note, deck_id=deck_id)





