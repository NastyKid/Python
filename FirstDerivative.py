import re
class Derive:

    def __init__(self):
        self.__firstDx = ""
        self.__variable = ''
        self.__terms = []

    def __disect(self,f):
        self.__variable = re.findall("[a-zA-Z]",f) # get the variable used
        self.__variable = self.__variable[0] # set it into a character
        # getting the (sign, coeffecient, exponent) of each term
        self.__terms = re.findall("([\+-]?)\s?(\d?)\*?[a-zA-Z]\*?\*?\^?(\d?)", '+' + f)

    def __deriveMe(self,f):
        self.__disect(f) # disecting the function
        for t in range(len(self.__terms)):
            # derive per term
            # combine the sign(+/-) to the coeffecient
            n = int(self.__terms[t][0] + self.__terms[t][1]) if not self.__terms[t][1] == "" else int(self.__terms[t][0]+"1")
            # get the exponent
            r = int(self.__terms[t][2]) if not self.__terms[t][2] == "" else 1

            # Power rule: n*rx^(r-1)
            n = n * r
            r = r - 1
            if(n > 0): # n > 0, + (n*r)x^(r-1) + (n*r)x^(r-1)
                self.__firstDx += "+"

            if(r == 0):
                self.__firstDx += "%d" % (n)
            elif(r == 1):
                self.__firstDx += "%d%s" % (n, self.__variable)
            else:
                self.__firstDx += "%d%s^%d" % (n, self.__variable, r)

        if(self.__firstDx[0] == "+"): # f'(x) = + 2x^3 + 6x^5
            self.__firstDx = self.__firstDx[1:]

        self.__firstDx = self.__firstDx.replace("+"," + ")
        self.__firstDx = self.__firstDx.replace("-"," - ")
        return self.__firstDx

    def getFirstDerivative(self,f):
        return self.__deriveMe(f)

x = Derive()

print(x.getFirstDerivative("-3z**4 + z**2 - z^4 + 1"))
