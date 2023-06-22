from src.classes.head_hunter_api import HeadHunterAPI
from src.classes.json_saver import JSONSaver
from src.classes.super_job_api import SuperJobAPI
from src.utils.utils import filter_vacancies, sort_vacancies, \
    get_top_vacancies, find_hh_vacancies, find_sj_vacancies


def main():
    """Точка входа в программу"""
    print('Добро пожаловать в программу по поиску и фильтрации информации о вакансиях с разных платформ в России')
    while True:
        entered_name_vacancy = input('Введите название вакансии \n'
                                     'Введите "exit" для выхода из программы.\n')

        if entered_name_vacancy == 'exit':
            print('Работа программы завершена.')
            return

        if not entered_name_vacancy:
            print("Вы ничего не ввели. Повторите ввод.")
            continue

        while True:
            print('Выберите платформу для поиска:')
            choice_platform = (input('1 - HeadHunter\n2 - SuperJob\n3 - Все платформы\n\n'
                                     '0 - для ввода новой вакансии.\n'))

            if not choice_platform or choice_platform == '0':
                break
            else:
                choice_platform = int(choice_platform)

            hh_api = HeadHunterAPI()
            superjob_api = SuperJobAPI()
            json_saver = JSONSaver()

            found_hh_vacancies = []
            found_sj_vacancies = []
            found_vacancies = []

            if choice_platform in (1, 2, 3):
                print('Идет поиск и сбор вакансий, это займет некоторое время...')
                if choice_platform == 1:
                    found_hh_vacancies = find_hh_vacancies(hh_api, entered_name_vacancy)
                elif choice_platform == 2:
                    found_sj_vacancies = find_sj_vacancies(superjob_api, entered_name_vacancy)
                elif choice_platform == 3:
                    found_hh_vacancies = find_hh_vacancies(hh_api, entered_name_vacancy)
                    found_sj_vacancies = find_sj_vacancies(superjob_api, entered_name_vacancy)

                found_vacancies.extend(found_hh_vacancies)
                found_vacancies.extend(found_sj_vacancies)
                json_saver.write_vacancies(found_vacancies)

                if not found_vacancies:
                    print('Вакансий не найдено! Введите другую вакансию.')
                    break

                print(f'Поиск завершен! Найдено всего вакансий: {len(found_vacancies)}')

                while True:
                    print("Введите навыки через запятую или введите 'quit' для перехода к вводу вакансии: ")
                    entered_keywords = list(input().lower().split(','))
                    entered_keywords = set([item.strip() for item in entered_keywords])

                    top_n = input('Введите количество вакансий для вывода в топ N по зарплате: ')

                    filtered_list_vacancies = filter_vacancies(entered_keywords)

                    if not filtered_list_vacancies:
                        print('Нет вакансий, соответствующих заданным критериям. Введите другие критерии поиска.')
                    else:
                        sorted_vacancies = sort_vacancies(filtered_list_vacancies)
                        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
                        print(
                            f'Отсортированный список из {top_n} вакансий, содержащий ключевые'
                            f' слова ({entered_keywords}):')

                        for i, item in enumerate(top_vacancies, 1):
                            print(i, item)

                        print('\n', '*' * 20, '\n')

                        user_choice = input('Нажмите Enter для поиска вакансий по другим навыкам.\n'
                                            'Введите 1, чтобы перейти к выбору платформы.')

                        if user_choice:
                            break
            else:
                print('Пункты ввода не корректны! Выберите указанные пункты!')


if __name__ == '__main__':
    main()
