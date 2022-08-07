from curses.ascii import isdigit
import pytest
import findstring
import uni

def test_ispresent():
     assert findstring.ispresent('A1')
    
def test_nodigit():
    assert(findstring.nodigit('BR'))