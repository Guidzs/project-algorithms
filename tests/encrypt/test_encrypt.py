from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 'trybe')

    assert encrypt_message('trybe', 3) == 'yrt_eb'
    assert encrypt_message('trybe', 2) == 'eby_rt'
    assert encrypt_message('trybe', 6) == 'ebyrt'
