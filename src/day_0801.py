input_string = open("data/day_0801.txt").read()
width = 25
height = 6
layer_len = width * height
most_0s = 0
most_0s_string = ''
least_0s = 150
least_0s_string = ''

layers = [(input_string[i:i+layer_len])
          for i in range(0, len(input_string), layer_len)]
for layer in layers:
    if len(layer) >= 25:
        zero_count = 0
        for i in layer:
            if i == '0':
                zero_count = zero_count + 1
        if zero_count > most_0s:
            most_0s = zero_count
            most_0s_string = layer
        if zero_count < least_0s:
            least_0s = zero_count
            least_0s_string = layer

ones_count = 0
twos_count = 0
for i in least_0s_string:
    if i == '1':
        ones_count = ones_count + 1
    if i == '2':
        twos_count = twos_count + 1

print(ones_count * twos_count)
