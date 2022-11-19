from pytest import raises
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"
    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("AABBCC", "invalid_key")

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1234567890, 5)
