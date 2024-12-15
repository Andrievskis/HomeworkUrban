def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # не ошибка, ничего не выводит

#inner_function() #выдает ошибку: имя не
# определено (нельзя вывести внутренние значения функции снаружи)

test_function() #выводит текст из команды print