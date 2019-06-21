from next_train import next_train
from send_text import send_text


outgoing_station = 'Suburban%20Station'
inbound_station = 'Ambler'
num_results = 5

message = next_train(outgoing_station, inbound_station, num_results)
send_text(message)
