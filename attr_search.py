
def attr_search(obj, search):
    attr_list = dir(obj)
    result = []
    for attr in attr_list:
        if attr.find(search) != -1:
            result.append(attr)
    return result

