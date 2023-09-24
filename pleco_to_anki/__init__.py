import time

from aqt import mw
from aqt.utils import qconnect, showInfo, QAction

from pleco_to_anki.Configuration import Configuration

from .ImportBookmarksGUI import ImportBookmarksGUI
from .pleco.All_Bookmarks import All_Bookmarks
from .pleco.Bookmark import Bookmark
from .spoonfed.Spoonfed import Spoonfed

#TODO: config file to modify the word replacements.

#for some reason, when running the AddOn, the Collection object mw.col is ONLY callable through qconnect
#so any function working on the col need to be in one big function, not in submodules
def excecuted_function() -> None:


    dialog = ImportBookmarksGUI()
    configs = dialog.config_from_user_input()

    if configs.run_code == False:
        return

    #configs = Configuration()

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

    all_bookmarks = All_Bookmarks(configs.file_name)

    counter = 0
    counter_duplicates = 0

    #for slice in [all_bookmarks.get_slice(5)]: #in all_bookmarks.raw_data:

    for slice in all_bookmarks.raw_data:

        dict = {}

        bookmark = Bookmark(slice, configs)

        dict.update({"Hanzi": bookmark.hanzi})
        dict.update({"Pinyin": bookmark.pinyin})
        dict.update({"Definition": bookmark.definition})
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
            counter_duplicates += 1
            continue
        else:
            print("note already exists in collection")
            counter_duplicates += 1
            note.tags.append('duplicate')

        mw.col.add_note(note, deck_id)

        counter += 1

    showInfo("Successfully created " + str(counter) +
             " new cards. \n\n"  +
             "Of the " + str(len(all_bookmarks)) + " bookmarks " + str(counter_duplicates) +
             " where duplicates, i.e. cards with the same Hanzi field where already in the collection. \n"+
             "To delete or work on duplicates, look for the tag 'duplicate'.")

from .notetype import NOTE_TYPE

def get_notetype():
    return NOTE_TYPE

action = QAction("Import Pleco Bookmarks", mw)
qconnect(action.triggered, excecuted_function)
mw.form.menuTools.addAction(action)
