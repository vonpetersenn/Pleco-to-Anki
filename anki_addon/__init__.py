from aqt import mw

from aqt.utils import qconnect, showInfo, QAction

from .Configuration import Configuration

import time

from .ImportBookmarksGUI import ImportBookmarksGUI
from .pleco.Bookmarks import Bookmarks
from .pleco.Bookmark import Bookmark

#everything in excecuted_function, as using submodules are not connected
    #to the Collection object mw.col, as this one is ONLY callable through qconnect
    #so any function working on the col need a new button in anki
#at least I haven't found another way to call mw.col from a submodule
#in the terminal it works, but not relatively with the addon

def excecuted_function() -> None:


    #dialog = ImportBookmarksGUI()
    #configs = dialog.config_from_user_input()
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

    ########

    #showInfo("Importing bookmarks from " + file_name)
    all_bookmarks = Bookmarks(configs.file_name)

    counter = 0
    counter_dublicates = 0

    for slice in [all_bookmarks.get_slice(5)]: #in all_bookmarks.raw_data:

        dict = {}

        bookmark = Bookmark(slice, configs)

        dict.update({"Hanzi": bookmark.hanzi})
        dict.update({"Pinyin": bookmark.pinyin})
        dict.update({"Definition": bookmark.definiton})
        dict.update({"Examples": bookmark.examples})
        dict.update({"Spoonfed": bookmark.spoonfed})

        note = mw.col.new_note(notetype)

        note.fields[0] = dict.get("Hanzi")
        note.fields[1] = dict.get("Pinyin")
        note.fields[2] = dict.get("Definition")
        note.fields[3] = dict.get("Examples")
        note.fields[4] = dict.get("Spoonfed")

        note.tags.append(tag)

        if mw.col.find_notes(dict.get('Hanzi')) == []:
            print("note does not exist in collection yet")
        elif configs.existing_notes == 'skip':
            print("note already exists in collection")
            pass #continue
        else:
            print("note already exists in collection")
            counter_dublicates += 1
            note.tags.append('dublicate')

        mw.col.add_note(note, deck_id)

        counter += 1

    showInfo(str(counter) +
             " new cards created, of which " +
             str(counter_dublicates) +
             " are dublicates" +
             str(configs.file_name)
             )


from .notetype import NOTE_TYPE
def get_notetype():
    return NOTE_TYPE


action = QAction("test", mw)
qconnect(action.triggered, excecuted_function)
mw.form.menuTools.addAction(action)
