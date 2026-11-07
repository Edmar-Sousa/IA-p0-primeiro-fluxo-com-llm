import pytest

from unittest.mock import patch

from src.app import App
from src.exception import AppInputError


def test_app_with_message_empty():
    with patch('builtins.input', return_value=''):
        app = App('mock')

        with pytest.raises(AppInputError) as err:
            app.__get_user_input__()

        assert str(err.value) == 'Envie uma mensagem valida! Tente novamente!'
    

def test_app_with_message_spaces():
    with patch('builtins.input', return_value='        '):
        app = App('mock')

        with pytest.raises(AppInputError) as err:
            app.__get_user_input__()

        assert str(err.value) == 'Envie uma mensagem valida! Tente novamente!'

def test_app_with_valid_message():
    with patch('builtins.input', return_value='Quero uma pizza!'):
        app = App('mock')
        user_input = app.__get_user_input__()

        assert user_input == 'Quero uma pizza!'
