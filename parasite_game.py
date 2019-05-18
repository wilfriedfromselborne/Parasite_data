import random


class ProbParasite:

    def __init__(self, factor=0, energy=100, contribute=20):
        self.energy=energy
        self.contribute=contribute
        self.factor=factor*100
        self.killed=False

    def play(self):
        host=0
        if (self.factor>0 and random.randint(0,100)<self.factor) or self.energy<20:
            host=1       
        else:
            self.energy=self.energy-self.contribute
        if (self.killed):
            host=2
        return host

    def payout(self, payout):
        self.energy=round(self.energy+payout,2)
        if self.energy<=0:
            self.killed=True
            return "RIP"
        else:
            return self.energy


class Game:

    def __init__(self, factor=0.9, rounds=100, players=30, contribute=20, probs=[]):
        self.energy=100
        self.conribute=20
        self.parasites=[]
        self.rounds=rounds
        self.history=[]
        self.factor=factor
        self.players=players
        self.contribute=contribute
        self.history.append([100]*players)
        if len(probs)==0:
            self.probs=[0, 0.1, 0.2, 0.3, 0.4, 0.5]
        else: self.probs=probs
        self.parasites=self.create_game(players, self.probs)


    def create_game(self, players, probs):
        return [ProbParasite(factor=random.choice(probs)) for i in range(0, players)]

    def play(self):
        for i in range(0,self.rounds):
            n,contributed=self.play_round()
            if contributed==0:
                print("All Death")
                break
            print(contributed)
            print(self.scores)

    def play_round(self):
        contributed=0
        self.scores=[]
        n=0
        for p in self.parasites:
            h=p.play()
            if (h==0):
                contributed+=self.contribute
            if h!=2:
                n+=1
        payout=(contributed/n*self.factor)
        for p in self.parasites:
            self.scores.append(p.payout(payout))
        self.history.append(self.scores)
        return (n, contributed)

#example code
#
# play 4 tournaments in which the probability of a player parasiting has value p.


nplayers=10
for p in [0.0, 0.3, 0.5, 0.7]:
    g=Game(players=nplayers, probs=[p])
    g.play()
    print(g.history)
             
 
