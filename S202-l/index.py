from graph_database import Graph
import os

os.system('cls' if os.name == 'nt' else 'clear')

graph = Graph(uri='bolt://18.208.180.245:7687', user='neo4j',
              password='warning-evacuations-abrasive')


def create_node():
    query = [
        'CREATE(p1{nome: "Túlio", idade: 16, sexo: "M"})'
        'CREATE(p2{nome: "Ana", idade: 23, sexo: "F"})'
        'CREATE(p3{nome: "Carla", idade: 22, sexo: "F"})'
        'CREATE(p4{nome: "Rodrigo", idade: 17, sexo: "M"})'
        'CREATE(p5{nome: "Vinícius", idade: 36, sexo: "M"})'
        'CREATE(p6{nome: "Jaqueline", idade: 38, sexo: "F"})'
        'CREATE(p7{nome: "Lucas", idade: 44, sexo: "M"})'
        'CREATE(p8{nome: "Fernanda", idade: 19, sexo: "F"})'
        'CREATE(p9{nome: "Pedro", idade: 24, sexo: "M"})'
        'CREATE(p10{nome: "Raquel", idade: 41, sexo: "F"})'

        'CREATE(f1{titulo:"Johnny English 3.0",generos:["Comédia","Ação","Sátiras"]})'
        'CREATE(f2{titulo:"Debi & Lóide - Dois Idiotas em Apuros",generos:["Comédia","Clássicos"]})'
        'CREATE(f3{titulo:"Golpe Baixo",generos:["Comédia","Esportes"]})'
        'CREATE(f4{titulo:"Professor Peso Pesado",generos:["Comédia","Esportes","Para a família toda"]})'
        'CREATE(f5{titulo:"Jumanji: Bem-vindo à Selva",generos:["Comédia","Ação","Para a família toda"]})'
        'CREATE(f6{titulo:"Segurança de shopping",generos:["Comédia","Ação"]})'
        'CREATE(f7{titulo:"Cada um tem a Gêmea que Merece",generos:["Comédia"]})'

        'CREATE(s1{titulo:"Modern Family",generos:["Comédia","Sitcoms","EUA"]})'
        'CREATE(s2{titulo:"Brooklin Nine-Nine",generos:["Comédia","Crime","Sitcoms","EUA"]})'
        'CREATE(s3{titulo:"The Good Place",generos:["Comédia","EUA","Sitcoms"]})'
        'CREATE(s4{titulo:"Atypical",generos:["Comédia","Teen","Drama","EUA"]})'
        'CREATE(s5{titulo:"Lupin",generos:["Comédia","Mistério","Crime","Francês","Drama","Ação"]})'
        'CREATE(s6{titulo:"Sex Education",generos:["Comédia","Teen","Drama","Britânico"]})'
        'CREATE(s7{titulo:"Big Mouth",generos:["Comédia","Sitcoms","EUA"]})'
    ]
    for q in query:
        graph.write(query=q)


def create_relationship():
    query = [

        'MATCH (p{nome: "Túlio"}), (n1{titulo: "The Good Place" }) CREATE(p)-[:ASSISTIU] -> (n1)',
        'MATCH (p{nome: "Túlio"}), (n2{titulo: "Golpe Baixo" }) CREATE(p)-[:ASSISTIU] -> (n2)',
        'MATCH (p{nome: "Túlio"}), (n3{titulo: "Jumanji: Bem-vindo à Selva" }) CREATE(p)-[:ASSISTIU] -> (n3)',

        'MATCH (p{nome: "Ana"}), (n4{titulo: "Atypical" }) CREATE(p)-[:ASSISTIU] -> (n4)',
        'MATCH (p{nome: "Ana"}), (n5{titulo: "The Good Place" }) CREATE(p)-[:ASSISTIU] -> (n5)',
        'MATCH (p{nome: "Ana"}), (n6{titulo: "Professor Peso Pesado" }) CREATE(p)-[:ASSISTIU] -> (n6)',

        'MATCH (p{nome: "Carla"}), (n7{titulo: "Atypical" }) CREATE(p)-[:ASSISTIU] -> (n7)',
        'MATCH (p{nome: "Carla"}), (n8{titulo: "Lupin" }) CREATE(p)-[:ASSISTIU] -> (n8)',
        'MATCH (p{nome: "Carla"}), (n9{titulo: "Johnny English 3.0" }) CREATE(p)-[:ASSISTIU] -> (n9)',

        'MATCH (p{nome: "Rodrigo"}), (n10{titulo: "Modern Family" }) CREATE(p)-[:ASSISTIU] -> (n10)',
        'MATCH (p{nome: "Rodrigo"}), (n11{titulo: "Debi & Lóide - Dois Idiotas em Apuros" }) CREATE(p)-[:ASSISTIU] -> (n11)',
        'MATCH (p{nome: "Rodrigo"}), (n12{titulo: "Jumanji: Bem-vindo à Selva" }) CREATE(p)-[:ASSISTIU] -> (n12)',

        'MATCH (p{nome: "Vinícius"}), (n13{titulo: "Segurança de shopping" }) CREATE(p)-[:ASSISTIU] -> (n13)',
        'MATCH (p{nome: "Vinícius"}), (n14{titulo: "Debi & Lóide - Dois Idiotas em Apuros" }) CREATE(p)-[:ASSISTIU] -> (n14)',
        'MATCH (p{nome: "Vinícius"}), (n15{titulo: "Cada um tem a Gêmea que Merece" }) CREATE(p)-[:ASSISTIU] -> (n15)',

        'MATCH (p{nome: "Jaqueline"}), (n16{titulo: "Brooklin Nine-Nine" }) CREATE(p)-[:ASSISTIU] -> (n16)',
        'MATCH (p{nome: "Jaqueline"}), (n17{titulo: "Modern Family" }) CREATE(p)-[:ASSISTIU] -> (n17)',
        'MATCH (p{nome: "Jaqueline"}), (n18{titulo: "Big Mouth" }) CREATE(p)-[:ASSISTIU] -> (n18)',

        'MATCH (p{nome: "Jaqueline"}), (n25{titulo: "Lupin" }) CREATE(p)-[:ASSISTIU] -> (n25)',

        'MATCH (p{nome: "Lucas"}), (n19{titulo: "Big Mouth" }) CREATE(p)-[:ASSISTIU] -> (n19)',
        'MATCH (p{nome: "Lucas"}), (n20{titulo: "Golpe Baixo" }) CREATE(p)-[:ASSISTIU] -> (n20)',
        'MATCH (p{nome: "Lucas"}), (n21{titulo: "Johnny English 3.0" }) CREATE(p)-[:ASSISTIU] -> (n21)',

        'MATCH (p{nome: "Pedro"}), (n22{titulo: "Professor Peso Pesado" }) CREATE(p)-[:ASSISTIU] -> (n22)',

        'MATCH (p{nome: "Raquel"}), (n23{titulo: "The Good Place" }) CREATE(p)-[:ASSISTIU] -> (n23)',
        'MATCH (p{nome: "Raquel"}), (n24{titulo: "Segurança de shopping" }) CREATE(p)-[:ASSISTIU] -> (n24)',

    ]
    for q in query:
        graph.write(query=q)


def read(qr):
    read = graph.read(qr)
    for r in read:
        print(r)


def update():
    qr = '''
        MATCH (p)-[a:ASSISTIU]->(n)
            SET a.quando = '10/06/2021'
            RETURN p.nome as Usuário , n.titulo as Título , a.quando as Quando_assistiu
        '''
    graph.execute_query(qr)
    read(qr)

def show():
    qr = '''
        MATCH (p)-[a:ASSISTIU]->(n)
        RETURN n.titulo, COLLECT(p.nome)
        '''
    graph.execute_query(qr)
    read(qr)

def clear():
    graph.execute_query("MATCH(n) DETACH DELETE n;")


def main():
    clear()
    create_node()
    create_relationship()
    update()
    show()


main()
