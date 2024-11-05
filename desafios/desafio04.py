a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a),
      '\nSó tem espaços?', a.isspace(),
      '\nÉ um número?',a.isnumeric(), 
      '\nÉ alfabético?', a.isalpha(), 
      '\nÉ alfanúmerico?', a.isalnum(), 
      '\nEstá em maiúsculas?', a.isupper(), 
      '\nEstá em minúsculas?', a.islower(), 
      '\nEstá capitalizada', a.istitle())