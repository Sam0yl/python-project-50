import json
from gendiff.build_diff_tree import generate_diff
from gendiff.parser import parse_file_by_type


stylish_diff = str()
with open('tests/fixtures/stylish_diff.txt', 'r') as test_file:
    for line in test_file:
        stylish_diff += line


plain_diff = str()
with open('tests/fixtures/plain_diff.txt', 'r') as test_file:
    for line in test_file:
        plain_diff += line


def make_json_diff():
    json_file = json.load(open('tests/fixtures/json_diff.json', 'r'))
    return json.dumps(json_file, indent=4, sort_keys=True)


json_diff = make_json_diff()


def test_parse_json_by_type():
    assert parse_file_by_type(
        'tests/fixtures/json/file2.json'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_parse_yaml_by_type():
    assert parse_file_by_type(
        'tests/fixtures/yaml/file2.yaml'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_generate_stylish_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json'
    ) == stylish_diff


def test_stylish_format_yaml_diff():
    assert generate_diff(
        'tests/fixtures/yaml/file3.yml',
        'tests/fixtures/yaml/file4.yaml'
    ) == stylish_diff


def test_plain_format_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'plain'
    ) == plain_diff


def test_plain_format_yaml_diff():
    assert generate_diff(
        'tests/fixtures/yaml/file3.yml',
        'tests/fixtures/yaml/file4.yaml',
        'plain'
    ) == plain_diff


def test_json_format_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'json'
    ) == json_diff


def test_json_format_yaml_diff():
    assert generate_diff(
        'tests/fixtures/yaml/file3.yml',
        'tests/fixtures/yaml/file4.yaml',
        'json'
    ) == json_diff


def test_fail_generate_stylish_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json'
    ) != plain_diff


def test_fail_generate_plain_json_diff():
    assert generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'plain'
    ) != stylish_diff
