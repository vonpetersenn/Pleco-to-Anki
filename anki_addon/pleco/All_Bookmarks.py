class All_Bookmarks:
    def __init__(self, file_name):

        self.raw_data = load_pleco_data(file_name)

    def get_slice(self, index):
        return self.raw_data[index]

    def __len__(self):
        return len(self.raw_data)

def load_pleco_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()

            rows = file_content.split('\n')

            data = []

            for row in rows:
                cells = row.split('\t')

                if len(cells) == 3:

                    entry = {
                        "Hanzi": cells[0],
                        "Pinyin": cells[1],
                        "Information": cells[2]
                    }

                    data.append(entry)

        return data

    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

#print(load_pleco_data("exampledata.txt")[5].get("Hanzi"))