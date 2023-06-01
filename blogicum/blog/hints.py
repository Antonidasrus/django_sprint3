"""Тексты подсказок."""
help_text_dict = {
    'pub_date': 'Если установить дату и время в будущем — можно '
                'делать отложенные публикации.',
    'slug': 'Идентификатор страницы для URL; разрешены '
                'символы латиницы, цифры, дефис и подчёркивание.',
    'is_published': 'Снимите галочку, чтобы скрыть публикацию.'
}


class HelpText():
    def __init__(self) -> None:
        self.help_text = help_text_dict

    def print_hint(self, field: str) -> str:
        return self.help_text[field]
