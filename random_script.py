def reverse(x):
    output_len = len(x)
    output = [None] * output_len
    print(output, "_1")
    output_index = output_len - 1
    print(output_index, "_2")
    for c in x:
        output[output_index] = c
        print(c,"_3")
        output_index -= 1
        print(output_index,"_4")

    return ''.join(output)

obj = reverse('Hello')
print(obj)
