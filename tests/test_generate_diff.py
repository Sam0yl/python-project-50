import pytest
import json
from gendiff.gendiff_engine import generate_diff
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
        'tests/fixtures/json/file4.json'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_parse_yaml_by_type():
    assert parse_file_by_type(
        'tests/fixtures/yaml/file4.yaml'
    ) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


JSON_FILE1 = 'tests/fixtures/json/file1.json'
JSON_FILE2 = 'tests/fixtures/json/file2.json'
YAML_FILE1 = 'tests/fixtures/yaml/file1.yml'
YAML_FILE2 = 'tests/fixtures/yaml/file2.yaml'
STYLE_FORMAT = (
    'stylish',
    'plain',
    'json'
)


@pytest.mark.parametrize("file1,file2,style_format,expected_result", [
    (JSON_FILE1, JSON_FILE2, STYLE_FORMAT[0], stylish_diff),
    (JSON_FILE1, JSON_FILE2, STYLE_FORMAT[1], plain_diff),
    (JSON_FILE1, JSON_FILE2, STYLE_FORMAT[2], json_diff),
    (YAML_FILE1, YAML_FILE2, STYLE_FORMAT[0], stylish_diff),
    (YAML_FILE1, YAML_FILE2, STYLE_FORMAT[1], plain_diff),
    (YAML_FILE1, YAML_FILE2, STYLE_FORMAT[2], json_diff),
    pytest.param(
        JSON_FILE1,
        JSON_FILE2,
        STYLE_FORMAT[0], plain_diff, marks=pytest.mark.xfail),
    pytest.param(
        JSON_FILE1,
        JSON_FILE2,
        STYLE_FORMAT[1], json_diff, marks=pytest.mark.xfail),
    pytest.param(
        JSON_FILE1,
        JSON_FILE2,
        STYLE_FORMAT[2], stylish_diff, marks=pytest.mark.xfail),
])
def test_generate_diff(file1, file2, style_format, expected_result):
    assert generate_diff(file1, file2, style_format) == expected_result
