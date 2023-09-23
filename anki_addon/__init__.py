from aqt import mw

from aqt.utils import qconnect, showInfo, QAction

from .Configuration import Configuration

import time


#everything in excecuted_function, as using submodules are not connected
    #to the Collection object mw.col, as this one is ONLY callable through qconnect
    #so any function working on the col need a new button in anki
#at least I haven't found another way to call mw.col from a submodule
#in the terminal it works, but not relatively with the addon

def excecuted_function() -> None:
    configs = Configuration()

    #initialize note type
    #TODO: find out why first time the notetype is created twice
    notetype = get_notetype()
    if mw.col.models.by_name(notetype['name']) is not None:
        print("notetype already exists in collection")
        notetype = mw.col.models.by_name(notetype['name'])
    if mw.col.models.by_name(notetype['name']) is None:
        print("notetype does not exist in collection yet")
        mw.col.models.add_dict(notetype)
        mw.col.models.save(notetype)
        notetype = mw.col.models.by_name(notetype['name'])


    deck_name = "pleco::" + time.strftime("%Y-%m-%d")
    deck_id = mw.col.decks.id(deck_name)

    tag = "pleco::" + time.strftime("%Y-%m-%d")

    note_note = {}
    note_note.update({"Hanzi": "泡茶"})
    note_note.update({"Pinyin": "paocha"})
    note_note.update({"Definition": "to make tea"})
    note_note.update({"Examples": "diese anderen details"})
    note_note.update({"Spoonfed": ""})

    note = mw.col.new_note(notetype)

    if mw.col.find_notes(note_note.get('Hanzi')) == []:
        print("note does not exist in collection yet")
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

    showInfo("New cards created.")


from .notetype import NOTE_TYPE
def get_notetype():
    return NOTE_TYPE


action = QAction("test", mw)
qconnect(action.triggered, excecuted_function)
mw.form.menuTools.addAction(action)
