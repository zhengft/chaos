#!/usr/bin/env python3

from lxml import etree


def test_pretty_print_01():
    root = etree.Element("root")
    root.append(etree.Element("child1"))
    child2 = etree.SubElement(root, "child2")
    child3 = etree.SubElement(root, "child3")

    r0 = etree.tostring(root, pretty_print=True)
    assert isinstance(r0, bytes)

    r1 = r0.decode()
    assert isinstance(r1, str)
    expect = """
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
"""
    assert expect.lstrip() == r1
