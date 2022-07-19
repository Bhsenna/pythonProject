import sqlite3

conexao = sqlite3.connect('banco pokemon.db')
cursor = conexao.cursor()


def criar():
    nome = input('Digite o nome: ')
    tipo = input('Digite o tipo: ')
    pokedex = input('Digite o Id da Pokedex: ')
    level = int(input('Digite o Level: '))
    cursor.execute('INSERT INTO lista_pokemons (nome, tipo, pokedex, Level)'
                   'VALUES(?,?,?,?)', (nome, tipo, pokedex, level))


def evoluir():
    nome = input('Qual o pokemon que deseja evoluir: ')
    level = cursor.execute('SELECT Level FROM lista_pokemons WHERE nome=?', (nome,)).fetchone()[0]
    new_level = level + 1
    cursor.execute('UPDATE lista_pokemons SET Level=? WHERE nome=?', (new_level, nome))
    print(f'{nome} subiu para o nível {new_level}!')


def editar():
    id = int(input('Id (posição) do pokemon: '))
    nome = input('Digite o novo nome: ')
    tipo = input('Digite o novo tipo: ')
    pokedex = input('Digite o novo Id da Pokedex: ')
    level = int(input('Digite o novo Level: '))
    cursor.execute('UPDATE lista_pokemons SET nome=?, tipo=?, pokedex=?, Level=? WHERE id=?', (nome, tipo, pokedex, level, id))


def listar():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'{pokemon[0]} - {pokemon[1]} - {pokemon[2]} - {pokemon[3]} - {pokemon[4]}')


def deletar():
    nome = input('Qual o pokemon que deseja APAGAR DA EXISTENCIA: ')
    if input(f'Deseja deletar {nome}? Essa ação é irreversível\n').lower() == 's':
        cursor.execute('DELETE FROM lista_pokemons WHERE nome=?', (nome,))
        print(f'{nome} foi deletado')


acoes = {'1': criar, '2': evoluir, '3': editar, '4': listar, '5': deletar}
while True:
    acao = input('Você deseja:\n'
                 '[1] Adicionar um Pokemon\n'
                 '[2] Evoluir um Pokemon\n'
                 '[3] Editar um Pokemon\n'
                 '[4] Listar os Pokemons\n'
                 '[5] Deletar um Pokemon\n').strip()
    acoes[acao]()
    conexao.commit()
    if input('Deseja parar? ').lower() == 's':
        break

cursor.close()
conexao.close()