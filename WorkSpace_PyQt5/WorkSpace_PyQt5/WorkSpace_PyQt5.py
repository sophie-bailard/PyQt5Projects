

global count 
count = 0

class t():
    def checkExpect(self, test, expectedValue):
        global count
        temp = count + 1
        count = temp
        if test != expectedValue:
            print("Test #" + str(count) + " Actual: " + str(test) \
                 + ", Expected: " + str(expectedValue))


    

class ValidDate():
    def __init__(self, dateData):
        self.dateData = dateData
        self.isValid = self.isValidDate()

    #checks to see if date entered is valid dd/mm/yyyy
    def isValidDate(self):
        valid = False
        if self.dateNumbers() and self.hasDateFormat():
           print("hi")
           valid = self.isValidMonth() and self.isValidDay()
        return valid
        
    #does date use correct date format? "dd/mm/yyyy"
    def hasDateFormat(self):
        return (len(self.dateData) == 10) and self.slashes()

    #are slashes in correct location on date?
    def slashes(self):
        return self.dateData[2:3] == "/" and self.dateData[5:6] == "/" 

    #can date values be converted to ints?
    #EFFECT: sets day, month, and year
    def dateNumbers(self):
        try:
            self.dayStr = self.dateData[0:2]
            self.monthStr = self.dateData[3:5]
            self.yearStr = self.dateData[6:]
            if self.dayStr[0:1] == "0":
                self.day = int(self.dayStr[1:2])
            else:
                self.day = int(self.dayStr)
            self.month = int(self.monthStr)
            self.year = int(self.yearStr)
            return True
        except ValueError:
            return False

    #is the day valid?
    def isValidDay(self):
        if self.month31day():
            valid = (self.day <= 31 and self.day > 0)
        elif self.monthStr == ("04" or "06" or "09" or "11"):
            valid = (self.day <= 30 and self.day > 0)
        elif (self.monthStr == "02"):
            if self.isLeapYear():
                valid = (self.day <= 29 and self.day > 0)
            else:
                valid = (self.day <= 28 and self.day > 0)
        else:
            valid = False
            
        return valid

    def month31day(self):
       return (self.monthStr == "01") or (self.monthStr == "03") or (self.monthStr == "05") \
       or (self.monthStr == "07") or (self.monthStr == "08") or (self.monthStr == "10") or (self.monthStr == "12")

############################# Leap Year ###############################

    #returns true if is a leap year
    def isLeapYear(self):
        if self.yearStr[2:] == "00":
            return self.leapCentury()
        else:
            return (self.year % 4) == 0

    #returns true if century years (end in 00) are leap years
    def leapCentury(self):
        return (self.year % 400) == 0

    def isValidMonth(self):
        return self.month < 13 and self.month > 0

    
      ################################################################################################################################



from ValidDate import ValidDate
from CheckExpects import t

def testLeapCentury():
    print("leapCentury")
    t().checkExpect(ValidDate("11/11/2100").leapCentury(), False)
    t().checkExpect(ValidDate("11/11/0021").leapCentury(), False)
    t().checkExpect(ValidDate("11/11/0201").leapCentury(), False)
    t().checkExpect(ValidDate("11/11/2001").leapCentury(), False)
    t().checkExpect(ValidDate("11/11/2000").leapCentury(), True)
    t().checkExpect(ValidDate("11/11/1900").leapCentury(), False)
    print()

def testIsLeapYear():
    print("isLeapYear")
    t().checkExpect(ValidDate("11/11/2000").isLeapYear(), True)
    t().checkExpect(ValidDate("11/11/5890").isLeapYear(), False)
    t().checkExpect(ValidDate("11/11/1111").isLeapYear(), False)
    t().checkExpect(ValidDate("11/11/2004").isLeapYear(), True)
    t().checkExpect(ValidDate("11/11/1900").isLeapYear(), False)
    print()

def testIsValidDate():
    print("isValidDate")
    t().checkExpect(ValidDate("11/11/2000").isValidDate(), True)
    print()

def testHasDateFormat():
    print("hasDateFormat")
    t().checkExpect(ValidDate("11/11/2000").hasDateFormat(), True)
    t().checkExpect(ValidDate("11/sd/2000").hasDateFormat(), True)
    t().checkExpect(ValidDate("11/00/ashd").hasDateFormat(), True)
    t().checkExpect(ValidDate("as/00/2000").hasDateFormat(), True)
    t().checkExpect(ValidDate("11/11").hasDateFormat(), False)
    t().checkExpect(ValidDate("00/00/0000").hasDateFormat(), True)
    t().checkExpect(ValidDate("11/11/2000").hasDateFormat(), True)
    t().checkExpect(ValidDate("11112000").hasDateFormat(), False)
    print()

def testSlashes():
    print("slashes")
    t().checkExpect(ValidDate("11112000").slashes(), False)
    t().checkExpect(ValidDate("111/11/200").slashes(), False)
    t().checkExpect(ValidDate("11/11/2000").slashes(), True)
    t().checkExpect(ValidDate("11/11").slashes(), False)
    print()

def testDateNumbers():
    print("dateNumbers")
    t().checkExpect(ValidDate("11/11/2000").dateNumbers(), True)
    t().checkExpect(ValidDate("11/11/asdd").dateNumbers(), False)
    t().checkExpect(ValidDate("as/11/2000").dateNumbers(), False)
    t().checkExpect(ValidDate("11/ad/2000").dateNumbers(), False)
    print()

def testIsValidDay():
    print("isValidDay")
    t().checkExpect(ValidDate("31/01/2000").isValidDay(), True)
    t().checkExpect(ValidDate("30/10/2000").isValidDay(), True)
    t().checkExpect(ValidDate("32/07/2000").isValidDay(), False)
    t().checkExpect(ValidDate("00/03/2000").isValidDay(), False)
    t().checkExpect(ValidDate("01/03/2000").isValidDay(), True)
    t().checkExpect(ValidDate("09/03/2000").isValidDay(), True)

    t().checkExpect(ValidDate("30/04/2000").isValidDay(), True)
    t().checkExpect(ValidDate("31/04/2000").isValidDay(), False)
    t().checkExpect(ValidDate("32/04/2000").isValidDay(), False)
    t().checkExpect(ValidDate("29/04/2000").isValidDay(), True)

    t().checkExpect(ValidDate("29/02/2000").isValidDay(), True)
    t().checkExpect(ValidDate("30/02/2000").isValidDay(), False)
    t().checkExpect(ValidDate("28/02/2000").isValidDay(), True)
    t().checkExpect(ValidDate("28/02/1900").isValidDay(), True)
    t().checkExpect(ValidDate("30/02/1900").isValidDay(), False)
    t().checkExpect(ValidDate("29/02/1900").isValidDay(), False)

    print()

def testIsValidMonth():
    print("isValidMonth")
    t().checkExpect(ValidDate("11/11/2000").isValidMonth(), True)
    t().checkExpect(ValidDate("11/14/2000").isValidMonth(), False)
    t().checkExpect(ValidDate("11/13/2000").isValidMonth(), False)
    t().checkExpect(ValidDate("11/01/2000").isValidMonth(), True)
    t().checkExpect(ValidDate("11/12/2000").isValidMonth(), True)
    t().checkExpect(ValidDate("11/00/2000").isValidMonth(), False)
    print()

def testmonth31day():
    print("month31day")
    t().checkExpect(ValidDate("11/02/2000").month31day(), False)
    t().checkExpect(ValidDate("11/04/2000").month31day(), False)
    t().checkExpect(ValidDate("11/01/2000").month31day(), True)
    t().checkExpect(ValidDate("11/03/2000").month31day(), True)
    t().checkExpect(ValidDate("11/05/2000").month31day(), True)
    t().checkExpect(ValidDate("11/07/2000").month31day(), True)
    t().checkExpect(ValidDate("11/08/2000").month31day(), True)
    t().checkExpect(ValidDate("11/10/2000").month31day(), True)
    t().checkExpect(ValidDate("11/12/2000").month31day(), True)
    print()

#testLeapCentury()
#testIsLeapYear()
#testHasDateFormat()
#testSlashes()
#testDateNumbers()
#testIsValidDay()
#testIsValidMonth()
#testmonth31day()

