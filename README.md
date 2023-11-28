`sha256.py` is a program that prints its own hash. It does not read from its own
file or use any `eval`. It simply computes its own hash directly. It does so by
first computing its own source code as a string, and then calculating the hash
of it.

To verify:

```
dionyziz@pluto ~ $ python sha256.py
3a50ff10de6521da3e0ae3b67bbe71e8882b8faa51f3734d7845f38995ef85c5
dionyziz@pluto ~ $ sha256sum sha256.py
3a50ff10de6521da3e0ae3b67bbe71e8882b8faa51f3734d7845f38995ef85c5  sha256.py
```