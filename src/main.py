from dotenv import load_dotenv

from app.app import App
from app.utils import check_exists_llm_api_key



def main() -> None:
    load_dotenv()
    check_exists_llm_api_key()

    app = App('gemini')
    app.process_user_message()


if __name__ == '__main__':
    main()