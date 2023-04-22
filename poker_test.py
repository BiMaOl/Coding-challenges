import random
#hand_str = '7C 7D 7H 7S 6D'
faces_str = '2 3 4 5 6 7 8 9 10 J Q K A'
suit_str = 'H D C S'
face_num = 13
suit_num = 4
'''
card_tab = [face_set, face_set, face_set, face_set]
#card_tab_T = [0, 0, 0, 0] * 13
card_tab_T = [suit_set] * 13
face_cnt_vctr = [0] * 13
suit_cnt_vctr = [0] * 4
_1st_index_vctr = [0] * 4'''

#cards = hand_str.split()
faces = faces_str.split()
suits = suit_str.split()

card_tuple_list = []
for s in suits:
    for f in faces:
        card_tuple_list.append((f, s))

class Hand:
    def __init__(self):
        self.card_tab = [[0 for i in range(13)] for j in range(4)]
        #card_tab_T = [0, 0, 0, 0] * 13
        self.card_tab_T = arr = [[0 for i in range(4)] for j in range(13)]
        self.face_cnt_vctr = [0] * 13
        self.suit_cnt_vctr = [0] * 4
        self._1st_index_vctr = [0] * 4
        self.method_list = [self.parse, self.face_count, self.suit_count, 
                            self._2_3_4, self.straight, self.flushes]
        self.hand = []
        self.create_hand()
        #self.evaluate()
        self.rank = 0
        
    def evaluate(self):
        for method in self.method_list:
            #print(f'{method}\n')
            method()

    def parse(self):
        for card in self.hand:
            print(card)
            face, suit = card
            face_index = faces.index(face)
            suit_index = suits.index(suit)
            #print(face_index, '-', suit_index)
            self.card_tab[suit_index][face_index] = 1
            self.card_tab_T[face_index][suit_index] = 1
        #print(self.card_tab)
        
    def create_hand(self):
        cnt = 0
        while cnt < 5:
            f, s = random.choice(card_tuple_list)
            self.hand.append((f, s))
            card_tuple_list.remove((f, s))
            cnt += 1
        print(self.hand)


    def face_count(self):    
        #cnt = 0
        #cnt_vctr = [0] * 13
        i = 0
        for face in self.card_tab_T:
            print('T', face)
            sum = 0
            for s in face:
                sum += s
            self.face_cnt_vctr[i] = sum
            i += 1

        print('Face_count', self.face_cnt_vctr)
        return True

    def suit_count(self):
        i = 0
        for suit in self.card_tab:
            print(suit)
            sum = 0
            for s in suit:
                sum += s
            self.suit_cnt_vctr[i] = sum
            if sum > 0:
                self._1st_index_vctr[i] = suit.index(1)
            i += 1
        print(self.suit_cnt_vctr)
        print(self._1st_index_vctr)
        
    def straight(self):
        rank = 0
        j = 0
        for i in self._1st_index_vctr:
            temp_list = self.card_tab[j][i : (i + 6)]
            if temp_list.count(1) == 5:
                self.rank = 4
                rank = 4
                break
            j += 1    
        return rank

    #royal, straight, flush
    def flushes(self):
        #rank = 0
    
        for cnt in self.suit_cnt_vctr:
            if cnt == 5:
                self.rank = 5
                for i in self._1st_index_vctr:
                    if self.straight() == 4:
                        if i == 9:
                            self.rank = 9
                            break
                        
#return rank


    #1 pair, 2 pair, 3 of a kind, full house, 4 of a kind
    #2, 2 and 2, 3, 3 and 2, 4
    def _2_3_4(self):
        pair_cnt = 0
        #rank = 0
        
        for cnt in self.face_cnt_vctr:
            print('2-3-4', cnt)
            if cnt == 0 or cnt == 1:
                continue
            elif cnt == 2:
                pair_cnt += 1
                continue
            elif cnt == 3:
                self.rank = 3   
                continue
            elif cnt == 4:
                self.rank = 7 
                continue
        
        if pair_cnt == 1:
            if self.rank == 3:
                self.rank = 6
            else:
                self.rank = 1 
        elif pair_cnt == 2:
            self.rank = 2
        #return rank
           
    def show(self):
        print(self.hand) 
        print('rank', self.rank)         

#print(card_tuple_list)

hand1 = Hand()
hand2 = Hand()
hand1.evaluate()
hand1.show()
hand2.evaluate()
hand2.show()

if hand1.rank > hand2.rank:
    message = 'Hand 1 wins\n'
elif hand2.rank > hand1.rank:
    message = 'Hand 2 wins\n'
else:
    message = 'Draw\n'
print(message)



