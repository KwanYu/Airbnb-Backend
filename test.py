import properties as properties
from neo4j import GraphDatabase
from pypher.builder import Pypher
import pytest
from py2neo import Graph


def testPy2():
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "harry"))
    res = graph.run("MATCH (n) return n")
    data = res.data()

    result_data = dict()
    for index, i in enumerate(data):
        data = dict(i['n'])
        result_data[index] = data
    print(result_data)

    pass


def test():
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "harry"))
    res = graph.run("match (l:LISTINGS),(h:HOST),(r:REVIEW) "
                    "WHERE l.city = 'Melbourne' and h.host_name = 'Eleni' and l.accommodates >= '2' " 
                    "RETURN l.accommodates,l.city,l.name, h.host_name,count(r.user_comments)")
    data = res.data()
    print(data)
    result_data = dict()
    for index, i in enumerate(data):
        data = dict(i)
        # print(data)
        result_data[index] = data
    print(result_data)
    pass



class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
        # result = tx.run("create (l:LISTINGS)"
        #                 "SET l.message = $message "
        #                 "RETURN l.message + properties(l)", message=message)
        # return result


if __name__ == "__main__":
    # greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "harry")
    # # greeter.print_greeting("begin")
    # greeter.run_query()
    # greeter.close()
    # testPy2()
    # pass
    test()
    pass
