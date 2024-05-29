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
        for d in range(0,len(self.nonterminals),1):
            for N in self.nonterminals:
                for a in self.productions[N]:
                    long = len(a)
                    cont = 0
                    for b in a:
                        if b in self.terminals:
                            if b not in self.first[N]:
                                self.first[N].append(b)
                            break
                        elif b in self.nonterminals:
                            if 'e' not in self.first[b]:
                                for c in self.first[b]:
                                    if (c != 'e') and (c not in self.first[N]):
                                        self.first[N].append(c)
                                break
                            elif 'e' in self.first[b]:
                                for c in self.first[b]:
                                    if (c != 'e') and (c not in self.first[N]):
                                        self.first[N].append(c)
                                cont+=1
                    if long==cont and 'e' not in self.first[N]:
                        self.first[N].append('e')


    def computeFirst(self):
        for N in self.nonterminals:
            self.first[N]=[]
            #Rule 3
            if 'e' in self.productions[N]:
                self.first[N].append('e')

            for a in self.productions[N]:
                for b in a:
                    if b in self.nonterminals:
                        break
                    if b in self.terminals:# Rule 1
                        if b not in self.first[N]:
                            self.first[N].append(b)
                        break

        self.rule2()


    def computeFollow(self):
        print()

    def printSolution(self):
        for a in self.nonterminals:
            print(f"{a}: {self.first[a]}")