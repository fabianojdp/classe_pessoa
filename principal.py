from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('222.555.333-77', nome='Golias', idade=35)

print(a.getCPF())
print(a.getNome())
print(a.getIdade())

# pula uma linha
print ('\n')

b = PessoaJuridica('00.999.999/0001-99', nome='Empresa Y', idade=75)

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())

# pula uma linha
print ('\n')     
