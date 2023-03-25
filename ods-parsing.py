# Copyright Jeffrey LeBlanc

from pyexcel_ods3 import get_data

def ods_as_list(path, sheet='Sheet1'):
    data = get_data(str(path))
    sheet1 = data[sheet]
    keys = sheet1[0]
    entries = []
    for row in sheet1[1:]:
        d = dict(zip(keys,row))
        if '' in d: del d['']
        if len(d) > 0:
            entries.append(d)
    return entries

class OdsFile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = get_data(str(filepath))

    @property
    def sheet_names(self):
        return list(self.data.keys())

    @property
    def main(self):
        return self.data[self.sheet_names[0]]

    def entries(self, name):
        sheet = self.data[name]
        keys = sheet[0]
        entries = []
        for row in sheet[1:]:
            d = dict(zip(keys,row))
            if '' in d: del d['']
            if len(d) > 0:
                entries.append(d)
        return entries

    def sheet_keys(self, name):
        sheet = self.data[name]
        return sheet[0]


