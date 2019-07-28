
# Middles Editor
#### A gui editor for middle constructions
___

## Usage
```
$: middles_editor --help
usage: middles_editor_app.py [-h] -i INPUT [-o OUTPUT] [-c CONT]

This app allows the user to go over the output file of middles-tools and
select from the output all of the entries that are middles and save the final
results.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Specifies the path to the input file. This file is the
                        output of middles-tool, or the output of this file if
                        the data is marked complete.
  -o OUTPUT, --output OUTPUT
                        Specifies the path to the output file. (if this is not
                        specified, any changes made during the run will not be
                        saved)
  -c CONT, --continue CONT
                        Specifies the path to an output file that you want to
                        continue from.

```
---
## Installing
1. Clone the repository
2. Change directories so that you are inside of the project directory. run:
```
pip install --user .
```

***