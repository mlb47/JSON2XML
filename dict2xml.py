from xml.etree.ElementTree import Element, tostring, SubElement

def get_data_type(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        tag = 'number'
    elif isinstance(value, str):
        tag = 'string'
    elif isinstance(value, bool):
        tag = 'boolean'
    elif isinstance(value, list):
        tag = 'array'
    elif isinstance(value, dict):
        tag = 'object'
    elif value is None:
        tag = 'null'  
    else:
        tag = 'unknown'
    return tag

def instance_handler(elem, val):
    if isinstance(val, dict):
        dict_handler(elem, val)
    elif isinstance(val, list):
        list_handler(elem, val)
    elif val is None:
        elem.text = None
    else:
        elem.text = str(val)

def dict_handler(elem, d):
    for name, val in d.items():
        data_type = get_data_type(val)
        child = SubElement(elem, data_type, name=name)
        instance_handler(child, val)
        
def list_handler(elem, val):
    for item in val:
        data_type = get_data_type(item)
        arrayChild = SubElement(elem, data_type)
        instance_handler(arrayChild, item)

def dict_to_xml(root, d):
    elem = Element(root)
    instance_handler(elem, d)
    xml_string = tostring(elem).decode("utf-8")
    return xml_string