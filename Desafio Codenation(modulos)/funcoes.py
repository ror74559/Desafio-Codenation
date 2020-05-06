
def decifrando(fraseCifrada,cifra,decifra ):

      i = 0
      Decifrada = str()
      
      while i < len(fraseCifrada):
              
      	if fraseCifrada[i] in cifra:
              
      		Decifrada = Decifrada + decifra[cifra.index(fraseCifrada[i])]
          
      	else:
              
      		Decifrada = Decifrada + fraseCifrada[i]
          
      	i += 1
      return Decifrada


def render1(x):
    print('-'*35,'Codenation','-'*35)
    print('')
    print('')
    print('+'*29,'Conteúdo da requisição','+'*29)
    print('')
    print(x)
    print('+'*80)
    print('')
    print('Decifrar a frase que está na em cifrado de acordo com o número_casas estipulado que indica quantas letras foram puladas para frente para gerar a frase cifrada')
    print('')
    print(['cifrado'])
    print('-'*80)
    print('')
    

def render2():

    print('-'*80)
    print('')
    print('-'*30,'resumo_criptográfico','-'*30)
    print('')
    

def render3():
   
    print('-'*80)
    print('')
    print('-'*28,'Arquivo para ser enviado','-'*28)
    print('')
    
##########################################################################

def render4():

   
    print('')
    print('+'*80)
    
#########################################################################