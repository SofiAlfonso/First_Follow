#Grammar structure
class Grammar:
    def _init_(self):
        self.nonterminals=[] #Nonterminals list
        self.terminals=[] #terminals list
        self.first={} #First dictionary "nonterminal: list of its first"
        self.follow={} #Follow dictionary "nonterminal: list of its follow"
        self.productions={} #Productions dictionary "nonterminal: list of its productions"
        self.initial

    def rule2(self):
        for d in range(1,len(self.nonterminals),1):
            for N in self.nonterminals:
                for a in self.productions[N]:
                    long = len(b)
                    cont = 0
                    for b in a:
                        if b in self.terminals:
                            break
                        elif b in self.nonterminals:
                            for c in self.first[b]:
                                if (c != 'e') and (c not in self.first[N]):
                                    self.first[N].append(c)
                            if 'e' in self.first[b]:
                                cont+=1
                    if long==cont:
                        self.first[N].append('e')



    def computeFirst(self):
        for N in self.nonterminals:
            self.first[N]=[]
            #Rule 3
            if 'e' in self.productions[N]:
                self.first[N].append('e')

            for a in self.productions[N]:
                for b in a:
                    if b in self.terminals and b not in self.first[N]:  # Rule 1
                        self.first[N].append(b)
                        break

        self.rule2()


    def computeFollow(self):
        print()

    def printSolution(self):
        print()