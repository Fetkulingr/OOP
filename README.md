Данный репозиторий создан для изучения объектно-ориентированное программирование в python
Модуль class_computer.py Данный модуль демонстрирует применение основных принципов объектно-ориентированного программирования (ООП) при работе с базой данных SQLite.

Ключевые аспекты ООП, которые модуль демонстрирует:

1. Класс `Computer`: В этом классе определены характеристики и методы, относящиеся к компьютеру. Атрибуты `cpu`, `ram`, `hdd` и `hdd_type` представляют информацию о процессоре, оперативной памяти, жестком диске и его типе, соответственно. Также имеется атрибут `conn`, который представляет соединение с базой данных SQLite.

2. Метод `__init__(self)`: Этот метод выполняется при создании экземпляра класса `Computer`. Он инициализирует атрибуты класса и устанавливает соединение с базой данных.

3. Метод `create_table(self)`: Этот метод создает таблицу "computers" в базе данных SQLite, если она ещё не существует. Он использует SQL-запрос для создания таблицы с необходимыми столбцами.

4. Метод `get_user_input(self)`: Этот метод позволяет пользователю вводить информацию о компьютере, такую как модель процессора, объем оперативной памяти, объем жесткого диска и тип жесткого диска. Он использует словарь `cpu_options` для предоставления пользователю вариантов моделей процессоров и обрабатывает пользовательский ввод.

5. Метод `is_input_correct(self)`: Этот метод проверяет, все ли необходимые атрибуты класса `Computer` были заполнены. Если хотя бы один из них отсутствует, метод возвращает `False`, иначе `True`.

6. Метод `save_to_database(self)`: Этот метод выполняет сохранение информации о компьютере в базу данных. Он использует SQL-запрос `INSERT INTO` для добавления данных в таблицу "computers". Переданные данные вставляются в запрос через параметры, чтобы предотвратить SQL-инъекции.

Использование этого модуля позволяет пользователям вводить информацию о компьютере и сохранять ее в базе данных SQLite. Модуль демонстрирует принцип инкапсуляции. Класс Computer инкапсулирует данные компьютера (cpu, ram, hdd, hdd_type) и методы работы с ними (create_table, get_user_input, is_input_correct, save_to_database). Это означает, что данные и методы класса Computer скрыты от прямого доступа извне, и взаимодействие с ними происходит через публичный интерфейс класса (методы get_user_input и save_to_database), что способствует защите и контролю над данными.
