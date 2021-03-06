if __name__ == "__main__":
    pass

import sys
import os
import json
import tkinter as tk
import deck_database
from config import ROOT_DIR

def filter_bool_init():
    filters = {
        "energy_filter":{
            "fire" : "empty_value",
            "dark" : "empty_value",
            "fighting" : "empty_value",
            "grass" : "empty_value",
            "electric" : "empty_value",
            "water" : "empty_value",
            "psychic" : "empty_value",
            "metal" : "empty_value",
            "fairy" : "empty_value",
            "dragon" : "empty_value",
            "colorless" : "empty_value"
            },
        "set_legal":{
            "expanded" : False,
            "unlimited" : False,
            "standard" : False
            },
        "set_name" : "All",
        "name_search" : "empty_value",
        "ability_search" : "empty_value",
        "hp_search" : "empty_value",
        "hp_check" : "GT",
        "supertypes" : "All"
        }
    return filters

def load_set_names():
    with open(os.path.join(ROOT_DIR,'data','sets.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
    sets = cards_obj['data']
    set_list = []
    set_list.append('All')
    for one_set in sets:
        set_list.append(one_set['name'])
    return set_list

def load_supertypes():
    all_supertypes = ['All','Pokémon', 'Trainer', 'Energy']
    return all_supertypes

def load_usernames():
    #deck_database
    default_users = ['default_user_1','default_user_2']

def load_user_sets():
    default_users = deck_database.retrieve_users()
    #default_users = ['default_userset_1','default_userset_2']
    return default_users