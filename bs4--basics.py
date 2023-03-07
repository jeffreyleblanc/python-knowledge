#! /usr/bin/env python3

'''
https://beautiful-soup-4.readthedocs.io/en/latest/
()$ pip3 install beautifulsoup4
'''

from pathlib import Path
from bs4 import BeautifulSoup


def main():
    # Open a File and parse it
    html_file = Path('bs4--basics-source.html')
    html_doc = html_file.read_text()
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Print the html out 'pretty'
    ## print(soup.prettify())

    # Example of finding all links and then generating markdown from them
    markdown_list = []
    for link in soup.find_all('a'):
        href = link['href']
        text = link.get_text()
        markdown_list.append(f'[{text}]({href})')
    for md in markdown_list:
        print('* '+md)

if __name__ == '__main__':
    main()


