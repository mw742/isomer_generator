#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:59:16 2020

@author: mw742
"""
############################################################################
## Input nodes and adjacency_matrix information of a graph list
## Generate smiles for each corresponding graph
############################################################################
import sys
import numpy
import pickle
import random
import rdkit
from rdkit import Chem
from rdkit.Chem import rdmolfiles
import time


start = time.time()
def MolFromGraphs():
    readablelist = open("list.txt", "a")    
    for i in range(0, len(mollist_nodes)):
        #print(mollist_nodes)
        node_list = str(mollist_nodes.get(i))
        #print(node_list)
        adjacency_matrix = mollist_matrix.get(i)
        #print(adjacency_matrix)
        # create empty editable mol object
        mol = Chem.RWMol()
        # add atoms to mol and keep track of index
        node_to_idx = {}
        for j in range(0,len(node_list)):
            a = Chem.Atom(6)
            molIdx = mol.AddAtom(a)
            node_to_idx[j] = molIdx    
        # add bonds between adjacent atoms
        for ix, row in enumerate(adjacency_matrix):
            for iy, bond in enumerate(row):    
                # only traverse half the matrix
                if iy <= ix:
                    continue    
                # add relevant bond type (there are many more of these)
                if bond == 0:
                    continue
                elif bond == 1:
                    bond_type = Chem.rdchem.BondType.SINGLE
                    mol.AddBond(node_to_idx[ix], node_to_idx[iy], bond_type)    
        # Convert RWMol to Mol object
        mol = mol.GetMol()
        #print(mol)
        readablemol = (Chem.MolToSmiles(mol)).split(".")[-1]
        readablelist.write('\n'+readablemol)
        
###############################################################################
## Input nodes and adjacency_matrix information of a graph list, generated from 
## GENG program, translated by g6reader program and stroing in pickle_file
##
## Generate smiles for each corresponding graph
###############################################################################        
nodes = open('mollist_nodes.pkl','rb')
mollist_nodes = pickle.load(nodes)
matrix = open('mollist_matrix.pkl','rb')
mollist_matrix = pickle.load(matrix)
MolFromGraphs()

for _ in range(100000000):
    pass
end = time.time()
print(end-start)    










