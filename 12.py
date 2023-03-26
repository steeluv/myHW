import request
request = input('Введите ваш запрос: ')
response = request.process_request(request)
print(response)