input_string = open("data/day_0802.txt").read()
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


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


final_result = list(['transparent'] * (width * height))
for layer in layers:
    for i in range(len(layer)):
        if final_result[i] == 'transparent':
            # print(layer[i])
            if layer[i] is '0':
                #print('This is black')
                final_result[i] = '█'
            elif layer[i] is '1':
                #print('This is white')
                final_result[i] = '0'


output_split = list(divide_chunks(final_result, width))
# print(output_split)
for row in output_split:
    row_merged = ""
    for char in row:
        row_merged = row_merged + char
    print(row_merged)
