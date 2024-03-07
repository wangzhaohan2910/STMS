from xml.etree.ElementTree import *
from xml.dom.minidom import parseString


def prettier(xml_element):
    raw_string = tostring(xml_element)
    pretty_tree = parseString(raw_string)
    prettied_string = pretty_tree.toprettyxml()
    return prettied_string


def loader(filename):
    tree = None
    data = {"teacher": {}, "pupil": {}}
    with open(filename, "r") as file:
        tree = parse(file)
    for node in tree.iter("teacher"):
        name = node.attrib.get("name")
        data["teacher"][name] = set()
        for pupil in node.iter("pupilname"):
            data["teacher"][name].add(pupil.text)
    for node in tree.iter("pupil"):
        name = node.attrib.get("name")
        data["pupil"][name] = set()
        for teacher in node.iter("teachername"):
            data["pupil"][name].add(teacher.text)
    return data


def dumper(filename, data):
    xml = Element("document")
    teachers = SubElement(xml, "teachers")
    for each_teacher in data["teacher"].keys():
        the_teacher = SubElement(teachers, "teacher")
        the_teacher.set("name", each_teacher)
        for pupil_name in data["teacher"][each_teacher]:
            teacher_pupil = SubElement(the_teacher, "pupilname")
            teacher_pupil.text = pupil_name
    pupil = SubElement(xml, "pupils")
    for each_pupil in data["pupil"].keys():
        the_pupil = SubElement(pupil, "pupil")
        the_pupil.set("name", each_pupil)
        for teacher_name in data["pupil"][each_pupil]:
            pupil_teacher = SubElement(the_pupil, "teachername")
            pupil_teacher.text = teacher_name
    with open(filename, "w") as file:
        file.write(prettier(xml))


if __name__ == "__main__":
    from pprint import pprint

    data = {
        "teacher": {
            "tea1": {"pup1", "pup2", "pup3"},
            "tea2": {"pup2", "pup3", "pup4"},
            "tea3": {"pup3", "pup4", "pup5"},
            "tea4": {"pup4", "pup5"},
            "tea5": {"pup1", "pup2"},
        },
        "pupil": {
            "pup1": {"tea1", "tea5"},
            "pup2": {"tea1", "tea2", "tea5"},
            "pup3": {"tea1", "tea2", "tea3"},
            "pup4": {"tea2", "tea3", "tea4"},
            "pup5": {"tea3", "tea4"},
        },
    }
    dumper("data.xml", data)
    data2 = loader("data.xml")
    print("\n\nData before changes:\n")
    pprint(data)
    print("\n\nData after loading and printing:\n")
    pprint(data2)
    print("\n\nData uncorrupted:\n")
    print(data == data2)
