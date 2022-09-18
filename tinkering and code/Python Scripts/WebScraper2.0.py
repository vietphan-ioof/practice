filename = "cache/epub/78/pg78.rdf"
from lxml import etree
rdf = open(filename).read()
tree = etree.fromstring(rdf)
resource_tag = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource'
hasFormat_tag = './/{http://purl.org/dc/terms/}hasFormat'
resources = [el.attrib[resource_tag] for el in tree.findall(hasFormat_tag)]
urls = [url for url in resources if url.endswith('htm')]

import requests
response = requests.get(urls[0])
html = etree.HTML(response.text)
text = '\n'.join([el.text for el in html.findall('.//p')])


