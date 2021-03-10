class Leaderboard:
    def __init__(self):
        self.filename = "C:\\Users\\User\\Documents\\GitHub\\Nibbles-Game\\Nibbles-Reboot\\leaderboard.txt"
  
    def saveFile(self, pname, pscore):
        scoreboard_file = open(self.filename, "a")
        scoreboard_file.write(pname + " " + str(pscore) + "\n")
        scoreboard_file.close()
 
    def GetTop10(self):
        scores = []
        nameList = []
        top10List = []
        nameCount = 0
        listCount = 0

        scoreboard_file = open(self.filename, "r")
        txt = scoreboard_file.read()
        splitList = txt.split()

        for i in range(len(splitList)):
            char = splitList[i]
            if char.isnumeric() == True:
                scores.append(int(char))

        while nameCount < len(splitList):
            nameList.append(splitList[nameCount])
            nameCount += 2

        while listCount < 10 and len(scores) > 0:
            score = max(scores)
            index = scores.index(score)
            top10List.append(nameList[index] + " " + str(score))
            listCount += 1
            scores.remove(score)
            nameList.remove(nameList[index])
        return top10List

