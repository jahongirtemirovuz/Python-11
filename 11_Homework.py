####################################### Task 1 -- Luke, I am your ...
# # def relation_to_luke(name):
# #     relation = {
# #         "Darth Vader": "father",
# #         "Leila": "sister",
# #     }
# #     if name in relation:
# #         return f"Luke I am your {relation[name]}"
# #     else:
# #         return "I don't know who are you speaking of."
    

####################################### Task 2 -- Get studrnt names
# def get_student_names(students):
#     return sorted(students.value())
# # students = {
# #     "Student 1": "Steve",
# #     "Student 2": "Dann",
# #     "Student 3": "John"
# # }
# # print(get_student_names(students))

# # print(get_student_names({
# #     "Student 1": "Steve",
# #     "Student 2": "Dann",
# #     "Student 3": "John"
# # }))


####################################### Task 3 -- Scrabble hand 
# def maximum_score(tile_list):
#     return sum(tile['score'] for tile in tile_list)

# print(maximum_score({
#     "tile": "N", "score": 1 ,
#     "tile": "K", "score": 5 ,
#     "tile": "Z", "score": 10 ,
#     "tile": "X", "score": 8 ,
#     "tile": "D", "score": 2 ,
#     "tile": "A", "score": 1 ,
#     "tile": "E", "score": 1 ,
# }))


# # score_dict = {}
# #     for tile in tile_list:
# #         score_dict[tile["tile"]] = score_dict.get(tile["tile"], 0) + tile["score"]
# #         return sum(score_dict.values)


####################################### Task 4 -- Frequency distribution
def get_frequinces(lst):
    freq_dict = {}
    for elem in lst:
        freq_dict[elem] = freq_dict.get(elem, 0 ) + 1
    return freq_dict

lst1 = [1, 2, 3, 3, 2]
print(get_frequinces(lst1))

lst2 = ["A", "B", "A", "A"]
print(get_frequinces(lst2))


####################################### Task 5 -- Invert Keys and Values
def invert(dct):
    return {v: k for k, v in dct.items()}
print(invert({"zebra": "koala", "horse": "camel"}))