from lib.design_recipe import *

"""
Given a text of 200 words
it will return an estimate time of reading of 1 minute
"""

def test_design_recipe_for_200():
    text = " ".join(["word" for i in range(0, 200)])
    reading = design_recipe(text)
    assert reading == 1

def test_design_recipe_for_400():
    text = " ".join(["word" for i in range (0, 400)])
    reading = design_recipe(text)                                                                  
    assert reading == 2

def test_design_recipe_for_1000():
    text = " ".join(["word" for i in range (0, 1000)])
    reading = design_recipe(text)                                                                  
    assert reading == 5

def test_design_recipe2():
    grammer = design_recipe2("Hello world")
    assert grammer == False

def test_design_recipe2_punctutation():
    grammer = design_recipe2("ello world.")
    assert grammer == False

def test_design_recipe2_fullstop_and_capital():
    grammer = design_recipe2("Hello world.")
    assert grammer == True

def test_design_recipe2_questionmark_and_capital():
    grammer = design_recipe2("How r you?")
    assert grammer == True


def test_design_recipe2_exclamationmark_and_capital():
    grammer = design_recipe2("Nice weather!")
    assert grammer == True

def test_design_recipe3_todo():
    check = design_recipe3("Hello world #TODO.")
    assert check == True

def test_design_recipe3_todo_for_false():
    check = design_recipe3("Hello world #TDO.")
    assert check == False

