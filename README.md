# Grant Deadline Board

Выводит незавершённые грантовые заявки, срок которых уже близок.

## Запуск

```bash
python src/grant_deadline_board.py due examples/sample.json --today 2026-08-18 --days 7
```

Локальный инструмент без внешних сервисов. Проверка: `python -m unittest discover -s tests -v`.
