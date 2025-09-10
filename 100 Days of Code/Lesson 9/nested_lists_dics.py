# travel_log = {
#     'France' : ['Paris', 'Lille', 'Dijon'],
#     'Germany': ['Berlin', 'Stuttgart']
# }

# print(travel_log['France'][1])  # Primero se accede al diccionario, y luego a la posicion de la lista 

# nested_list = ['A', 'B', ['C', 'D']] # Como accedo a 'D'?
# print(nested_list[2][1])

travel_log = {
    'France' : {
        "times_visited": 8, 
        'cities_visited': ['Paris', 'Lille', 'Dijon']
    },

    'Germany': {
        "times_visited": 12, 
        'cities_visited': ['Berlin', 'Stuttgart'] # Como accedo a Stuttgart?
    }
}

print(travel_log['Germany']['cities_visited'][1]) # Accedo primero al diccionario, luego al key, luego a la posicion 

