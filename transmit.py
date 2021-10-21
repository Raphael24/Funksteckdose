from argparse import ArgumentParser
import os
parser = ArgumentParser()

parser.add_argument("arsch")
args = parser.parse_args()


def schalterAON():
    print("schalter A ON")
    os.system("sudo ./433Utils/RPi_utils/codesend 5506385")


def schalterAOFF():
    print("schalter A OFF")
    os.system("sudo ./433Utils/RPi_utils/codesend 5506388")

def schalterBON():
    print("schalter B ON")
    os.system("sudo ./433Utils/RPi_utils/codesend 5509457")

def schalterBOFF():
    print("schalter B OFF")
    os.system("sudo ./433Utils/RPi_utils/codesend 5509460")



if args.arsch == "AON":
    print('schaltera')
    schalterAON()

if args.arsch == "AOFF":
    print('schaltera')
    schalterAOFF()

if args.arsch == "BON":
    print('schaltera')
    schalterBON()

if args.arsch == "BOFF":
    print('schaltera')
    schalterBOFF()
