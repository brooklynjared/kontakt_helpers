# Tests for the convert MIDI notes function

import pytest

from convert_midi_notes import num_to_note, note_to_num

#  ----- Tests for num_to_note -----

# Test ints in and out of range
def test_num_to_note_int():
    assert num_to_note(60) == "C3"
    assert num_to_note(0) == "C-2"
    assert num_to_note(127) == "G8"

    with pytest.raises(ValueError):
        num_to_note(400)
    with pytest.raises(ValueError):
        num_to_note(-64)

# Test inputs types
def test_num_to_note_type():
    with pytest.raises(TypeError):
        num_to_note('cat')
    with pytest.raises(TypeError):
        num_to_note(6.735)



# ----- Tests for note_to_num -----

# Test inputs for validity
def test_note_to_num():
    assert note_to_num('C-2') == 0
    assert note_to_num('Db3') == 61
    assert note_to_num('F#2') == 54
    with pytest.raises(ValueError):
        note_to_num('C')


# Test input types
def test_note_to_num_type():
    with pytest.raises(TypeError):
        note_to_num(7)
    with pytest.raises(TypeError):
        note_to_num(['C', 'C#', 'G'])        

