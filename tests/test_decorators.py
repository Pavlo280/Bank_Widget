"""Тесты для модуля src/decorators.py."""

import pytest

from src.decorators import log

# ---------------------------------------------------------------------------
# Вспомогательные функции — декорируются здесь, чтобы не повторяться
# ---------------------------------------------------------------------------


@log
def add(a: int, b: int) -> int:
    """Складывает два числа (декоратор без скобок)."""
    return a + b


@log
def fail_no_args() -> int:
    """Всегда бросает ZeroDivisionError (декоратор без скобок)."""
    return 1 // 0


# ---------------------------------------------------------------------------
# Тесты: вывод в консоль (@log без скобок)
# ---------------------------------------------------------------------------


def test_log_success_console(capsys: pytest.CaptureFixture) -> None:
    """При успехе в stdout должна появиться строка с 'ok' и результатом."""
    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok result: 5" in captured.out


def test_log_error_console(capsys: pytest.CaptureFixture) -> None:
    """При исключении в stdout должна появиться строка с 'error'."""
    with pytest.raises(ZeroDivisionError):
        fail_no_args()

    captured = capsys.readouterr()
    assert "fail_no_args error: ZeroDivisionError" in captured.out
    assert "Inputs:" in captured.out


def test_log_error_console_shows_inputs(
    capsys: pytest.CaptureFixture,
) -> None:
    """Аргументы функции попадают в лог ошибки."""

    @log
    def divide(x: int, y: int) -> float:
        """Делит x на y."""
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "10" in captured.out
    assert "0" in captured.out


# ---------------------------------------------------------------------------
# Тест: @log(filename=None) — явный None, должен вести себя как @log
# ---------------------------------------------------------------------------


def test_log_with_explicit_none_filename(
    capsys: pytest.CaptureFixture,
) -> None:
    """@log(filename=None) выводит лог в консоль, а не в файл."""

    @log(filename=None)
    def multiply(a: int, b: int) -> int:
        """Умножает a на b."""
        return a * b

    result = multiply(3, 4)
    captured = capsys.readouterr()

    assert result == 12
    assert "multiply ok result: 12" in captured.out


# ---------------------------------------------------------------------------
# Тесты: запись в файл (@log(filename=...))
# ---------------------------------------------------------------------------


def test_log_success_file(tmp_path: pytest.TempPathFactory) -> None:
    """При успехе с filename лог пишется в файл, а не в консоль."""
    log_file = tmp_path / "success.log"  # type: ignore[operator]

    @log(filename=str(log_file))
    def greet(name: str) -> str:
        """Возвращает приветствие."""
        return f"Hello, {name}"

    result = greet("World")
    content = log_file.read_text(encoding="utf-8")

    assert result == "Hello, World"
    assert "greet ok result: Hello, World" in content


def test_log_error_file(tmp_path: pytest.TempPathFactory) -> None:
    """При исключении с filename ошибка пишется в файл."""
    log_file = tmp_path / "error.log"  # type: ignore[operator]

    @log(filename=str(log_file))
    def boom(x: int) -> int:
        """Всегда бросает ValueError."""
        raise ValueError("bad input")

    with pytest.raises(ValueError):
        boom(42)

    content = log_file.read_text(encoding="utf-8")
    assert "boom error: ValueError" in content
    assert "Inputs:" in content
    assert "42" in content


def test_log_file_appends(tmp_path: pytest.TempPathFactory) -> None:
    """Каждый вызов дописывает строку в файл, а не перезаписывает."""
    log_file = tmp_path / "append.log"  # type: ignore[operator]

    @log(filename=str(log_file))
    def inc(n: int) -> int:
        """Увеличивает n на 1."""
        return n + 1

    inc(1)
    inc(2)

    lines = log_file.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2


# ---------------------------------------------------------------------------
# Тест: декоратор сохраняет имя и docstring (functools.wraps)
# ---------------------------------------------------------------------------


def test_log_preserves_metadata() -> None:
    """functools.wraps должен сохранить __name__ и __doc__ функции."""

    @log
    def my_func() -> None:
        """Моя функция."""

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "Моя функция."
