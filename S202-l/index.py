from graph_database import Graph
import os

os.system('cls' if os.name == 'nt' else 'clear')

graph = Graph(uri='bolt://18.208.180.245:7687', user='neo4j',
              password='warning-evacuations-abrasive')


def create_node():
    query = [
        "CREATE(b1:Band{name: 'twenty one pilots', year: 2009, style: 'rock alternativo'})",
        "CREATE(a1: Album{name: 'Trench', lancado: 2018, faixas: 12})",
        "CREATE(m1: Music{name: 'Jumpsuit ', time: '4:58'})",
        "CREATE(b2: Band{name: 'Iron Maiden', year: 1975, style: 'Heavy Metal'})",
        "CREATE(a2: Album{name: 'Piece of Mind', lancado: 1983, faixas: 9})",
        "CREATE(m2: Music{name: 'The Trooper', time: '4:12'})",
        "CREATE(b3: Band{name: 'Bon Jovi', year: 1983, style: 'Rock'})",
        "CREATE(a3: Album{name: 'Crush', lancado: 2000, faixas: 13})",
        "CREATE(m3: Music{name: 'Its My Life', time: '3:45'})"
    ]
    for q in query:
        graph.write(query=q)


def create_relationship():
    query = [
        "MATCH(b1:Band{name: 'twenty one pilots'}), (a1: Album{name: 'Trench'}) CREATE(b1)-[:POSSUI] -> (a1)",
        "MATCH(a1:Album{name: 'Trench'}), (m1: Music{name: 'Jumpsuit '}) CREATE(a1)-[:TEM] -> (m1)",
        "MATCH(b2:Band{name: 'Iron Maiden'}), (a2: Album{name: 'Piece of Mind'}) CREATE(b2)-[:POSSUI] -> (a2)",
        "MATCH(a2:Album{name: 'Piece of Mind'}), (m2: Music{name: 'The Trooper'}) CREATE(a2)-[:TEM] -> (m2)",
        "MATCH(b3:Band{name: 'Bon Jovi'}), (a3: Album{name: 'Crush'}) CREATE(b3)-[:POSSUI] -> (a3)",
        "MATCH(a3:Album{name: 'Crush'}), (m3: Music{name: 'Its My Life'}) CREATE(a3)-[:TEM] -> (m3)",

        "MATCH(b1:Band{name: 'twenty one pilots'}), (b2: Band{name: 'Iron Maiden'}) CREATE(b1)-[:RELACIONAMENTO{tipo: 'forte'}] -> (b2)",
        "MATCH(b2: Band{name: 'Iron Maiden'}), (b3: Band{name: 'Bon Jovi'}) CREATE(b2)-[:RELACIONAMENTO{tipo: 'medio'}] -> (b3)",
        "MATCH(b1: Band{name: 'twenty one pilots'}), (b3: Band{name: 'Bon Jovi'}) CREATE(b1)-[:RELACIONAMENTO{tipo: 'fraco'}] -> (b3)",
    ]
    for q in query:
        graph.write(query=q)


def read():
    print(graph.read("MATCH(n) RETURN n;"))


def update():
    graph.execute_query("MATCH (n:Album {name: 'Crush2'}) SET n.name = 'Crush'")


def clear():
    graph.execute_query("MATCH(n) DETACH DELETE n;")


def main():
    clear()
    create_node()
    create_relationship()
    update()
    read()


main()
