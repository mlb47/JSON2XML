import json
import dict2xml

#Tests the programs ability to properly identify type values
def test_values():
    with open('examples/example1.json') as data:
      jsonData = json.load(data)
    xml = dict2xml.dict_to_xml('object', jsonData)
    expected = '<object><number name="cars">2</number><number name="trucks">3</number><string name="firstname">Adam</string><boolean name="isHuman">True</boolean><null name="computer_name" /></object>'
    assert(xml==expected)

#Tests the programs ability to properly handle lists
def test_lists():
    with open('examples/example2.json') as data:
      jsonData = json.load(data)
    xml = dict2xml.dict_to_xml('object', jsonData)
    expected = '<object><array name="friends"><string>Joe</string><object><string name="firstname">Sue</string><string name="lastname">Jones</string></object></array></object>'
    assert(xml==expected)

#Tests the programs ability to translate a more complex JSON file to XML 
def test_securin_example():
    with open('examples/example3.json') as data:
      jsonData = json.load(data)
    xml = dict2xml.dict_to_xml('object', jsonData)
    expected = '<object><object name="organization"><string name="name">Securin</string><string name="type">Inc</string><number name="building_number">4</number><number name="floating">-17.4</number><null name="null_test" /></object><boolean name="security_related">True</boolean><array name="array_example0"><string>red</string><string>green</string><string>blue</string><string>black</string></array><array name="array_example1"><number>1</number><string>red</string><array><object><boolean name="nested">True</boolean></object></array><object><boolean name="obj">False</boolean></object></array></object>'
    assert(xml==expected)

print("Running tests...")
test_values()
test_lists()
test_securin_example()
print("Everything passed")