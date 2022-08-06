#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:18:18 2022

@author: ccye
"""

# Define types of model cells here
# so that instances (objects based on them)
# can be created in main.py after loading in
# this file

# The classes defined below include:
# reduced_cell_model: the pyramidal cell model
# stimcell: an artificial cell that synapses onto
#            the pyramidal cell and that can spike
#            during the simulation, activating a 
#            postsynaptic current in the pyramidal cell.
#            Note: Excitatory and inhibitory stimulating
#            cells can both be created from this cell class.
#            The difference is which synapse on the post-
#            synaptic pyramidal cell you connect them to

from neuron import h
import matplotlib.pyplot as plt
import math
  
class stimcell():
    def __init__(self, noise):
        self.is_art=1
        self.noiseFromRandom=0
        self.gid=[]
        self.x=0
        self.y=0
        self.z=0

        pp = h.MyNetStim(.5)
        
        pp.interval = 1000/8 # Gives an 8 Hz rhythm with an interval of 125 ms
        pp.number = 1e9
        pp.noise = noise # 0 = no noise, same interval every time. 1 = maximum noise, variable interval with poisson mean of 125 ms                
        pp.start = 0
        self.pp = pp

    def is_art(self):
        return 1

    def setnoiseFromRandom(self,ranstream):
        self.noiseFromRandom(ranstream)
    
    def connect2target(self, target, thresh=-10):
        nc = h.NetCon(self.pp, target)
        nc.threshold = thresh
        
        #self.spike_times = []
        #vecrecs = []
        #vecrecs.append(h.Vector())
        #nc.record(vecrecs[0])
        #self.nclist.append(nc)
        #self.spike_times.append(vecrecs[0])

        return nc
        
    def position(self,xp,yp,zp):
        self.x = xp
        self.y = yp
        self.z = zp    
        xpos = xp
        ypos = yp
        zpos = zp    
        #self.pp.position(xpos, ypos, zpos)
        