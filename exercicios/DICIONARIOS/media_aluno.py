alunos= []
aluno = {}
aluno['nome'] = str(input("Nome do aluno: "))
aluno['Média'] = float(input("Média do aluno: "))


if aluno['Média'] <= 5:
    aluno['Situação'] = "Reprovado"
    alunos.append(aluno.copy())
else:
    aluno['Situação'] = 'Aprovado'
    alunos.append(aluno.copy())

print(f'Nome do aluno: {alunos[0]['nome']}')
print(f'Média do aluno: {alunos[0]['Média']}')
print(f'Situação: {alunos[0]['Situação']}')