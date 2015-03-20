# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:16:41 2015

@author: Insper
"""
import random
import time

user_score = 0
pc_score = 0

while user_score < 3 and pc_score < 3:
    pc_choice= random.choice(['pedra', 'papel','tesoura','lagarto',' spock',])
    user_choice = input('Qual sua escolha?:\n-pedra\n-papel\n-tesoura\n-lagarto\n-spock\n\nColoque aqui:')
       
    if user_choice == 'pedra' and pc_choice == 'spock':  #Primeira Pedra
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'pedra' and pc_choice == 'papel':
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'pedra' and pc_choice == 'lagarto':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == 'pedra' and pc_choice == 'tesoura':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
         
    if user_choice == 'papel' and pc_choice == 'tesoura':  #Primeira Papel
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'papel' and pc_choice == 'lagarto':
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'papel' and pc_choice == 'pedra':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == 'papel' and pc_choice == 'spock':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
        
    if user_choice == 'tesoura' and pc_choice == 'pedra':  #Primeira Tesoura
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'tesoura' and pc_choice == 'spock':
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'tesoura' and pc_choice == 'papel':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == 'tesoura' and pc_choice == 'lagarto':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
         
    if user_choice == 'lagarto' and pc_choice == 'tesoura':  #Primeira Lagarto
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'lagarto' and pc_choice == 'pedra':
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'lagarto' and pc_choice == 'spock':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == 'lagarto' and pc_choice == 'papel':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
         
    if user_choice == 'spock' and pc_choice == 'lagarto':  #Primeira Spock
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'spock' and pc_choice == 'papel':
         print('Você Perdeu') 
         pc_score += 1
         user_score = 0
         
    if user_choice == 'spock' and pc_choice == 'tesoura':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == 'spock' and pc_choice == 'pedra':
         print('Você ganhou') 
         pc_score = 0
         user_score += 1
         
    if user_choice == pc_choice :               #O Empate
        print('Empate')
        pc_score= 0
        user_score=0
         
        
         
    print('Sua escolha:', user_choice)
    time.sleep(1)      
    print('Computador escolha:', pc_choice)
    time.sleep(1)     

    print('Seu score:', user_score)
    time.sleep(1)
    print('Computador score:', pc_score)
    time.sleep(1)
                
                
                
    if user_score == 3:
        print('Parabéns! Você ganhou!')
        
    if pc_score == 3:
        print('Você perdeu! Tente novamente')