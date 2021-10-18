from requests_html import HTMLSession
from bs4 import BeautifulSoup

appointment_types = {
    'PERMIT': 15,
    'NON-CDL-KNOWLEDGE-TESTING': 19,
    'KNOWLEDGE-TESTING': 17
}

locations = {
    'Bakers Basin': 186,
    'Bayonne': 187,
    'Camden': 189,
    'Cardiff': 208,
    'Delanco': 191,
    'Eatontown': 192,
    'Edison': 194,
    'Elizabeth': 264,
    'Flemington': 195,
    'Freehold': 197,
    'Lodi': 198,
    'Newark': 200,
    'North Bergen': 201,
    'Oakland': 203,
    'Paterson': 204,
    'Rahway': 206,
    'Randolph': 207,
    'Rio Grande': 188,
    'Salem': 190,
    'South Plainfield': 193,
    'Toms River': 196,
    'Vineland': 199,
    'Wayne': 202,
    'West Deptford': 205
}

# order by priority
check_locations = ['Newark', 'Lodi', 'Wayne', 'Eatontown']
check_appointment_type = 'PERMIT'

def get_soup():
    session = HTMLSession()
    response = session.get("https://telegov.njportal.com/njmvc/AppointmentWizard/15")
    response.html.render()
    return BeautifulSoup(response.html.html, 'html.parser')

def get_location_divs():
    location_divs = []
    soup = get_soup()
    appoint_type_id = str(appointment_types[check_appointment_type])
    for location in check_locations:
        location_id = str(locations[location])
        location_div = soup.find(id="dateText" + location_id + appoint_type_id)
        location_divs.insert(location_div)

    return location_divs



get_location_divs()