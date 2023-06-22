# Курсовой проект по ООП “Парсер вакансий”

Представленная программа позволяет скачать вакансии с сайтов hh.ru и superjob.ru, используя предоставляемый API этих
сайтов.
Скаченные вакансии сохраняются в файл 'vacancies.json' и их можно отсортировать, вывести топ N вакансий по зарплате.

## Требования

Все необходимые зависимости указаны в файле 'pyproject.toml'. Для их установки следует выполнить команду poetry install
и все модули будут установлены.

## Содержимое программы

Программа состоит из файлов с расширением .py, которые выполняют следующие задачи:

- head_hunter_api.py - подключается к API сайта и загружает данные о вакансии по полю "Название вакансии"
- super_job_api.py - подключается к API сайта и загружает данные о вакансии по полю "Название вакансии"
- vacancy.py - представляет вакансии.
- json_saver.py - записывает вакансии в JSON-файл.
- utils.py - выполняет вспомогательные задачи

## Работа программы

В начале работа программа приветствует пользователя и предлагает ввести вакансию.
После ввода вакансии (например: "python") программа предложить выбрать платформы для поиска: HeadHunter, SuperJob или
все
представленные.
Выбрав платформу для поиска идет сбор вакансий из указанных платформ.
После успешного завершения поиска программа предложит указать навыки для фильтрации вакансий и кол-во вакансий для
показа. (например, навык: "git", кол-во вакансий: "5").
После сбора уточняющих данных от пользователя, программа выведет в консоль искомые вакансии либо выведет сообщение об
отсутствии вакансий по заданным параметрам.
