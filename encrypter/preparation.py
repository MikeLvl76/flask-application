from os import system, sep
from urllib.request import urlopen
import pandas as pd
from glob import glob
from os.path import isdir

# classic alphabet size
romanic_alphabet_length = 26

ascii_type = {
    'lowercase': [(97, 122)],
    'uppercase': [(65, 90)],
    'digit': [(48, 57)],
    'symbol': [(33, 47), (58, 64), (91, 96)]
}

# fecthes all files with given extension and returns it as dictionnary
def fetch_files(extension: str):
    if not isdir('resources_files'):
        system('mkdir resources_files')
    files = glob(f"resources_files{sep}*.{extension}")
    if len(files) == 0:
        return {}

    names = [name[name.index('\\') + 1:name.index('.')] for name in files]

    return dict(zip(names, files))

# scraps emoji list on web and writes it to txt file
# if used url is down or changed, then this function is unusable
# writting method is raw and can be improved later (one line = one emoji)
def write_emojis(filename: str):
    file = fetch_files('txt')
    if filename in file.values():
        print(f'Rewritting {filename}...')

    url = "https://carpedm20.github.io/emoji/"
    with urlopen(url) as i:
        html = i.read()

    data = pd.read_html(html)[0]
    dictionnary = data.to_dict()
    names = dictionnary[('name', 'en')]
    collect = [value for item, value in names.items()][:-1]

    with open(f'resources_files{sep}{filename}', 'w', encoding='utf-8') as writer:
        for item in collect:
            writer.write(item + '\n')
    
if __name__ == '__main__':
    write_emojis('emoji.txt')