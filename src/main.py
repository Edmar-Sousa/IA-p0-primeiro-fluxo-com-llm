import os

from dotenv import load_dotenv

from src.app.app import App
from src.app.utils import check_env_vars_is_defined
from src.app.exception import EnvironmentVariablesError


def main() -> None:
    load_dotenv()

    try:
        check_env_vars_is_defined()

        app = App(os.getenv('LLM_PROVIDER'))
        app.process_user_message()

    except EnvironmentVariablesError as err:
        print(f'{str(err)}: {err.var_name}')


if __name__ == '__main__':
    main()