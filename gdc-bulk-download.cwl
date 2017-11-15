
cwlVersion: v1.0
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: biostream/gdc-extract:latest
baseCommand:
  - /opt/gdc-bulk-download.py

inputs:
  DATA_TYPE:
    type: string
    inputBinding:
      position: 1
  PROJECT_ID:
    type: string
    inputBinding:
      position: 2
  OUTPUT_NAME:
    type: string
    inputBinding:
      position: 3

outputs:
  FILE:
    type: File
    outputBinding:
      glob: $(inputs.OUTPUT_NAME)

