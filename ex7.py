import json
import yaml
from pprint import pprint as pp

with open("ex6.yml") as f:
  yaml_list = yaml.load(f)
  print "Printing Yaml list in non condensed format"
  print yaml.dump(yaml_list, default_flow_style = False)

with open("ex6.json") as f:
  print "Printing JSON list in pretty print format"
  json_list = json.load(f)
  pp(json_list)
