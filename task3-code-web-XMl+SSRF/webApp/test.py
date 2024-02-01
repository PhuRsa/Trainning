from lxml import etree
import os

content = 'helloworld'
size = '128'
font_size ='16'
imageSvg = f'''<?xml version="1.0" ?>
<!DOCTYPE test [ <!ENTITY xxe {content} > ]>
<svg width="{size}px" height="{size}px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
<text font-size="{font_size}" x="0" y="16"> &xxe; </text>
</svg>
        '''
parser = etree.XMLParser(resolve_entities=True, dtd_validation=False, load_dtd=True)
tree = etree.fromstring(imageSvg,parser)
parsed_xml = etree.tostring(tree)
print(parsed_xml)