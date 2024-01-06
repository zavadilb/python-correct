import sys
import unittest
from unittest.mock import patch
from io import StringIO
import main as main
import random
from main import Env


def customPrint(msg):
    sys.stdout.write("|||"+str(msg))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def colorOutput(color):
    sys.stdout.write(color)


def printTaskSuccess(taskNum):
    sys.stdout.write(f'{bcolors.OKGREEN}Minden teszt sikeresen lefutott, a(z) {taskNum}. feladat helyes! :)\n')

def printTaskFail(taskNum):
    sys.stdout.write(f'{bcolors.FAIL}Nem sikerult a(z) {taskNum}. feladat, mert hibasan futottak a tesztek!\n')

def printSeparator(taskNum):
    colorOutput(bcolors.RESET)
    sys.stdout.write("-"*80 + '\n')
    sys.stdout.write(f'{bcolors.BOLD}{taskNum}. Feladat: \n{bcolors.RESET}')

def printTestSucccess(testNum, expected, result):
    colorOutput(bcolors.OKGREEN)
    print(f'{bcolors.RESET}Elvart eredmeny: {expected}')
    print(f'{bcolors.RESET}Kapott eredmeny: {bcolors.OKGREEN}{result}')
    print(f'{testNum}. teszt sikeres!')
def printTestFail(testNum, expected, result):
    colorOutput(bcolors.FAIL)
    print(f'{bcolors.RESET}Elvart eredmeny: {expected}')
    print(f'{bcolors.RESET}Kapott eredmeny: {bcolors.FAIL}{result}')
    print(f'{testNum}. teszt sikertelen!')

def printTestHeader(args):
    colorOutput(bcolors.HEADER)
    print(f"Tesztelem a feladatot a kovetkezo bemenetekkel: {', '.join(args)}" )

def testTaskEquals(taskNum, testNum, functionName, inputArr, expected):
    if Env.MELYIK_FELADATON_DOLGOZOK != taskNum: return
    printSeparator(taskNum)
    inputArr = [str(x) for x in inputArr]
    printTestHeader(inputArr)

    txtInput = '\n'.join(inputArr) + '\n'
    with patch('builtins.print', new=customPrint):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('sys.stdin', new=StringIO(txtInput)) as fake_in:
                task = getattr(main, functionName)
                task()

    result = None
    try:
        result = fake_out.getvalue().split('|||')[1].strip()
    except:
        sys.stderr.write(f"Hiba! (Biztosan kiir valamit a(z) {taskNum}. feladat?)\n")

    if (result == expected):
        printTestSucccess(testNum, expected, result)
        return True
    else:
        printTestFail(testNum, expected, result)
        return False

def multipleTestTaskEquals(taskNum, functionName, inputArrs, expectedArr):
    if Env.MELYIK_FELADATON_DOLGOZOK != taskNum: return
    passedAll = True
    for i in range(len(inputArrs)):

        if not testTaskEquals(taskNum, i + 1, functionName, inputArrs[i], expectedArr[i]):
            passedAll = False
    if passedAll:
        printTaskSuccess(taskNum)
    else:
        printTaskFail(taskNum)
        assert()


class TestMain(unittest.TestCase):
    def testZero(self):
        testTaskEquals(0, 1, 'nulladik', [''], 'Szia!')

    def testFirst(self):
        inputArrs = []
        expected = []

        inputArrs.append(["10 20 30 40 50 60"])
        expected.append("Nem")

        inputArrs.append(["1212 9300 3100"])
        expected.append("Nem")

        inputArrs.append(["24 53 123 9600"])
        expected.append("Igen")

        inputArrs.append(["9301"])
        expected.append("Igen")


        multipleTestTaskEquals(1, 'elso', inputArrs, expected)

    def testSecond(self):
        inputArrs = []
        expectedArr = []

        inputArrs.append(["440 34 3234 23442"])
        expectedArr.append("1 ilyen jármű volt.")

        inputArrs.append(["13 134 13344343 314139587 1234 22"])
        expectedArr.append("2 ilyen jármű volt.")

        inputArrs.append(["9300"])
        expectedArr.append("0 ilyen jármű volt.")

        inputArrs.append(["9301"])
        expectedArr.append("1 ilyen jármű volt.")

        multipleTestTaskEquals(2, 'masodik', inputArrs, expectedArr)


    def testThird(self):
        inputArrs = []
        expectedArr = []

        inputArrs.append(['110 2000 300 3032'])
        expectedArr.append('Össztömeg: 5442kg, nehéz: 0kg')

        inputArrs.append(['9301 2131 9500 123 382'])
        expectedArr.append('Össztömeg: 21437kg, nehéz: 18801kg')

        inputArrs.append(['9301'])
        expectedArr.append('Össztömeg: 9301kg, nehéz: 9301kg')

        multipleTestTaskEquals(3, 'harmadik', inputArrs, expectedArr)

if __name__ == '__main__':
    unittest.main()

