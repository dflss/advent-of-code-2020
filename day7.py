from copy import copy
from dataclasses import dataclass


def parse_rules():
    with open("day7_data.txt", "r") as file:
        lines = file.readlines()
    rules = []
    for line in lines:
        bags = line.split(" bags contain ")
        bag_outer = bags[0]
        bags_inner = []
        for bag in bags[1].split(", "):
            bag_split = bag.split()
            amount = bag_split[0]
            if amount == 'no':
                continue
            type = ""
            for i in range(1, len(bag_split) - 1, 1):
                type += bag_split[i] + " "
            bags_inner.append((amount, type.strip()))
        rules.append((bag_outer, bags_inner))
    return rules


def find_outer_bags(rules, inner_bag):
    outer_bags = set()
    for rule in rules:
        bags = rule[1]
        for bag in bags:
            if bag[1] == inner_bag:
                outer_bags.add(rule[0])
                outer_bags.update(find_outer_bags(rules, rule[0]))
    return outer_bags


@dataclass
class BagCount:
    number: int
    name: str


def parse_rules_dict():
    with open("day7_data.txt", "r") as file:
        lines = file.readlines()
    rules = {}
    for line in lines:
        bags = line.split(" bags contain ")
        bag_outer = bags[0]
        bags_inner = []
        for bag in bags[1].split(", "):
            bag_split = bag.split()
            amount = bag_split[0]
            if amount == 'no':
                continue
            type = ""
            for i in range(1, len(bag_split) - 1, 1):
                type += bag_split[i] + " "
            bags_inner.append(BagCount(int(amount), type.strip()))
        rules[bag_outer] = bags_inner
    return rules


def find_inner_bags(rules, outer_bag):
    total_bags = rules.get(outer_bag, []).copy()
    bags_stack = rules.get(outer_bag, []).copy()
    while bags_stack:
        parent_bag = bags_stack.pop()
        children_bags = rules.get(parent_bag.name, [])
        for child_bag in children_bags:
            child_copy = copy(child_bag)
            child_copy.number = parent_bag.number * child_copy.number
            total_bags.append(child_copy)
            bags_stack.append(child_copy)
    return sum([bag.number for bag in total_bags])


### Part 1 ###
print(len(find_outer_bags(parse_rules(), "shiny gold")))

### Part 2 ###
print(find_inner_bags(parse_rules_dict(), "shiny gold"))