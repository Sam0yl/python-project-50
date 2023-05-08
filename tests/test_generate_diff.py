from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import parse_file_by_type


diff = ''
with open('./tests/fixtures/diff.txt', 'r') as test_file:
    for line in test_file:
        diff += line


def test_parse_json_by_type():
    assert parse_file_by_type(
        './tests/fixtures/json/file2.json'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_parse_yaml_by_type():
    assert parse_file_by_type(
        '../python-project-50/tests/fixtures/yaml/file2.yaml'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_generate_json_diff():
    assert generate_diff(
        './tests/fixtures/json/file1.json',
        './tests/fixtures/json/file2.json'
    ) == diff


def test_generate_yaml_diff():
    assert generate_diff(
        '../python-project-50/tests/fixtures/yaml/file1.yml',
        '../python-project-50/tests/fixtures/yaml/file2.yaml'
    ) == diff
