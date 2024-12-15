calls = 0
def count_calls():
    global calls
    calls +=1

def string_info(string):
    info = (len(string), string.upper(), string.lower())
    count_calls()
    return info
print(string_info('Grizzly'))
print(string_info('November'))

def is_contains (string, list_to_search):
    string = str(string).upper()
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).upper() == string:
            end = True
            break
        else:
            end = False
            continue
    return end
print(is_contains('cat', ['cats', 'CatS', 'CAT']))
print(is_contains('dog', ['dogs', 'DOGS']))

print(calls)
