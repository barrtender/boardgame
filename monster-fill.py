#!/usr/bin/env python

# Paste the cells from the balancing sheet into the monsters_paste variable
# Open cards_template.xcf in Gimp
# Filters -> Test -> monsterfill

import gimp
from gimpfu import *

#logging and debug https://stackoverflow.com/questions/20763448/writing-gimp-plugins-in-python-on-windows-how-do-i-debug-where-is-the-output
import sys
sys.stderr = open('C:/Temp/er.txt', 'a')
sys.stdout = open('C:/Temp/log.txt', 'a')
def gimp_log(text):
    pdb.gimp_message(text)
#end logging and debug

# Centers of the boxes
green = [55, 55]
orange = [350, 51]
red = [54, 528]
black = [350, 530]
gold = [203, 460]

card_offset = [410, 588]

# Values copy/pasted from the spreadsheet where I'm balancing monsters
monsters_paste = '''
7	18	21	38	3
12	19	24	32	4
10	14	21	26	3
11	11	18	36	2
12	23	26	47	5
7	14	28	42	3
9	11	32	49	4
8	14	22	15	3
6	10	22	24	2
11	8	26	38	3
10	22	24	45	4
10	14	21	31	3
10	16	7	20	2
12	23	11	26	3
16	14	7	54	2
9	27	39	50	6
9	12	11	22	2
9	13	37	33	5
11	23	15	30	3
7	10	24	56	3
'''.split('\n')[1:-1]
monsters = map(lambda x: x.split('\t'), monsters_paste)

font_color = "#0a0a0a"

def doit(img, layer):
    # Maybe use gimp_item_is_group and gimp_item_get_parent to make sure we're not putting it in a group
    # Or just make sure the selected layer isn't a group.
    layer_group = pdb.gimp_layer_group_new(img)
    pdb.gimp_item_set_name(layer_group, "card texts")
    img.add_layer(layer_group)

    gimp_log(monsters)

    for index, monster in enumerate(monsters):
        write_card(img, layer_group, index, monster)


def write_card(img, parent_layer, card_num, values):
    gimp_log(values)
    # Create new layer
    layer_group = pdb.gimp_layer_group_new(img)
    pdb.gimp_item_set_name(layer_group, "card " + str(card_num))

    # add new layer to the parent layer group
    pdb.gimp_image_insert_layer(img, layer_group, parent_layer, 0)
    
    # Write the values into the correct locations of the cards
    write_green(img, layer_group, card_num, values[0])
    write_orange(img, layer_group, card_num, values[1])
    write_red(img, layer_group, card_num, values[2])
    write_black(img, layer_group, card_num, values[3])
    write_gold(img, layer_group, card_num, values[4])
    pdb.gimp_selection_clear(img)


def write_green(img, layer, card_num, value):
    write_color(img, layer, card_num, value, green)

def write_orange(img, layer, card_num, value):
    write_color(img, layer, card_num, value, orange)

def write_red(img, layer, card_num, value):
    write_color(img, layer, card_num, value, red)

def write_black(img, layer, card_num, value):
    write_color(img, layer, card_num, value, black)

def write_gold(img, layer, card_num, value):
    write_color(img, layer, card_num, value, gold)

def write_color(img, parent_layer, card_num, value, color):
    text_layer = pdb.gimp_text_layer_new(img, value, "Comic Sans MS Bold", 71, 3)
    pdb.gimp_image_insert_layer(img, text_layer, parent_layer, 0)
    pdb.gimp_text_layer_set_color(text_layer, font_color)
    offset = get_card_offset(card_num)
    text_layer.set_offsets(offset[0] + color[0] - text_layer.width/2, offset[1] + color[1] - text_layer.height/2)
    pdb.gimp_selection_clear(img)

def get_card_offset(card_num):
    col = card_num % 10
    row = card_num / 10
    return [card_offset[0] * col, card_offset[1]*row]

register(
    "python_fu_monster_fill",
    "Monster Fill",
    "Adds numbers to the monster cards",
    "barrtender",
    "MIT",
    "2022",
    "<Image>/Filters/Test/monster_fill",
    "*",
    [],
    [],
    doit)

main()

