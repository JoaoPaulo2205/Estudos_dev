book = dict()

book["O jogador - Dostoiévski"] = 20.00
book["Dom Casmurro - Machado de assis"] = 49.90
book["Grokking Algorithms - Aditya"] = 68.99
book["Ana karenina"] = 2.99
book["Os irmãos karamazov - Liev Tolstoi"] = 27.50

# A partir do python 3.7 a ordem de inserção é preservada

print(book) # retorna TUDO 
print(book["Dom Casmurro - Machado de assis"]) # Retorna o valor referente a chave
print(book.items()) # Retorna os itens/ chaves e seus valores
print(book.keys()) # Retorna somente as chaves
print(book.values()) # Retorna somente os valores