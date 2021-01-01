#!/usr/bin/env python3

from pathlib import Path
import pytest

from ruamel.yaml import YAML
from ruamel.yaml.constructor import DuplicateKeyError


def get_current_dirpath() -> Path:
    return Path(__file__).parent.resolve()


def test_load_01():
    """
    test load success.
    """
    filepath = get_current_dirpath() / 'sample.yaml'
    yaml = YAML(typ='safe')
    result = yaml.load(filepath)

    expect = {
        'aaa': 'aaa',
        'bbb': 'bbb',
    }
    assert expect == result


def test_load_02():
    """
    test load duplicate key yaml.
    """
    filepath = get_current_dirpath() / 'sample-duplicate-keys.yaml'
    yaml = YAML(typ='safe')
    with pytest.raises(DuplicateKeyError) as wex:
        yaml.load(filepath)

    ex = wex.value
    problem = 'found duplicate key "aaa" with value "aaa" (original value: "aaa")'

    assert problem == ex.problem
