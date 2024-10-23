from os import path
from json import load
from xml.dom.minidom import parseString
from dict2xml import dict_to_xml

def get_pretty_xml(xml_string):
      temp = parseString(xml_string)
      pretty_xml_string = temp.toprettyxml()
      return pretty_xml_string

def get_input_path():
      inputPath = input("Please enter the path for the input file:")
      while(path.exists(inputPath) == False):
            print("\nFile not found\n")
            inputPath = input("Please enter the path for the input file:")
      return inputPath

def get_output_path():
      outputPath = input("\nPlease enter your desired path for the output file, including the .xml extension for the file name:")
      return outputPath

print("This program converts the data from a given JSON file to XML format, which is outputted to a given file\n")

inputPath = get_input_path()

with open(inputPath) as data:
      jsonData = load(data)

xml = dict_to_xml('object', jsonData)

pretty_xml = get_pretty_xml(xml)

outputPath = get_output_path()

with open(outputPath, 'w') as f:
      f.write(pretty_xml)