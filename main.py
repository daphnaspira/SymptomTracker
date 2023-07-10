import pandas as pd

foods = pd.read_csv("fooddatastore.csv",index_col=0)
symptoms = pd.read_csv("symptomdatastore.csv")

def log_food(food, time, gluten=False, lactose=False, sugar=False, 
    fiber=False, additive=False, acid=False, legume=False):
    foods.loc[len(foods)]=[food, time, gluten, lactose, sugar, fiber, additive, 
    acid, legume]
    foods.to_csv("fooddatastore.csv")

def update_log(index, food, time, gluten=False, lactose=False, sugar=False, 
    fiber=False, additive=False, acid=False, legume=False):
    foods.loc[index]=[food, time, gluten, lactose, sugar, 
    fiber, additive, acid, legume]
    foods.to_csv("fooddatastore.csv")

def remove_log(index):
    foods.drop(index, inplace=True)
    foods.to_csv("fooddatastore.csv")

def split_tags(tags):
    tag_list = tags.lower().split()
    gluten,lactose,sugar,fiber,additive,acid,legume=False,False,False,False,False,False,False
    for tag in tag_list:
        if tag == "gluten":
            gluten=True
        if tag == "lactose":
            lactose=True
        if tag == "sugar":
            sugar=True
        if tag == "fiber":
            fiber=True
        if tag == "additives":
            additive=True
        if tag == "acidic":
            acid=True
        if tag == "legume":
            legume=True
    return gluten, lactose, sugar, fiber, additive, acid, legume

def main():
    food = input("What food did you eat? ")
    time = input("What time did you eat it? ")
    tags = input("What tags would you like to give it? Separate them with a space. ")
    gluten, lactose, sugar, fiber, additive, acid, legume = split_tags(tags)
    log_food(food,time, gluten, lactose, sugar, fiber, additive, acid, legume)
    print(foods)

if __name__ == "__main__":
    main()

