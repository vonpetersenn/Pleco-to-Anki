from aqt.importing import importFile


# Specify the path to the file you want to import
file_path = "/path/to/your/file.txt"

# Create an importFile object
importer = importFile.Importer(mw.col, file_path)
