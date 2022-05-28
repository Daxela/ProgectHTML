import bs4
from bs4 import BeautifulSoup
import requests as req
from .constants import *
class WebProcessor:
    def __init__(self, hyperlink=HYPERLINK, address=ADDRESS, indirect_information=INDIRECT_INFORMATION, source=SOURCE, footer=FOOTER, heading=HEADING, annotation=ANNOTATION, ignored=IGNORED, min_tag_len=3):
        self.deleted_tags = {"hyperlink": hyperlink, "address": address, "indirect_information": indirect_information, "source": source, "footer": footer,
                        "heading": heading, "annotation": annotation}
        self.ignored = ignored
        self.min_tag_len = min_tag_len

    def web_parser(self, vershina, deleted_data, general_data):
        if type(vershina) == bs4.element.Tag:
            name = vershina.name
            if name is None:
                general_data.append(vershina.text)
            elif not name in self.ignored:
                tag_is_deleted = False
                for key in self.deleted_tags:
                    if name in self.deleted_tags[key]:
                        tag_is_deleted = True
                        deleted_data[key].append(vershina.text)
                if not tag_is_deleted:
                    for content in vershina.contents:
                        self.web_parser(content, deleted_data, general_data)

        else:
            general_data.append(vershina.text)

    def process(self, url):
        resp = req.get(url)
        deleted_data = {}
        for key in self.deleted_tags:
            deleted_data[key]=[]
        general_data = []
        soup = BeautifulSoup(resp.text, 'html.parser')
        self.web_parser(soup.head, deleted_data, general_data)
        self.web_parser(soup.body, deleted_data, general_data)
        return general_data, deleted_data

    def post_process(self, data):
        result_data = []
        for element in data:
            temp_element = element.replace("\n", "").replace(" ","")
            if len(temp_element)>=self.min_tag_len:
                result_data.append(element)
        return result_data