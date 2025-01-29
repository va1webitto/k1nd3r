def hello(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    if not name.strip():
        raise ValueError("Имя не может быть пустым!!")
    return f"Привет, {name}!"