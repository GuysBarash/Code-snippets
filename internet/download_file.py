import urllib
import os

path = r'http://proceedings.mlr.press/v80/gilra18a/gilra18a.pdf'
target_dir = r'C:\Users\32519\Desktop\pdffolder\pdfs'

if __name__ == '__main__':
    fname = path.split('/')[-1]
    fname_path = os.path.join(target_dir, fname)
    urllib.urlretrieve(path, fname_path)
