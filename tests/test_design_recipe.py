from lib.design_recipe import *

def test_design_recipe():
    reading = design_recipe(5000)
    assert reading == 25

def test_design_recipe_highnum():
    reading = design_recipe(25000)
    assert reading == 125

def test_design_recipe2():
    grammer = design_recipe2("Hello world")
    assert grammer == False

def test_design_recipe2_punctutation():
    grammer = design_recipe2("ello world.")
    assert grammer == False

def test_design_recipe2_punctutation_and_capital():
    grammer = design_recipe2("Hello world.")
    assert grammer == True

def test_design_recipe3_todo():
    check = design_recipe3("Hello world #TODO.")
    assert check == True

def test_design_recipe3_todo_for_false():
    check = design_recipe3("Hello world #TDO.")
    assert check == False