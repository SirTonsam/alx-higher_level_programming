#!/usr/bin/python3.8
import dis

if __name__ == "__main__":
    module = __import__("hidden_4")
    for name in sorted(dir(module)):
        if name[0] != "_" and name[1] != "_":
            code = getattr(module, name)
            if isinstance(code, bytes):
                code = code.decode("utf-8")
                print(dis.dis(code))
            else:
                print(name)

