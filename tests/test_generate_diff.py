from gendiff.scripts.gendiff import generate_diff

diff = ''
with open('../python-project-50/tests/fixtures/diff.txt', 'r') as test_file:
    for line in test_file:
        diff += line


def test_generate_diff():
    assert generate_diff(
        '../python-project-50/tests/fixtures/file1.json',
        '../python-project-50/tests/fixtures/file2.json'
    ) == diff
