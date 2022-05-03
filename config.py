from dataclasses import dataclass
from environs import Env


@dataclass(frozen=True)
class Config:
    lang: str

    token: str
    main_chat: int
    admin_chat: int

    google_api_key: str
    channel_name: str
    channel_url: str
    channel_id: str
    update_interval: int

    rules_file: str
    welcome_file: str


env = Env()
env.read_env(override=True)
config = Config(
    lang=env.str("LANG", default="ru"),
    token=env.str("TOKEN"),
    main_chat=env.int("MAIN_CHAT"),
    admin_chat=env.int("ADMIN_CHAT"),
    google_api_key=env.str("GOOGLE_API_KEY"),
    channel_name=env.str("CHANNEL_NAME"),
    channel_url=env.str("CHANNEL_URL"),
    channel_id=env.str("CHANNEL_ID"),
    update_interval=env.int("UPDATE_INTERVAL"),
    rules_file=env.str("RULES_FILE"),
    welcome_file=env.str("WELCOME_FILE")
)

