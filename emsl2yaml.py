#!/usr/bin/env python3
import emsl
import argparse
import yaml
import os
from datetime import datetime


def emsl2yaml():
  """ Download emsl basis data and return yaml string of it,
  which is enhanced with metadata about the date and version
  """
  d = {
    "list": emsl.download_basisset_list(),
    "meta": {
      # UTC timestamp
      "timestamp": datetime.utcnow().isoformat(),
      # yaml format version:
      "version": "0.0.0",
    }
  }
  return yaml.safe_dump(d)

def main():
  parser = argparse.ArgumentParser(
    description="Download and convert the EMSL basis set exchange data to a yaml file")
  parser.add_argument("output", type=str, metavar="out.yaml",
                      help="Location to store the yaml file")
  args = parser.parse_args()

  _, ext = os.path.splitext(args.output)
  if not ext in [ '.yml', '.yaml' ]:
    args.output += '.yaml'

  data = emsl2yaml()
  open(args.output, "w").write(data)

if __name__ == "__main__":
  main()
