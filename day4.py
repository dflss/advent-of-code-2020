### Part 1 ###

with open("day4_data.txt", "r") as file:
    lines = file.read()
passports = lines.split("\n\n")
valid_count = 0
required_field_names = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for passport in passports:
    passport_fields = passport.replace("\n", " ").split(" ")
    field_names = set()
    for field in passport_fields:
        field_name = field.split(":")
        field_names.add(field_name[0])
    if field_names.issuperset(required_field_names):
        valid_count += 1
print(valid_count)


### Part 2 ###
import re


def validate_byr(value):
    return bool(re.match(REGEX_BYR, value))


def validate_iyr(value):
    return bool(re.match(REGEX_IYR, value))


def validate_eyr(value):
    return bool(re.match(REGEX_EYR, value))


def validate_hgt(value):
    return bool(re.match(REGEX_HGT, value))


def validate_hcl(value):
    return bool(re.match(REGEX_HCL, value))


def validate_ecl(value):
    return bool(re.match(REGEX_ECL, value))


def validate_pid(value):
    return bool(re.match(REGEX_PID, value))


validators_map = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
}

def validate_field(field, value):
    validator_func = validators_map.get(field)
    return validator_func(value) if validator_func else True


REGEX_BYR = re.compile(r"^(19[2-9]\d|19[5-9]\d|200[0-2])$")
REGEX_IYR = re.compile(r"^(201\d|2020)$")
REGEX_EYR = re.compile(r"^(202\d|2030)$")
REGEX_HGT = re.compile(r"^((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$")
REGEX_HCL = re.compile(r"^(#[0-9a-f]{6})$")
REGEX_ECL = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
REGEX_PID = re.compile(r"^([0-9]{9})$")


with open("day4_data.txt", "r") as file:
    lines = file.read()

passports = lines.split("\n\n")
valid_count = 0
required_field_names = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate_fields(passport_fields):
    """Returns set with all field names if all fields were validated correctly.
    """

    field_names = set()
    for field in passport_fields:
        field_name_value = field.split(":")
        field_names.add(field_name_value[0])
        if not validate_field(field_name_value[0], field_name_value[1]):
            return None
    return field_names


for passport in passports:
    passport_fields = passport.replace("\n", " ").split(" ")
    field_names = validate_fields(passport_fields)
    if field_names is not None and field_names.issuperset(required_field_names):
        valid_count += 1
print(valid_count)