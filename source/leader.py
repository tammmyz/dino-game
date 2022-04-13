import datetime
import os
import random
import threading
from turtle import update
import pygame
import time
from username import get_username 

# importing local application/library specific imports
from cloud import Cloud
from large_obstacle import LargeObstacle
from small_obstacle import SmallObstacle
from bird import Bird
from character import Character
from obstacle import Obstacle
import global_var
import images


## @brief Displays the restart page texts and graphics 
#  @return A list containing the formatted leader text
def get_leaders():
    font = pygame.font.Font("freesansbold.ttf", 25) # make font a global var
    score_dict = {}
    ## score: Players []
    leaders_text = []
    with open("score.txt", "r") as f:
            score = (
                f.read()
            ) 
    score_list = score.split("\n")
    # ["Anjola 3", "Chel 200"]
    curr_user_scores = [] # the current users score
    for score in score_list:
        temp = score.split()
        # temp = [Anjola, 3]
        if temp[1] in score_dict:
            score_dict[int(temp[1])].append(temp[0])
            '''
            {100 : [Anjola, Sheridan]}
            '''
        else:
            score_dict[int(temp[1])] = [temp[0]]
            ## if it's a score we've never seen, we'll make that a key
        if temp[0] == global_var.username:
            curr_user_scores.append(int(temp[1]))

    ## sort scores in descending order
    sorted_scores = sorted(score_dict, reverse=True) 
    ## a list of sorted score from score_dict
    sorted_top_scores = []  # 2-D list of top scores
    count = 0 ## ensure that only five score are added to sorted top scoresS
    for score in sorted_scores:
        if count < 5:
            ## if more than one person has the top score
            if len(score_dict[score]) > 1:
                for person in score_dict[score]:
                    if count < 5:
                        sorted_top_scores.append([person, score])
                        count+= 1
            else:
                person = score_dict[score][0]
                sorted_top_scores.append([person, score])
                count+= 1

    ## first index is the highest score
    for pair in sorted_top_scores:
        leaders_text.append(font.render(f"{pair[0]}: {pair[1]}", True, global_var.FONT_COLOR))
        ## formating the leader text
    if global_var.test_leaderboard2:
        return sorted_top_scores

    ## high score displayed is curent user's high score
    if len(curr_user_scores) > 0:
        global_var.high_score =  max(curr_user_scores)
    else:
        global_var.high_score = 0
    
    return (leaders_text)


