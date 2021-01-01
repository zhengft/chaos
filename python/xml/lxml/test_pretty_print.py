#!/usr/bin/env python3

from lxml import etree


def test_pretty_print_01():
    root = etree.Element("root")
    root.append(etree.Element("child1"))
    child2 = etree.SubElement(root, "child2")
    child3 = etree.SubElement(root, "child3")

    result = etree.tostring(root, pretty_print=True).decode()

    assert isinstance(result, str)
    expect = """
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
"""
    assert expect.lstrip() == result
