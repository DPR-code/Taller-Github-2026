import unittest
from unittest.mock import Mock

from calc.clipboard import copy_to_clipboard


class TestCopyToClipboard(unittest.TestCase):
    def test_replaces_clipboard_contents(self):
        widget = Mock()
        copy_to_clipboard(widget, "42")
        widget.clipboard_clear.assert_called_once()
        widget.clipboard_append.assert_called_once_with("42")

    def test_clears_before_appending(self):
        widget = Mock()
        copy_to_clipboard(widget, "3.14")
        calls = [name for name, _args, _kwargs in widget.method_calls]
        self.assertLess(calls.index("clipboard_clear"), calls.index("clipboard_append"))

