"""
Current real estate markets we're supporting
ID's are coming from `https://redfin-com-data.p.rapidapi.com/properties/auto-complete?query=<city_name>`
    -> in <city_name>, replace spaces (' ') with %20
    -> EX: San%20Diego
    -> Using 1st ID found in result string
"""

real_estate_markets = [
    {'name': 'New York', 'id': '6_30749'},
    {'name': 'Chicago', 'id': '6_29470'},
    {'name': 'Houston', 'id': '6_8903'},
    {'name': 'Los Angeles', 'id': '6_11203'},
    {'name': 'St. Petersburg', 'id': '6_16164'},
    {'name': 'Jacksonville', 'id': '6_8907'},
    {'name': 'New Orleans', 'id': '6_14233'},
    {'name': 'Phoenix', 'id': '6_14240'},
    {'name': 'Detroit', 'id': '6_5665'},
    {'name': 'Mesa', 'id': '6_11736'},
    {'name': 'Miami', 'id': '6_11458'},
    {'name': 'Minneapolis', 'id': '6_10943'},
    {'name': 'Cincinnati', 'id': '6_3879'},
    {'name': 'San Diego', 'id': '6_16904'},
    {'name': 'Bakersfield', 'id': '6_953'},
    {'name': 'San Francisco', 'id': '6_17151'},
    {'name': 'Nashville', 'id': '6_13415'},
    {'name': 'Sacramento', 'id': '6_16409'},
    {'name': 'Atlanta', 'id': '6_30756'},
    {'name': 'Las Vegas', 'id': '6_10201'},
    {'name': 'Charlotte', 'id': '6_3105'},
    {'name': 'Memphis', 'id': '6_12260'},
    {'name': 'Greensboro', 'id': '6_7161'},
    {'name': 'Fresno', 'id': '6_6904'},
    {'name': 'Hialeah', 'id': '6_7649'},
    {'name': 'Louisville', 'id': '6_12262'},
    {'name': 'San Antonio', 'id': '6_16657'},
    {'name': 'Durham', 'id': '6_4909'},
    {'name': 'Seattle', 'id': '6_16163'},
    {'name': 'Colorado Springs', 'id': '6_4147'},
    {'name': 'Philadelphia', 'id': '6_15502'},
    {'name': 'Richmond', 'id': '6_17149'},
    {'name': 'Columbus', 'id': '6_4664'},
    {'name': 'Gilbert', 'id': '6_6998'},
    {'name': 'Dallas', 'id': '6_30794'},
    {'name': 'Indianapolis', 'id': '6_9170'},
    {'name': 'San Jose', 'id': '6_17420'},
    {'name': 'Orlando', 'id': '6_13655'},
    {'name': 'Fort Wayne', 'id': '6_6438'},
    {'name': 'Boise', 'id': '6_2287'},
    {'name': 'Scottsdale', 'id': '6_16660'},
    {'name': 'Oklahoma City', 'id': '6_14237'},
    {'name': 'Tampa', 'id': '6_18142'},
    {'name': 'Austin', 'id': '6_30818'},
    {'name': 'Henderson', 'id': '6_8147'},
    {'name': 'Denver', 'id': '6_5155'},
    {'name': 'Omaha', 'id': '6_9417'},
    {'name': 'Tucson', 'id': '6_19459'},
    {'name': 'Fort Worth', 'id': '6_30827'},
    {'name': 'Lancaster', 'id': '6_10233'}
]

ISO8601 = "%Y-%m-%dT%H:%M:%SZ"

NUMBER_OF_PROPERTIES_PER_SYNAPSE = 100
