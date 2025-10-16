import sqlite3

con = sqlite3.connect("tutorial.db") #like mongodb connection

cur=con.cursor() # this is like pointer used to execute commands
#
# #creating sentence table
# cur.execute("CREATE TABLE sentences(sentence TEXT, score INTEGER, sentiment TEXT)")
#
# # creating word list table
# cur.execute("CREATE TABLE  words(word TEXT, score INT, is_available_in_dict BOOLEAN)")
#
# #creating analysis table
# cur.execute(
#     """
#     CREATE TABLE analysis(
#     total_sentences INT,
#     total_paragraphs INT,
#     total_score INT,
#     total_words INT,
#     total_negative_words INT,
#     total_positive_words INT,
#     total_dict_hits INT,
#     total_dict_miss INT,
#     total_positive_sentences INT,
#     total_negative_sentences INT
#     )
#     """
# )

con.commit() #take data from RAM -> .db storage
con.close()