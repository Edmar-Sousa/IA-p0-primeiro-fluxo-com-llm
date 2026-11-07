import os

from dotenv import load_dotenv

from app import App



def check_exists_llm_api_key():
    if 'LLM_API_KEY' not in os.environ:
        raise Exception('LLM_API_KEY not defined in the environment')


def main() -> None:
    load_dotenv()
    check_exists_llm_api_key()

    app = App('gemini')
    app.process_user_message()


if __name__ == '__main__':
    main()