import json
import requests  # use for API call to septa
import numbers


def next_train(outgoing_station, inbound_station, num_results):
    assert type(num_results) == int, 'You must input a valid integer number.'

    url = r'http://www.septa.org/hackathon/NextToArrive/{}/{}/{}'.format(outgoing_station, inbound_station, num_results)

    # Get api json from septa website
    septa_api_request = requests.get(url)
    septa_json = json.loads(septa_api_request.text)

    # parse out specific values from json
    delay = septa_json[0]['orig_delay'].strip()
    depart_time = septa_json[0]['orig_departure_time'].strip()
    train_line = septa_json[0]['orig_line'].strip()

    # return message about next train
    if delay == 'On time':
        return 'The {} {} train is on time.'.format(depart_time, train_line)
    else:
        return 'The {} {} train is {} late!'.format(depart_time, train_line, delay)



