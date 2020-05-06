import hashlib
import requests
import json

cifra = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',

decifra = ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x']

requisicao = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=ec4148788b49def646d1ab39841b6d8fd91623eb')

desafio = json.loads(requisicao.text)

print('-'*35,'Codenation','-'*35)
print('')
print('')
print('+'*29,'Conteúdo da requisição','+'*29)
print('')
print(desafio)
print('+'*80)
print('')
print('Decifrar a frase que está na em cifrado de acordo com o número_casas estipulado que indica quantas letras foram puladas para frente para gerar a frase cifrada')
print('')
print(desafio['cifrado'])
print('-'*80)
print('')


fraseCifrada = desafio['cifrado']


fraseDecifrada = ''

i = 0

while i < len(fraseCifrada):
        
	if fraseCifrada[i] in cifra:
        
		fraseDecifrada = fraseDecifrada + decifra[cifra.index(fraseCifrada[i])]
    
	else:
        
		fraseDecifrada = fraseDecifrada + fraseCifrada[i]
    
	i += 1

print(fraseDecifrada)
print('-'*80)
print('')
print('-'*30,'resumo_criptográfico','-'*30)
print('')

res_cript = hashlib.sha1(fraseDecifrada.encode())

print(res_cript.hexdigest())
print('-'*80)
print('')
print('-'*28,'Arquivo para ser enviado','-'*28)
print('')
desafio['decifrado'] = fraseDecifrada
desafio['resumo_criptografico'] = res_cript.hexdigest()

print(desafio)
print('')
print('+'*80)


arquivo = open('answer.json', 'w')
json.dump(desafio, arquivo, indent=4, sort_keys=False)
arquivo.close()

urlpost = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=ec4148788b49def646d1ab39841b6d8fd91623eb"
file = {"answer": open("answer.json", "rb")}
resposta = requests.post(urlpost, files=file)
print(resposta.text)






















	