if __name__ == "__main__":
    pass

import math
import numpy as np
#import pandas as pd
import requests
import json
import re
from config import ROOT_DIR
import os

def load_card_data():
    with open(os.path.join(ROOT_DIR,'data','cards.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
    card_data = cards_obj['data']
    return card_data

def name_search(cards,search_string):
    result = []
    for oneCard in cards:
        card_ = oneCard['name'].lower().find(search_string.lower())
        if card_ >= 0:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'hp':oneCard['hp'],'setName':oneCard['set']['name'],'setSeries':oneCard['set']['series'],'setLegal':oneCard['set']['legalities'],'small_img':oneCard['images']['small']})
    return result

def has_abilities(cards,isAbility):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result

def search_attack(cards,search_term):
    result = []
    for oneCard in cards:
        if 'attacks' in oneCard:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'attack':oneCard['attacks']['name'],'attack_cost':oneCard['attacks']['cost'],'attack_conv_cost':oneCard['attacks']['convertedEnergyCost'],'attack_damage':oneCard['attacks']['damage'],'attack_text':oneCard['attacks']['cost']})
    return result

def search_ability_names(cards,search_term):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            card_ = oneCard['abilities']['name'].lower().find(search_term.lower())
            if card_ >= 0:
                result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result


