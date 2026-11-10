import os

from dotenv import load_dotenv

from src.app.app import App
from src.app.utils import check_env_vars_is_defined



def main() -> None:
    load_dotenv()
    check_env_vars_is_defined()

    app = App(os.getenv('LLM_PROVIDER'))
    app.process_user_message()


if __name__ == '__main__':
    main()