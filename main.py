import requests
import datetime

SECINDAY = 86400

def getstamp(date_obj=datetime.datetime.now()):
    return(int(date_obj.timestamp() // SECINDAY * SECINDAY))

if __name__ == '__main__':
    url = 'https://api.stackexchange.com/2.3/questions'
    to_date = getstamp()
    from_date = to_date - SECINDAY
    params = {"fromdate" : str(from_date) , "todate" : str(to_date),
              "order" : "desc", "sort" : "activity", "site" : "stackoverflow"}
    response = requests.get(url,params=params)
    python_questions = []
    print(f"Всего вопросов {len(response.json()['items'])}")
    for item in response.json()['items']:
        if 'python' in item['tags']:
            python_questions.append(item['title'])
    print(f"Вопросов с тэгом 'python' - {len(python_questions)}")
    print('\n'.join(python_questions))

