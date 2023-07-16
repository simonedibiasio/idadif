import re
from argparse import ArgumentParser


def patch(binary, dif, revert):
    with open(binary, "rb") as b:
        code = b.read()

    with open(dif, "r") as d:
        dif = d.read()

    m = re.findall("([0-9a-fA-F]+): ([0-9a-fA-F]+) ([0-9a-fA-F]+)", dif)
    for offset, orig, new in m:
        offset, orig, new = int(offset, 16), int(orig, 16), int(new, 16)
        if revert:
            if code[offset] == new:
                code = code[:offset] + orig.to_bytes(1, "little") + code[offset+1:]
            else:
                raise Exception(f"{binary}[{hex(offset)}] == {hex(code[offset])} != {hex(new)}")
        else:
            if code[offset] == orig:
                code = code[:offset] + new.to_bytes(1, "little") + code[offset+1:]
            else:
                raise Exception(f"{binary}[{hex(offset)}] == {hex(code[offset])} != {hex(orig)}")

    with open(binary, "wb") as b:
        b.write(code)


def main(args):
    if args.revert:
        print(f"Reverting patch {args.dif} on binary {args.binary}")
    else:
        print(f"Patching binary {args.binary} with {args.dif}")

    try:
        patch(args.binary, args.dif, args.revert)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = ArgumentParser(description="IDA .dif patcher")
    parser.add_argument("--binary", dest="binary", type=str, help="binary file path", required=True)
    parser.add_argument("--dif", dest="dif", type=str, help=".dif file path", required=True)
    parser.add_argument("--revert",dest="revert", action="store_true", help="Revert the patch", default=False)
    args = parser.parse_args()
    main(args)
