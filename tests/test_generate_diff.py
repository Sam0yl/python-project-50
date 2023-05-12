from gendiff.build_diff_tree import generate_diff
from gendiff.parser import parse_file_by_type


diff = ''
with open('tests/fixtures/diff.txt', 'r') as test_file:
    for line in test_file:
        diff += line


def test_parse_json_by_type():
    assert parse_file_by_type(
        'tests/fixtures/json/file2.json'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_parse_yaml_by_type():
    assert parse_file_by_type(
        'tests/fixtures/yaml/file2.yaml'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_generate_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json'
    ) == diff


def test_generate_yaml_diff():
    assert generate_diff(
        'tests/fixtures/yaml/file3.yml',
        'tests/fixtures/yaml/file4.yaml'
    ) == diff
