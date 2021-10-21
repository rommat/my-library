Створити папку `tests` в ній папки `unit`, `integration` і конфігураційний файл \
`pytest.ini` з дефолтними налаштуваннями.


### --- Unit tests ---
Написати юніт тести, покрити головну частину логіки додатка (data_handlers.py).
Використовувати `unittest.mock.patch` щоб ізолювати запити в базу даних.

### --- Integration test ---
Написати хоча б інтеграційний тест на будь який із сценаріїв.
Для інтеграційних тестів створити окрему базу даних.


### --- SQL test ---
Написати тест на будь який `sql` запит (не тестувати нічого крім самого запиту і отриманих даних).
Для даного теста теж створити окрему базу. Відмітити його маркером(`pytest.mark`) `sql`.
При виконанній команди `pytest -m sql` має виконуватися тільки даний тест.

### --- Pytest Hooks ---
Зробити так щоб при виконанні команди
`pytest tests` не виконувалися тести з папки integration(всі окрім них).
Інтеграційні команди мають запускатися тільки при  додатковій опції `--integration`.

Корисні лінки:
* [pytest docs](https://docs.pytest.org/en/6.2.x/reference.html)
* [pytest_collection_modifyitems](https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.pytest_collection_modifyitems) - хук дозволяє динамічно міняти обєкти знайдених тестів
(наприклад добавити маркер `integartion`)
* [pytest_adoption](https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.pytest_addoption) - хук що дозволяє добавляти кастомні аргументи при виклику команди `pytest`
* [pytest.mark.skip](https://docs.pytest.org/en/6.2.x/reference.html#pytest.skip) - маркер що дає можливість пропустити виконання тесту
