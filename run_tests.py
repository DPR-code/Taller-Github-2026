#!/usr/bin/env python3
"""Ejecuta todos los tests.

Devuelve 0 si todo pasa y 1 si algo falla.
Es justo lo que necesita `git bisect run`.
"""

import os
import sys
import unittest
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    os.chdir(root)
    sys.path.insert(0, str(root))

    suite = unittest.defaultTestLoader.discover("tests", top_level_dir=".")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
