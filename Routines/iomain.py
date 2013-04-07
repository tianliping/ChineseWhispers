'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

from graph import Graph
from cluster import Cluster
from graphmanip import *
from ioaux import file_input_test_data as input_from_file

if __name__ == '__main__':
    '''n = raw_input()
    g = Graph()
    lclusters = []
    for i in range(n):
        l = raw_input().split()
        length = len(l)
        node_name = l[0]
        #node_edges = 
        node_nbrs = l[1:]
        g.create_node(node_name)
        g.graf.add_weighted_edges_from((node_name, nbr, 1) for nbr in node_nbrs)
        c = Cluster(ID = g.graf.node[node_name]['CLID'])
        c.add_node(node_name)
        #c.add_node(g.graf.node[node_name]['label'])
        lclusters.append(c)'''
    g = Graph()
    g = input_from_file()
    clustersli = []
    for node_name in g.nodes():
        c = Cluster(ID = get_max_weighted_clusters(g, node_name))
        c.add_node(node_name)
        change_node_cluster(g, node_name, c.label)
        clustersli.append(c)
    