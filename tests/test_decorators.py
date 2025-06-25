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
