class personagem:
    def __init__(self, nome, idade, classe):
        self.nome_personagem = nome
        self.idade_personagem = idade
        self.classe_personamegm = classe
    def classeAtaque(self):
        global ataque
        
        if self.classe_personamegm == "Mago":
            ataque = "Mágia"
            print(self.classe_personamegm + " atacou usando %s"%ataque)
        elif self.classe_personamegm == "Guerreiro":
            ataque = "Espada"
            print(self.classe_personamegm + " atacou usando %s"%ataque)
        elif self.classe_personamegm == "Monge":
            ataque = "Artes Maciais"
            print(self.classe_personamegm + " atacou usando %s"%ataque)
        else:
            ataque = "Shuriken"
            print(self.classe_personamegm + " atacou usando %s"%ataque)

        
classe_tipo = ['Mago','Guerreiro','Monge', 'Ninja']

name = input("Seu nome: ")
idade1 = input("Sua idade: ")
classe1 = int(input("\nDigite o número da respectiva classe \n\n1: Mago \n2: Guerreiro \n3: Monge \n4: Ninja \n"))

if classe1 < 1 or classe1 > 4:
    while classe1 < 1 or classe1 > 4:
        print("Não pode!")
        classe1 = int(input("Digite o número da respectiva classe \n1: Mago \n2: Guerreiro \n3: Monge \n4: Ninja \n"))

classe_real = classe_tipo[classe1 - 1]

informações = personagem(name,idade1,classe_real)

informações.classeAtaque()

