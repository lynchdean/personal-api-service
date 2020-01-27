import requests
import json

def next_deadline():
    """
    /api/fantasy_pl/next_deadline
    with the complete lists of people

    :return:        Timestamp for next upcoming gameweek
    """
    json_data = get_all_data()
    gw_data = get_upcoming_gw_data(json_data)

    #TODO handle exception and return error code
    return gw_data['deadline_time']


def get_all_data():
    response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').text
    return json.loads(response)


def get_upcoming_gw_data(json_data):
    events = json_data['events']
    for gw in events:
        if gw['is_next']:
            return gw
    return '{}'

if __name__ == '__main__':
    next_deadline()
