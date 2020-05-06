import hashlib
import requests
import json
import funcoes as f


cifra = 'abcdefghijklmnopqrstuvwxyz'

decifra = 'yzabcdefghijklmnopqrstuvwx'

requisicao = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=ec4148788b49def646d1ab39841b6d8fd91623eb')

desafio = json.loads(requisicao.text)



f.render1(desafio)

fraseCifrada = desafio['cifrado']
	
fraseDecifrada = f.decifrando(fraseCifrada, cifra, decifra)

print(fraseDecifrada)



f.render2()

res_cript = hashlib.sha1(fraseDecifrada.encode())

print(res_cript.hexdigest())



f.render3()

desafio['decifrado'] = fraseDecifrada

desafio['resumo_criptografico'] = res_cript.hexdigest()

print(desafio)



f.render4()

arquivo = open('answer.json', 'w')

json.dump(desafio, arquivo, indent=4, sort_keys=False)

arquivo.close()

urlpost = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=ec4148788b49def646d1ab39841b6d8fd91623eb"

file = {"answer": open("answer.json", "rb")}

resposta = requests.post(urlpost, files=file)

print(resposta.text)






















	