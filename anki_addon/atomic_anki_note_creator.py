from anki.collection import Collection

col = Collection("C:/Users/Paulo/AppData/Roaming/Anki2/Chinesisch/collection.anki2")

#TODO: real import notetype funtion
def import_notetype():
    print("importing notetype")
    notetype = col.models.by_name("Basic")
    return notetype




note_dict = {"Front": "泡茶", "Back": "to make tea", "Details": "diese anderen details"}
deck_name = "pleco::1523652"


notetype = col.models.by_name("Basicasdf")

if notetype == None:
    notetype = import_notetype()
else:
    print("notetype already exists")

#initialize new note
note = col.new_note(notetype)

deck_id = col.decks.id(deck_name)
note.fields = {note_dict["Front"]: "Front", note_dict["Back"]: "Back", note_dict["Details"]: "Details"}
note.tags = ["pleco::2021-01-01"]
col.add_note(note, deck_id=deck_id)


col.close()

