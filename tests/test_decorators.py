import pytest
from src.decorators import log

def test_log_error_console(capsys):

    @log()
    def foo(x, y):
        return  x + y

    with pytest.raises(TypeError):
        foo(2, "4")
    captured = capsys.readouterr()
    assert "foo - <class 'TypeError'> - args: (2, '4') - kwargs: {}\n\n" == captured.out


def test_log_console(capsys):

    @log()
    def foo(x, y):
        return  x + y

    captured = foo(22, 5)
    assert 27 == captured

def test_log_success_file(capsys):

    @log(filename = 'logfile.txt')
    def foo(x, y):
        return x + y

    result = foo(22, 5)
    assert result == 27

    with open('logfile.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        assert content[-1] == 'foo: OK : 27\n'