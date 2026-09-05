import os
import json
import random

# find matching question
# find name (x) that matches whoever got points
# find answer that matches by given name (enumerate)
# some kind of fallback

# Edgecases
# answer edits /
# question being at the end of the file /
# no one answers (fuck this one) / 

# Current issue
# People changing usernames (ignore for now)
# Matching questions doesn't work for some reason /


def getFileNames():
    dir = r"C:\Users\<usernamehere>\main\python\trivia\Output"
    filenames = []

    for root, _, files in os.walk(dir):
        for filename in files:
            filenames.append(os.path.join(root, filename))
    return filenames

def readFile(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

# 578640960045580288 guide bot id
# 578675563301044234 trivia channel id

def findQuestionIndex(file, question):
    # count = 0
    questionIndex = None # None if question not found in this file
    for index, message in enumerate(file["messages"]):
        if message["embeds"]:
            if message["author"]["id"] == "578640960045580288" and message["embeds"][0]["description"] == question:
                questionIndex = index
                break
    return questionIndex

def findWinnerName(file, questionIndex):
    for _, message in enumerate(file["messages"][questionIndex+1:], start=questionIndex+1):
        if message["author"]["id"] == "578640960045580288" and message["embeds"]:
            winnerName = message["embeds"][0]["description"].split()[0] # getting 100 point winner name only
            # return winnerName
            return winnerName

def findWinningAnswer(file, questionIndex, winnerName):
    count = 0
    for _, message in enumerate(file["messages"][questionIndex+1:], start=questionIndex+1):
        count += 1
        if count > 1: # limit to one message
            return None
        if message["author"]["name"] == winnerName:
            if not message["timestampEdited"]:
                # return f'name: {message["author"]["name"]}, answer: {message["content"]}'
                return message["content"]

if __name__ == "__main__":
    file = readFile(getFileNames())
