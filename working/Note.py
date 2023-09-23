import time

class Note:
    def __init__(self, bookmarks):

        self.deck_name = "pleco::" + time.strftime("%Y-%m-%d")

        self.tags = []
        self.tags.append(self.deck_name)

        self.fields = {}
        self.fields = bookmarks.get_fields()

        self.note_type = ""
        self.note_id = ""

        self.existing_notes = 'dublicates' #'dublicates' or 'skip'. Maybe in the future add option 'update' or 'overwrite'




