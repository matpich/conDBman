#import os
import sys
#sys.path.append(os.getcwd()[:-5]+'bin')
sys.path.append('C:\\Users\\E6430\\Documents\\python programs\\conDBman\\bin')
import pytest
import helperDBman, wrkDBman


def test_are_you_sure_YES():
    '''Assert that are_you_sure() returns True if valid value is passed'''
    assert helperDBman.areYouSure('yes')

def test_are_you_sure_NO():
    '''Assert that are_you_sure() returns False if invalid value is passed'''
    assert not helperDBman.areYouSure('qwe')

@pytest.mark.parametrize('correct_input_value', [(5001),(5),(34),(500)])
def test_try_to_int(monkeypatch,correct_input_value):
    '''try_to_int() tries to convert input value to int, if it fails it asks user for new value nad tries again'''
    monkeypatch.setattr('builtins.input', lambda x: str(correct_input_value))
    val = helperDBman.tryToInt('incorect')
    assert isinstance(val,int) and val == correct_input_value

@pytest.mark.parametrize('name, position, salary, ids, exc_out', [
    ('John', 'President', 9000,1,'ID | NAME | POSITION | SALARY\n1 | JOHN | PRESIDENT | 9000\n'),
    ('Jim', 'NoOne', 4500,2,'ID | NAME | POSITION | SALARY\n2 | JIM | NOONE | 4500\n'),
    ('James', 'foo', 0,3,'ID | NAME | POSITION | SALARY\n3 | JAMES | FOO | 0\n'),
])
def test_displayTable(capsys, name, position, salary, ids, exc_out):
    empl = wrkDBman.Worker((name, position, salary),ids)
    helperDBman.displayTable([(empl.id, empl.name.upper(), empl.position.upper(), empl.salary)])
    out,err = capsys.readouterr()
    assert out==exc_out

@pytest.mark.parametrize('info', [('foo'),('bar'),('hello'),('world')])
def test_displayInfo(capsys,info):
    helperDBman.displayInfo(info, sleep_time =0)
    out, err = capsys.readouterr()
    assert out == info+'\n'





