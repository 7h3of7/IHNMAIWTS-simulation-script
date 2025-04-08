from playingcards import Deck, Card
import csv

def addScore(card, combo, score):
    cardValue = card.value
    cardSuit = card.suit
    if cardValue == 11 or cardValue == 12 or cardValue == 13:
        value = 10
    elif cardValue == 1:
        if cardSuit == 0 or cardSuit == 1:
            value = 11
        elif cardSuit == 2 or cardSuit == 3:
            value = 1
        else:
            print("card doesnt have a suit??")
    else:
        value = cardValue
    
    if cardSuit == 0 or cardSuit == 1:
        score += (value*combo)
        #score += value
    elif cardSuit == 2 or cardSuit == 3:
        score -= value
    return score

def updateCombo(card, combo):
    cardSuit = card.suit
    if cardSuit == 0 or cardSuit == 1:
        combo += 0.2
    elif cardSuit == 2 or cardSuit == 3:
        combo = 1
    return combo

def playGame(csvFilePath):
    deck = Deck()
    deck.shuffle()
    score = int(0)
    combo = float(1)
    cardsDrawn = int(0)
    for x in range(52):
        card = deck.draw_card()
        combo = updateCombo(card, combo)
        score = addScore(card, combo, score)
        cardsDrawn += 1
        if(score >= 100):
            break
    exportToFile(csvFilePath, int(score), cardsDrawn)

def exportToFile(csvFilePath, score, cardsDrawn):
    if score >= 100:
        endResult = "Win"
    else:
        endResult = "Lose"
    data = [endResult, score, cardsDrawn]
    with open(csvFilePath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def parseData(csvFilePath, runs):
    wins = 0
    losses = 0
    totalscore = 0
    totaldrawn = 0
    with open(csvFilePath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for lines in csvfile:
            line = lines.split(',')
            if line[0] == 'Win':
                wins+=1
            else:
                losses+=1
            totalscore += int(line[1])
            totaldrawn += int(line[2])
    winrate = (wins / (wins+losses)) * 100
    averageScore = round(totalscore/runs, 2)
    averageDrawn = round(totaldrawn/runs)
    print("Total games: ", wins+losses)
    print("Wins: ", wins, ", Losses: ", losses, ", Win rate: ", winrate)
    print("Total Score: ", totalscore, ", Average Score: ", averageScore)
    print("Total Cards Drawn: ", totaldrawn, ", Average Cards Drawn: ", averageDrawn)



def startSimulation(runs):
    csvFilePath = 'data.csv'
    with open(csvFilePath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    for x in range(runs):
        playGame(csvFilePath)
    
    parseData(csvFilePath, runs)


startSimulation(100000)