# 1. Анализ кейса
**Пример фрагмента кода:**
<br>**def** calculate_sum(a,b): #нет пояснения<br>
      **result** = a + b
      <br>**return** result<br>
<h6>Цели ревью:</h6> 
<ul>Обеспечение корректности типов вводных данных</ul><ul>Повышение безопасности кода при обработке возможных ошибок</ul><ul>Улучшение поддерживаемости кода </ul>

<h6>Задачи ревьюера:</h6>
<ul>Проверить реализацию валидации типов вводных аргументов </ul><ul>Проанализировать читаемость кода</ul><ul>Проверить надичие документирования функции</ul>

<h6>Цели проверки</h6>
<ul>Ясность и понятность имен переменных</ul> <ul>Документация функции и ее параметров</ul> <ul>Обработка нечисловых входных данных</ul> <ul>Возможность оптимизации алгоритма</ul>

# 2. Чек-лист ревью
<h6>Работоспособность кода - </h6>
Код функционирует коррекно, подгатавливает необходимые переменные, отправляет запрос на сайт центробанк рф, парсит файлы из xml документа и записывает их в exel таблицу

<h6>Понятность кода</h6>
Код имеет высокую степень закоментированности и корректные названия функций и переменных, для импортированных библиотек использованы сокращенные названия 

<h6>Соответсвие кода стилю оформления</h6>
Код оформлен корректно, наименования соотвествуют роду хранящихся внутри данных, а логические части программы отделены друг от друга

<h6>корректная обработка исключений</h6>
Программа не принимает никаких данных от пользователя, только необходимые данные из xml файла, таким образом программа не способна получить исключения

<h6>Безопасность</h6>
Дополнительных проверок данных обнаружено не было

<h6>Документация</h6>
Комментарии в полной мере отображают работу кода

<h6>Тестирование</h6>
тестов не было обнаружено

<h6>Соответствие PEP-8</h6>
Код соответствует требованиям PEP-8

# 2.2 План этапов
Этап      |Действия                        |Срок    |Участники
----------|--------------------------------|--------|--------------
Подготовка|Выбор кода, назначение ревьюера |45 мин  |Tech lead
Анализ    |Проверка по чек-листу           |2 часа  |Ревизор
Обсуждение|Сессия в ZOOM                   |30 минут|Автор, ревизор
