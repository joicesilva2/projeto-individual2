import pandas as pd

def busca(notas, df):
    aprovacao = df[(df >= notas).all(axis=1)].index.tolist()
    if aprovacao:
        print(f'Candidatos aprovados: {aprovacao}')
    else:
        print('Nenhum candidato encontrado.')

cand = {}
while True:
    nome = input('Digite o nome: ')
    nota_do_cand = [int(input(f'Nota na etapa de {y}: ')) for y in ['entrevista', 'teste teórico', 'teste prático', 'soft skills']]
    cand[nome] = nota_do_cand
    novo_usuário = input('cadastrar novo candidato? (sim/não)')
    if novo_usuário != 'sim':
        break

df = pd.DataFrame.from_dict(cand, orient='index', columns=['entrevista', 'teste teórico', 'teste prático', 'soft skills'])
print('Lista de candidatos que realizaram as provas e suas respectivas notas:')
print(df)

notas = [int(input(f'Nota mínima para a etapa de {y}: ')) for y in ['entrevista', 'teste teórico', 'teste prático', 'soft skills']]

busca(notas, df)