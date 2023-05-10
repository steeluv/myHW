add_title = lambda name: name + (' Гений' if name[-1].upper() in ['А', 'Я', 'Г', 'М']
                                 else ' Сверхразум' if name[-1].upper()
                                 in ['О', 'Ь', 'Л', 'Н'] else ' Просто')
print(add_title('Саша'))
