"""Модуль содержит декоратор log для логирования вызовов функций."""

import functools
from typing import Any
from typing import Callable
from typing import Optional


def log(
    func: Optional[Callable[..., Any]] = None,
    *,
    filename: Optional[str] = None,
) -> Any:
    """Декоратор для логирования вызовов функций.

    Использование:
        @log                          # вывод в консоль
        @log(filename="app.log")      # запись в файл

    При успехе:  "<имя> ok result: <результат>"
    При ошибке:  "<имя> error: <ТипОшибки>. Inputs: <args>, <kwargs>"

    Args:
        func:     Декорируемая функция (при @log без скобок).
        filename: Путь к файлу для логов. None — вывод в консоль.

    Returns:
        Обёрнутая функция или декоратор.
    """

    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        """Принимает функцию и возвращает обёртку с логированием."""

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Вызывает исходную функцию, логирует результат или ошибку."""
            try:
                result = fn(*args, **kwargs)
                _write(f"{fn.__name__} ok result: {result}", filename)
                return result
            except Exception as e:
                error_msg = (
                    f"{fn.__name__} error: {type(e).__name__}: {e}."
                    f" Inputs: {args}, {kwargs}"
                )
                _write(error_msg, filename)
                raise

        return wrapper

    if func is not None:
        return decorator(func)
    return decorator


def _write(message: str, filename: Optional[str]) -> None:
    """Записывает сообщение в файл (дополняя) или выводит в консоль.

    Args:
        message:  Текст лога.
        filename: Путь к файлу. Если None — print в stdout.
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
