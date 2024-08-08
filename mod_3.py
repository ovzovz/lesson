def count_calls():
    global calls
    calls+=1
    return calls
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return (True)
    else:
        return (False)  
   
   
calls=0
print(string_info("ggdydyfRrt567") )
print(is_contains("f",["f","g,a",7]))
print(calls)





