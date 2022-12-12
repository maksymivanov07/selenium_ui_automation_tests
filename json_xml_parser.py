import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from argparse import ArgumentParser


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        json_obj = json.dumps(self.__dict__)

        save_path = "Output.json"

        with open(save_path, "w") as f:
            f.write(json_obj)

        return json_obj

    def convert_to_xml(self):
        convert_to_dict = self.__dict__
        my_item_func = lambda x: x + 's'
        dict_to_xml_obj = dicttoxml(convert_to_dict, item_func=my_item_func)
        xml_obj = parseString(dict_to_xml_obj).toprettyxml()

        save_path = "Output.xml"

        with open(save_path, "w") as f:
            f.write(xml_obj)

        return xml_obj


new_human = Human('Max', '33', 'male', '1989')

parser = ArgumentParser(description='test')
parser.add_argument('--convert_to', help='Init converter')
arguments = parser.parse_args()

if arguments.convert_to == 'json':
    new_human.convert_to_json()
elif arguments.convert_to == 'xml':
    new_human.convert_to_xml()
