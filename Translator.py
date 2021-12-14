import sys

import requests

from bs4 import BeautifulSoup

languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
             'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']


def checking_language(language):
    if language in languages:
        return language
    else:
        print(f"Sorry, the program doesn't support {language}")
        exit()


language_from = checking_language(sys.argv[1])
if sys.argv[2] == 'all':
    languages.remove(language_from)
    languages_to = [language for language in languages]
else:
    languages_to = checking_language(sys.argv[2])
word = sys.argv[3]

with open(f'{word}.txt', mode='w', encoding='utf-8') as file:
    session = requests.Session()
    if sys.argv[2] == 'all':
        for language_to in languages_to:
            url = f"https://context.reverso.net/translation/{language_from}-{language_to}/{word}"
            try:
                request = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            except Exception:
                print('Something wrong with your internet connection')
            else:
                soup = BeautifulSoup(request.text, 'html.parser')
                try:
                    examples = soup.select_one('#examples-content').select('.example')
                except AttributeError:
                    print(f"Sorry, unable to find {word}")
                    exit()
                else:
                    try:
                        translations = soup.select_one('#translations-content').select('a')
                    except AttributeError:
                        print(f"Sorry, unable to find {word}")
                        exit()
                    else:
                        result = '\n'.join([language_to + ' Translations:',
                                            str.strip(translations[0].text) + '\n',
                                            language_to + ' Examples:',
                                            str.strip(examples[0].select('.text')[0].text) + ':',
                                            str.strip(examples[0].select('.text')[1].text) + '\n\n'])

                        print(result, file=file, sep='\n', flush=True)
                        print(result)
    else:
        url = f"https://context.reverso.net/translation/{language_from}-{languages_to}/{word}"
        try:
            request = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        except Exception:
            print('Something wrong with your internet connection')
        else:
            soup = BeautifulSoup(request.text, 'html.parser')
            try:
                examples = soup.select_one('#examples-content').select('.example')
            except AttributeError:
                print(f"Sorry, unable to find {word}")
                exit()
            else:
                try:
                    translations = soup.select_one('#translations-content').select('a')
                except AttributeError:
                    print(f"Sorry, unable to find {word}")
                    exit()
                else:
                    result = '\n'.join([languages_to + ' Translations:',
                                        str.strip(translations[0].text) + '\n',
                                        languages_to + ' Examples:',
                                        str.strip(examples[0].select('.text')[0].text) + ':',
                                        str.strip(examples[0].select('.text')[1].text) + '\n\n'])
                    print(result)
