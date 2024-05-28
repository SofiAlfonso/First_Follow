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
        for N in self.nonterminals:
            for a in self.productions[N]:
                for b in a:
                    long=len(b)
                    cont=0
                    if b in self.terminals:
                        break
                    elif b in self.nonterminals:
                        for c in self.first[b]:
                            if c != 'e':
                                self.first[N].append(c)
                        if 'e' in self.first[b]:
                            cont+=1
                    




    def computeFirst(self):
        for N in self.nonterminals:
            self.first[N]=[]
            #Rule 3
            if 'e' in self.productions[N]:
                self.first[N].append('e')

            for a in self.productions[N]:
                for b in a:
                    if b in self.terminals:  # Rule 1
                        self.first[N].append(b)
                        break

        self.rule2()


    def computeFollow(self):
        print()

    def printSolution(self):
        print()