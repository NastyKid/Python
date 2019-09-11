from IPython.display import clear_output

class Game:
    def __init__(self):
        self.__title = ''
        self._player = Player() # instantiation for player
        self.__terminate = False
        self.__over = False

    def menu(self):
        pass

    def game(self):
        pass

    def play(self):
        pass

    def getTitle(self):
        return self.__title

    def setTitle(self,title):
        self.__title = title

    def isOver(self):
        return self.__over

    def over(self):
        self.__over = True

    def restart(self):
        self.__over = False

    def terminate(self):
        self.__terminate = True

    def isTerminate(self):
        return self.__terminate

class Player:
    def __init__(self):
        self.__playerName = ['','']
        self.move = [0,0]
        self.__player = 0

    def setPlayerName(self,name,player):
        self.__playerName[player] = name

    def getPlayerName(self,player):
        return self.__playerName[player]

    def getPlayer(self):
        return self.__player

    def setPlayer(self,player):
        self.__player = player

    def playerMove(self):
        print()
        row = input('Row #: ')
        stick = input('Stick : ')
        try:
            row = int(row)
            stick = int(stick)
            self.move[0],self.move[1] = row-1,stick
        except ValueError: # err
            print('Error: Invalid Input')
            self.move()

    def getMove(self):
        return self.move

class GameOfNim(Game):

    def __init__(self): # initialization
        super().__init__()
        self.setTitle('GameOfNim')
        self.__row = []  # set rows

    def __getStick(self,row): # return current # of stick in a row
        return self.__row[row]

    def __changePlayer(self): # change player
        if(self._player.getPlayer() == 1):
            self._player.setPlayer(self._player.getPlayer()-1)
        else:
            self._player.setPlayer(self._player.getPlayer()+1)

    def __getTotalStick(self): # get total stick
        return sum(self.__row)

    def __validate(self,move):
        return True if (move[0] > -1 and move[0] < 4) and (move[1] > 0) else False

    def __draw(self): # draw current rows status
        count = 1
        for x in self.__row:
            print('\n   ',end = "")
            for c in range(x):
                 print('\t|', end ="")
            print('\nRow #',count,end = "")
            for c in range(x):
                 print('\t|', end ="")
            print('\n   ',end = "")
            for c in range(x):
                 print('\t|', end ="")
            print()
            count += 1

    def __menu(self):
        err = True
        while(err):
            print('>\t'+self.getTitle()+'\t<')
            try:
                start = int(input('\t1 > Play\n\t2 > Exit\nAns> '))
                if(start != 1 and start != 2): # err
                    clear_output()
                    print('Error: Invalid Input')
                elif(start == 2): # exit
                    self.over()
                    self.terminate()
                    err = False
                    print('Bye-Bye')

                else:
                    err = False
                    name = input('Player '+ str(self._player.getPlayer()+1)+' name: ')
                    self._player.setPlayerName(name,self._player.getPlayer())
                    name = input('Player '+ str(self._player.getPlayer()+2)+' name: ')
                    self._player.setPlayerName(name,self._player.getPlayer()+1)
                    clear_output()
            except ValueError: # err
                clear_output()
                print('Error: Invalid Input')

    def __game(self):
        retry = False
        while(not retry):
            self.__row = [1,3,5,7]
            while(not self.isOver()):
                # draw
                self.__draw()
                # input
                print('\n'+self._player.getPlayerName(self._player.getPlayer())+'\'s turn')
                self._player.playerMove()
                # process
                if(self.__validate(self._player.getMove())):
                    # removing stick
                    if(self._player.move[1] <= self.__row[self._player.move[0]]):
                        self.__row[self._player.move[0]] = self.__row[self._player.move[0]] - self._player.move[1]
                        if(self.__getTotalStick() == 0):
                            # other player win
                            clear_output()
                            self.__draw()
                            self.__changePlayer()
                            print(self._player.getPlayerName(self._player.getPlayer()),' win!')
                            self.over()
                        elif(self.__getTotalStick() == 1):
                            # current player win
                            clear_output()
                            self.__draw()
                            print(self._player.getPlayerName(self._player.getPlayer()),' win!')
                            self.over()
                        else:
                            self.__changePlayer()
                            clear_output()
                    else: # err
                        clear_output()
                        print('Error: Row #',self._player.move[0]+1,' have only ',self.__row[self._player.move[0]],' stick left')
                else: # err
                    clear_output()
                    print('Error: Invalid Input')

            x = str(input('Enter [R] to play again\n\t> '))
            if(x == "r" or x == "R"):
                clear_output()
                self.restart()
            else:
                clear_output()
                retry = True


    def play(self): # process
        # game loop
        # menu
        while(not self.isTerminate()):
            self.__menu()
            if(not self.isTerminate()):
                self.__game()

x = GameOfNim()
x.play()
