class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def load(self, filename):
        file = open(filename, 'r')
        self.entries = file.read().splitlines()
        file.close()

    def load_from_url(self, url):
        pass

    def __str__(self):
        return '\n'.join(self.entries)

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I ate a bug')
j.add_entry('I saw a bug')

file = r'/Users/rafsan/Local/test/1-SOLID/journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())