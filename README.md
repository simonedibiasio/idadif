# idadif

When working with certain versions of IDA Freeware that lack the _Apply patches to input file..._ feature, it is possible to apply patches from a .dif file.

To enter patch mode in IDA, simply press F2 while in hex-view. Once you have made the necessary patches, proceed with the creation of a .dif file by following these steps: _File -> Produce File -> Create DIF file..._.

Then, to apply or revert the patch:
```
$ idadif.py --binary BINARY --dif DIF [--revert]
```

## Usage

```
usage: idadif.py [-h] --binary BINARY --dif DIF [--revert]

options:
  -h, --help       show this help message and exit
  --binary BINARY  binary file path
  --dif DIF        .dif file path
  --revert         Revert the patch
```
