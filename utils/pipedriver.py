import requests

from .settings import get_token

BASE_URL = 'https://reddirtoutdoorequipment.pipedrive.com/api/v1'
API_TOKEN = get_token()


def create_person(payload: dict) -> dict:
    ''' Create person and return person data 
    
    `payload` properties
    - name: str (required)
    - owner_id: int
    - org_id: int
    - email: list
    - primary_email: str
    - phone: list
    - visible_to: int
    - marketing_status: str
    - add_time: str (format: YYYY-MM-DD HH:MM:SS)
    '''
    url = f'{BASE_URL}/persons?api_token={API_TOKEN}'
    r = requests.post(url, json=payload)
    if r.status_code == 201:
        return r.json()['data']
    else:
        raise Exception('Error creating person', r.json())
    

def create_lead(payload: dict) -> dict:
    ''' Create lead and return lead data
    
    `payload` properties:
    - title: str (required)
    - owner_id: int
    - label_ids: list
    - person_id: int
    - org_id: int
    - value: int
    - expected_close_date: str (format: YYYY-MM-DD)
    - visible_to: int
    - was_seen: bool
    '''
    url = f'{BASE_URL}/leads?api_token={API_TOKEN}'
    r = requests.post(url, json=payload)
    if r.status_code == 201:
        return r.json()['data']
    else:
        raise Exception('Error creating lead', r.json())
    
    
def create_note(payload: dict) -> dict:
    ''' Create note and return note data 
    
    `payload` properties
    - content: str (required)
    - lead_id: int 
    - person_id: int
    - org_id: int
    - user_id: int
    - add_time: str (format: YYYY-MM-DD HH:MM:SS)
    - pinned_to_lead_flag: bool
    - pinned_to_deal_flag: bool
    - pinned_to_organization_flag: bool
    - pinned_to_person_flag: bool
    
    '''
    url = f'{BASE_URL}/notes?api_token={API_TOKEN}'
    r = requests.post(url, json=payload)
    if r.status_code == 201:
        return r.json()['data']
    else:
        raise Exception('Error creating note', r.json())