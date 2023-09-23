from anki.collection import Collection

from notetype import NOTE_TYPE
notetype = NOTE_TYPE


col = Collection("C:/Users/Paulo/AppData/Roaming/Anki2/Chinesisch/collection.anki2")

if col.models.by_name(notetype['name']) is not None:
    print("notetype already exists in collection")
    notetype = col.models.by_name(notetype['name'])

if notetype['id'] is None:
    print("notetype does not exist in collection yet")
    col.models.add(notetype)
    col.models.save(notetype)
    notetype = col.models.get(notetype['id'])

print(notetype['name'])

col.close()