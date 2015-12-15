
from lxml import etree

class TitleTarget(object):
    def __init__(self):
        self.text = []
    def start(self, tag, attrib):
        self.is_title = True if tag == 'QBody' else False
    def end(self, tag):
        pass
    def data(self, data):
        if self.is_title:
            self.text.append(data.encode('utf-8'))
    def close(self):
        return self.text

parser = etree.XMLParser(target = TitleTarget())

# This and most other samples read in the Google copyright data
infile = 'test.xml'

results = etree.parse(infile, parser)    

# When iterated over, 'results' will contain the output from 
# target parser's close() method

out = open('QBody.txt', 'w')
out.write('\n'.join(results))
out.close()