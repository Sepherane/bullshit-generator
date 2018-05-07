# coding=utf8

from argparse import ArgumentParser
from random import randint
import sys

matrix_consultant = [["Het proces", "De factor mens", "Het management", "De communicatie", "De kerncompetentie", "Human capital", "De organisatieontwikkeling", "De missie", "Kennismanagement", "De eerste aanzet"], 
    ["moet meerwaarde leveren bij", "stelt eisen aan", "dient te faciliteren bij", "is uitgangspunt bij", "is onlosmakelijk verbonden met", "schept voorwaarden voor", "dient te focussen op", "stuurt", "hangt nauw samen met", "moet een opstap bieden voor"], 
    ["de implementatie van", "de terugkoppeling van", "het aftimmeren van", "het aansturen van", "de ontwikkeling van", "de flexibilisering", "de integratie van", "de inventarisatie van", "de definitie van", "de insteek van"], 
    ["complexe", "optimale", "in elkaar grijpende", "eenduidige", "onderling afhankelijke", "van structurele", "pro-actieve", "resultaatgerichte", "efficiënte", "consistente"], 
    ["supply chain processen", "business architecture", "mijlpalen", "targets", "business units", "organisatie-onderdelen", "scenario's", "best practices", "business models", "conceptplannen"], 
    ["waarbij het belang van", "waarbij de feedback van", "waarbij het kader voor", "waarbij afstemming met", "waarbij de structuur van", "waarbij de synergie met", "waarbij de interface met", "waarbij input van", "waarbij commitment van", "waarbij klankborden met"], 
    ["strategisch beleid", "de taskforce", "de communicatie", "de werkgroepen", "new business development", "de systeemintegratie", "de markt", "de stakeholders", "het management", "de projectorganisatie"], 
    ["moet uitkristalliseren.", "voorop staat.", "wordt aangestuurd.", "leading is.", "toegevoegde waarde levert.", "win-win situaties creëert.", "moet worden gemanaged.", "voldoende draagvlak heeft.", "doorslaggevend is.", "cruciaal is."]]

matrix_ambtenaar = [["Het proces", "Het format", "Het management", "De communicatie", "De nieuwe organisatie", "Het ontwikkelpad", "De organisatieontwikkeling", "De missie", "Kennismanagement", "De eerste aanzet"], 
    ["moet meerwaarde leveren bij", "stelt eisen aan", "dient te faciliteren bij", "is uitgangspunt bij", "is onlosmakelijk verbonden met", "schept voorwaarden voor", "dient te focussen op", "stuurt", "hangt nauw samen met", "moet een opstap bieden voor"], 
    ["de implementatie van", "de terugkoppeling van", "het aftimmeren van", "het aansturen van", "de ontwikkeling van", "de flexibilisering van", "de integratie van", "de inventarisatie van", "de definitie van", "de insteek van"], 
    ["complexe", "optimale", "met elkaar samenhangende", "eenduidige", "onderling afhankelijke", "van structurele", "probleemoplossende", "resultaatgerichte", "efficiënte", "consistente"], 
    ["beslissingen", "besluitvorming", "oplossingen", "belangen", "teams", "organisatieonderdelen", "oplossingsrichtingen", "uitgangspunten", "protocollen", "memo's"], 
    ["waarbij het belang van", "waarbij de feedback van", "waarbij het kader voor", "waarbij afstemming met", "waarbij de structuur van", "waarbij de samenhang met", "waarbij de uitkomst van", "waarbij input van", "waarbij commitment van", "waarbij klankborden met"], 
    ["strategisch beleid", "de stuurgroep", "de communicatie", "de werkgroepen", "het ministerie", "de buitenwacht", "de markt", "de stakeholders", "de directie", "het beleid"], 
    ["moet uitkristalliseren.", "voorop staat.", "wordt aangestuurd.", "afgestemd moet worden.", "toegevoegde waarde levert.", "oplossingsgericht is.", "moet worden besloten.", "voldoende draagvlak heeft.", "doorslaggevend is.", "cruciaal is."]]

matrix = matrix_ambtenaar

tussenwoorden = ["daarom", "desalniettemin", "hoe dan ook", "tenslotte", "echter", "hierdoor", "met name", "tevens", "ook", "uiteraard"]

def randomMemo():
    text = ""
    j = randint(2,6)
    i = randint(2,6)
    for l in range(0,j):
      for n in range(0,i):
        text += matrix[0][randint(0,9)] + ' '
        arr = matrix[1][randint(0,9)].split(' ')
        arr.insert(1,tussenwoorden[randint(0,9)])
        text += " ".join(arr) + " "
        for m in range(2,8):
          text += matrix[m][randint(0,9)] + ' '

      text += '\n'
    return text

def randomSentence():
    str = ""
    for x in range(0,8):
        str += matrix[x][randint(0,9)] + ' '
    return str

def main():
    ap = ArgumentParser()
    ap.add_argument("-v", "--verbose", default=False, action='store_true', help="Increased verbosity")
    ap.add_argument("-t", "--type", type=str, default="ambtenaar", help="Type of sentence/memo (ambtenaar or consultant)")
    ap.add_argument("action", default="zin", help="Generate a sentence or memo (sentence/zin or memo)")
    args = ap.parse_args()

    if(args.type == "consultant"):
        matrix = matrix_consultant
    elif(args.type != "ambtenaar"):
        print "Unsupported type"
        sys.exit(0)


    if(args.verbose):
        print "--- Starting generation ---"
    
    if(args.action == "sentence" or args.action == "zin"):
        print randomSentence()
    elif(args.action == "memo"):
        print randomMemo()
    else:
        print "Unsupported action"

    if(args.verbose):
        print "--- Finished generation ---"


main()

