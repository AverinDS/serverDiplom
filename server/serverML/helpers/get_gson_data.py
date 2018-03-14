import json

NAME_DATA = "points"


def get_gson_data(request):
    json_data = json.loads(request.POST.get(NAME_DATA))  # getting form data
    json_data = json_data[NAME_DATA]
    return json_data
