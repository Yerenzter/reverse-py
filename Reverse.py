def reverse(value):
    data = ""
    value = str(value)
    for values in range(len(value)):
        result = (len(value)-values)-1
        data += value[result]

    return data
