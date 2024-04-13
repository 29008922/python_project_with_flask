#!/usr/bin/python3

houses = ["erick's house", "haron'shouse", "ann's house", "hannas's house", ]
def deliver_present_to_houses(houses):
    for house in houses:
        print("i delivered the present to", house)
        if len(houses) == 1:
            house = houses[0]
    else:
        mid = len(house) //2
        first_half = houses[:mid]
        second_half = houses[mid:]
        
deliver_present_to_houses(first_half)
deliver_present_to_houses(second_half)