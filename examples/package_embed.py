import sys
sys.path.append('/usr/lib/rustpython')
from dataclasses import dataclass
from typing import Any
import encodings

__all__ = ["context"]


@dataclass
class Context:
    name: str
    something: Any


_context = Context(
    name="test name",
    something=None,
)


def context() -> Context:
    import urllib.request

    url = 'http://www.baidu.com'
    response = urllib.request.urlopen(url)
    html = response.read()

    print(html)
    return _context


if __name__ == "__main__":
    print(context().name)
