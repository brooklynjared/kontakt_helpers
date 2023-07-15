# Tests for the convert MIDI notes function

import pytest

from convert_midi_notes import num_to_note

# Test ints in and out of range
def test_convert_int():
    assert num_to_note(60) == "C3"
    assert num_to_note(0) == "C-2"
    assert num_to_note(127) == "G8"

    with pytest.raises(ValueError):
        num_to_note(400)
    with pytest.raises(ValueError):
        num_to_note(-64)

# Test string and float inputs
def test_convert_type():
    with pytest.raises(TypeError):
        num_to_note('cat')
    with pytest.raises(TypeError):
        num_to_note(6.735)