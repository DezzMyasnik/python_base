APIKEY = '3373bf96b11f8169de9c85c56224e2134b185c192bd3dc637de8bdd06bbee6afff681620ea2382bf1a8d8'
PUBLIC_ID = 130111251

LOG_FILE_NAME = 'bot.log'
LOG_FORMAT = '%(asctime)s : %(levelname)s - %(message)s'

INTENTS = [
    {
        "name": "Дата проведения",
        "tokens": ('когда', "сколько", "дату", "дата"),
        "scenario": None,
        "answer": "Конференция продет 10-го апреля, регистрация начинается в 10 утра"
    },
    {
        "name": "Место проведения",
        "tokens": ("где", "место", "локация", "адрес", "метро"),
        "scenario": None,
        "answer": "Конференция продет в БЦ Трудагя, по адресу..., метро Метровское"
    },
    {
        "name": "Регистрация",
        "tokens": ('регистр', "добав"),
        "scenario": "registration",
        "answer": None
    }
]
SCENARIOS = {"registration":
    {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Чтобы зарегестрироваться, введите ваше имя. Оно будет написано на бейджике.",
                "failure_text": "Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "Введите email. Мы отправим на него все данные",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще",
                "handler": "handle_email",
                "next_step": "step3"
            },
            "step3": {
                "text": "Спасибо за регитсрацию, {name}! Мы отправилина {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            }
        }
    }
}

DEFAULT_ANSWER = "Не знаю как на это ответить." \
                 "Могу сказать когда и где пройдет конференция, а также зарегистировать Вас. Просто спросите"