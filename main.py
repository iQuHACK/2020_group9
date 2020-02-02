# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:14:27 2020

@collaborators: Hantoa, Derrick, Malvika, & Sergio
"""

from teleportation_circuit import *
import random
import time

#p is the probability of a single gate failing; n is the number of gates used so far.
def checkFail(n, p = 0.01):
        roll = random.random()
        if roll < (1 - p) ** n:
            return False
        else:
            return True

def startGame():
    
    while True:
        print("Simulation or real quantum computer? [sim/qc]")
        desired_device = input().lower()
        if desired_device != 'sim' and desired_device != 'qc':
            print('Not a valid response. Type sim or qc.')
        else: break
    
    p = 0.01
    print("Enter a failure rate: leave blank for 0.01")
    choice = input()
    if len(choice) != 0:
        try:
            p = float(choice)
        except:
            print("Not a float; using 0.01")
            
    #n starts at 8, since each teleportation requires 8 gates. p is 0.01 for now.
    n = 8
    
    #curQ is the current qubit that can be chnaged, while nxtQ is the other qubit.
    curQ = 0
    nxtQ = 2
    measurable = False
    first_turn = True
    
    #score keeps track of the score
    score = [0, 0]
    stopped = False
    
    while True:
        
        if curQ == 0:
            print("Player 1's turn!")
        else:
            print("Player 2's turn!")
        
        #Tells player the current fidelity; asks them whether they want to add gates.
        print("Current fidelity: " + str((1 - p) ** n))
        print("Current score: " + str(score[0]) + "-" + str(score[1]))
        
        if measurable:
            random_gate_position = random.randint(0, extra-1)
            gates_list = list(gates)
            for i in range(extra):
                if i != random_gate_position: gates_list[i] = '*'
            gates = "".join(gates_list)
            print("The other player used these gates: " + gates)
        
        if not first_turn:
            print("Measure the state? [y/n]")
            choice = input().lower()
            if len(choice) > 0 and choice[0] == 'y':
                stopped = True
                endgame(curQ, desired_device, True)
                break
            else: print("You did not measure the state.")
        
        first_turn = False
        measurable = True
        
        print("Add gates? [y/n]")
        choice = input().lower()
        if len(choice) > 0 and choice[0] == 'y':
            gates = getUserInput(curQ)
            extra = len(gates)
            n += extra
            
            player_operation(gates, curQ, circuit, False)
            
            #Giving the correct player the points
            if curQ == 0:
                score[0] += extra
            else:
                score[1] += extra
                
        else: 
            print("No gates added.")
            measurable = False
    
        print("Teleporting...")
        time.sleep(1)
        
        addTeleport(curQ, nxtQ)
        curQ = 2 - curQ
        nxtQ = 2 - nxtQ
        
        if checkFail(n, p):
            print("Transmission failed!")
            if curQ == 2:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
            break
        else:
            if score[0] >= 15:
                print("Player 1 wins with " + str(score[0]) + " points!")
                break
            elif score[1] >= 15:
                print("Player 2 wins with " + str(score[1]) + " points!")
                break
            else:
                n += 8
    
    if not stopped:
      endgame(curQ, desired_device)

startGame()

import os
if os.name == 'nt':
  input()
