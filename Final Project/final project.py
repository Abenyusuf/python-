# Name:Ahmed Benyusuf
# Class and Section: CS 120 01
# Assignment:Final Project
# Due Date:12/4/2023
# Date Turned in:12/2/2023
# Program Description: determine the cost of painting a set rooms
def main():
    # Writes the amount of gallons needed to the text file FinalProject
    def Writegallons():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            TotalSQFT = 0
            while Line != '':
                SQFT = int(Line)
                TotalSQFT = TotalSQFT + SQFT
                Line = SquareFoot.readline()
            Gallons = TotalSQFT / 112
            FormatGallons = "{:.2f}".format(Gallons)
            outfile.write(F'The total gallons of paint needed is {FormatGallons}\n')

    Writegallons()

    # Writes the amount of labor needed to the text file FinalProject
    def WriteLabor():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            TotalSQFT = 0
            while Line != '':
                SQFT = int(Line)
                TotalSQFT = TotalSQFT + SQFT
                Line = SquareFoot.readline()
            Gallons = TotalSQFT / 112
            TotalLabor = Gallons * 8
            FormatTotalLabor = "{:.2f}".format(TotalLabor)
            outfile.write(F'The total amount of labor needed is {FormatTotalLabor}\n')

    WriteLabor()

    # Writes the cost of gallons of paint needed to the text file FinalProject
    def WriteGallonsCost():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            TotalSQFT = 0
            while Line != '':
                SQFT = int(Line)
                TotalSQFT = TotalSQFT + SQFT
                Line = SquareFoot.readline()
            Gallons = TotalSQFT / 112
            CostGallons = Gallons * 50
            FormatCostGallons = "${:.2f}".format(CostGallons)
            outfile.write(F'The total cost of gallons of paint needed is {FormatCostGallons}\n')

    WriteGallonsCost()

    # Writes the amount of labor cost needed to the text file FinalProject
    def WriteLaborCost():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            TotalSQFT = 0
            while Line != '':
                SQFT = int(Line)
                TotalSQFT = TotalSQFT + SQFT
                Line = SquareFoot.readline()
            Gallons = TotalSQFT / 112
            TotalLabor = Gallons * 8
            TotalLaborCost = TotalLabor * 35
            FormatTotalLaborCost = "${:.2f}".format(TotalLaborCost)
            outfile.write(F'The total amount of labor cost is {FormatTotalLaborCost}\n')

    WriteLaborCost()

    # Writes the total cost to the text file FinalProject
    def WriteTotalCost():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            TotalSQFT = 0
            while Line != '':
                SQFT = int(Line)
                TotalSQFT = TotalSQFT + SQFT
                Line = SquareFoot.readline()
            Gallons = TotalSQFT / 112
            CostGallons = Gallons * 50
            TotalLabor = Gallons * 8
            TotalLaborCost = TotalLabor * 35
            CostTotal = TotalLaborCost + CostGallons
            FormatTotalCost = "${:.2f}".format(CostTotal)
            outfile.write(F'The total cost is {FormatTotalCost}\n')

    WriteTotalCost()

    # Writes the cost of each room to the text file FinalProject
    def WriteRoomsCost():
        with open('FinalProject.txt', 'a') as outfile:
            SquareFoot = open('rooms.txt')
            Line = SquareFoot.readline()
            Totalline = 0
            for line in range(1, 8 + 1):
                Lines = 1
                Totalline = Lines + Totalline
                SQFT = int(Line)
                Line = SquareFoot.readline()
                Gallons = SQFT / 112
                CostGallons = Gallons * 50
                TotalLabor = Gallons * 8
                TotalLaborCost = TotalLabor * 35
                CostTotal = TotalLaborCost + CostGallons
                FormatTotalCost = "${:.2f}".format(CostTotal)
                outfile.write(F'The total cost for room {Totalline} {FormatTotalCost}\n')

    WriteRoomsCost()


main()
