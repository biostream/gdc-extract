
cwlVersion: v1.0
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: gdc-extract:latest
baseCommand:
  - /opt/gdc-scan.py
  - cases
  - list

inputs:
  blank:
    type: [boolean, "null"]
outputs:
  CASE_LIST:
    type: stdout

stdout: gdc_case_scan.json