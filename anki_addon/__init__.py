from aqt import mw

from aqt.utils import qconnect, showInfo, QAction

from .Configuration import Configuration

import time

from .ImportBookmarksGUI import ImportBookmarksGUI

#everything in excecuted_function, as using submodules are not connected
    #to the Collection object mw.col, as this one is ONLY callable through qconnect
    #so any function working on the col need a new button in anki
#at least I haven't found another way to call mw.col from a submodule
#in the terminal it works, but not relatively with the addon

def excecuted_function() -> None:


    dialog = ImportBookmarksGUI()
    configs = dialog.config_from_user_input()




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

    ########
    # inprinciple add modified version of script from main.py here
    file_name = configs.file_name

    # get notes from Bookmarks TODO:modify Bookmarks to work without pandas
    dict = {}
    dict.update({"Hanzi": "泡茶"})
    dict.update({"Pinyin": "paocha"})
    dict.update({"Definition": "to make tea"})
    dict.update({"Examples": "diese anderen details"})
    dict.update({"Spoonfed": ""})
    notes = [dict]

    counter = 0
    counter_dublicate = 0

    for dict in notes:

        note = mw.col.new_note(notetype)

        if mw.col.find_notes(dict.get('Hanzi')) == []:
            print("note does not exist in collection yet")
        elif configs.existing_notes == 'skip':
            print("note already exists in collection")
            continue
        else:
            print("note already exists in collection")
            counter_dublicate += 1
            note.tags.append('dublicate')

        note.fields[0] = dict.get("Hanzi")
        note.fields[1] = dict.get("Pinyin")
        note.fields[2] = dict.get("Definition")
        note.fields[3] = dict.get("Examples")
        note.fields[4] = dict.get("Spoonfed")

        note.tags.append(tag)
        mw.col.add_note(note, deck_id)

        counter += 1

    showInfo(str(counter) +
             " new cards created, of which " +
             str(counter_dublicate) +
             " are dublicates" +
             str(configs.file_name)
             )


from .notetype import NOTE_TYPE
def get_notetype():
    return NOTE_TYPE


action = QAction("test", mw)
qconnect(action.triggered, excecuted_function)
mw.form.menuTools.addAction(action)
