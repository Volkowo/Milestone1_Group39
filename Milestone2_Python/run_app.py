import wx
import wx.grid
import pandas as pd
import re

from template_frame import NutritionApp as Frame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


class CalcFrame(Frame1):
    def __init__(self,parent=None):
        super().__init__(parent)

        global FilterMacro
        global FilterVitamin
        global FilterMineral
        global FilterOther

        FilterMacro = ""
        FilterVitamin = ""
        FilterMineral = ""
        FilterOther = ""

        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        pd.set_option('display.max_rows', self.df.shape[0] + 1)
        print(self.df)

        # Remove/comment Line 47 if you want to see every column.
        # self.df = self.df[["food"]]
        self.table = DataTable(self.df)

        self.foodData.SetTable(self.table, takeOwnership=True)

        # Change every line that has "self.foodData.SetColSize(0, 350)" to "self.foodData.AutoSize()"
        # self.foodData.AutoSize()
        self.foodData.SetColSize(0, 350)

        self.Show(True)
        self.Layout()

    def filterFood( self, event ):
        Macro = self.choiceMacro.GetSelection()
        Vitamin = self.choiceVitamin.GetSelection()
        Mineral = self.choiceMineral.GetSelection()
        Other = self.choiceOther.GetSelection()
        minValueInput = self.minValueInput.GetValue()
        maxValueInput = self.maxValueInput.GetValue()
        nutritionLevel = self.nutritionLevelFilter.GetSelection()
        choiceDiet = self.choiceDiet.GetSelection()

        if minValueInput == "":
            minValueInput = 0
        else:
            for i in minValueInput:
                if i.isalpha():
                    minValueInput = 0


        if maxValueInput == "":
            maxValueInput = 99999

        else:
            for i in maxValueInput:
               if i.isalpha():
                  maxValueInput = 99999

        self.makeSerchStatment(Macro, Vitamin, Mineral, Other, minValueInput ,maxValueInput, nutritionLevel, choiceDiet)





    def searchFood( self, event):

        #sets the df to the table
        df = self.table.data


        #initalises the filter condition
        filter_condition = pd.Series([True] * len(df))

        #pulls the min and the max values
        minValueInput = self.minValueInput.GetValue()
        maxValueInput = self.maxValueInput.GetValue()


        #chacks for if the min value is empty or not
        if minValueInput == "":
            #if its left empty set it to 0
            minValueInput = 0
        else:
            #loops through and checks if it has letter
            for i in minValueInput:
                if i.isalpha():
                    # if its left empty set it to 0
                    minValueInput = 0
            #makes the value a float inseatd of a string
            minValueInput = float(minValueInput)

        # chacks for if the max value is empty or not
        if maxValueInput == "":
            maxValueInput = 99999

        else:
            for i in maxValueInput:
                # loops through and checks if it has a letter
                if i.isalpha():
                    # if its left empty set it to a high number
                    maxValueInput = 99999
            # makes the value a float inseatd of a string
            maxValueInput = float(maxValueInput)

        #adds all the filtered options to the search if there not empty (aka the defult was selected)
        if FilterOther != "":
            filter_condition &= (df[FilterOther] >= minValueInput) & (df[FilterOther] <= maxValueInput)

        if FilterMineral != "":
            filter_condition &= (df[FilterMineral] >= minValueInput) & (df[FilterMineral] <= maxValueInput)

        if FilterVitamin != "":
            filter_condition &= (df[FilterVitamin] >= minValueInput) & (df[FilterVitamin] <= maxValueInput)

        if FilterMacro != "":
            filter_condition &= (df[FilterMacro] >= minValueInput) & (df[FilterMacro] <= maxValueInput)


        #searchess based on the key word uses strip and lower to remove case sensitivity
        key_word = self.searchInput.GetValue().strip().lower()
        #runs only if key word is not empty
        if key_word:
            filter_condition &= df['food'].str.contains(key_word, case=False, na=False)

        #runs the search using the made filter conditions
        filtered_df = df[filter_condition]
        print(filtered_df)

        #make the table of data
        self.foodData.ClearGrid()
        self.foodData.BeginBatch()
        self.foodData.SetTable(DataTable(filtered_df), True)
        self.foodData.EndBatch()
        self.foodData.AutoSize()


        self.foodData.SetColSize(0, 350)


        #returns  the result of the number of results
        self.extraInfo.SetLabel(f"Results found: {len(filtered_df)}")

        self.Layout()



    def makeSerchStatment(self, Macro, Vitamin, Mineral, Other, minValueInput ,maxValueInput, nutritionLevel, choiceDiet):
        # comment/Uncomment the below prints to see the value of each when filter button is pressed
        print("===========================")
        print("Macro: ", Macro)
        print("Vitamin :", Vitamin)
        print("Mineral :", Mineral)
        print("Other :", Other)
        print("minValueInput :", minValueInput)
        print("maxValueInput :", maxValueInput)
        print("nutritionLevel :", nutritionLevel)
        print("choiceDiet :", choiceDiet)
        print("===========================")


        self.searchText = ""

        #sets the filtered options as global so that they can be used in the search function
        global FilterMacro
        global FilterVitamin
        global FilterMineral
        global FilterOther

        #sets what mactro is selected
        if Macro != 0:
            if Macro == 1:
                Macro = "Fat"
            elif Macro == 2:
                Macro = "Saturated Fats"
            elif Macro == 3:
                Macro = "Monounsaturated Fats"
            elif Macro == 4:
                Macro = "Polyunsaturated Fats"
            elif Macro == 5:
                Macro = "Carbohydrates"
            elif Macro == 6:
                Macro = "Sugars"
            elif Macro == 7:
                Macro = "Protein"
            elif Macro == 8:
                 Macro = "Dietary Fiber"

            #addes the selected macro to the console so you can see the result
            print("Selected macro: ", Macro)

            #sets the filtered macro for later use in the search function
            FilterMacro = Macro

        # sets what Vitamin is selected
        if Vitamin != 0:
            if Vitamin == 1:
                Vitamin = "Vitamin B1"
            elif Vitamin == 2:
                Vitamin = "Vitamin B2"
            elif Vitamin == 3:
                Vitamin = "Vitamin B3"
            elif Vitamin == 4:
                Vitamin = "Vitamin B5"
            elif Vitamin == 5:
                Vitamin = "Vitamin B6"
            elif Vitamin == 6:
                Vitamin = "Vitamin B11"
            elif Vitamin == 7:
                Vitamin = "Vitamin B12"
            elif Vitamin == 8:
                Vitamin = "Vitamin C"
            elif Vitamin == 9:
                Vitamin = "Vitamin D"
            elif Vitamin == 10:
                Vitamin = "Vitamin E"
            elif Vitamin == 11:
                Vitamin = "Vitamin K"


            # sets the filtered Vitamin for later use in the search function
            FilterVitamin = Vitamin

            # addes the selected Vitamin to the console so you can see the result
            print("Selected Vitamin: ", Vitamin)



        # sets what Vitamin is selected
        if Mineral != 0:
            if Mineral == 1:
                Mineral = "Calcium"
            elif Mineral == 2:
                Mineral = "Copper"
            elif Mineral == 3:
                Mineral = "Iron"
            elif Mineral == 4:
                Mineral = "Magnesium"
            elif Mineral == 5:
                Mineral = "Manganese"
            elif Mineral == 6:
                Mineral = "Phosphorus"
            elif Mineral == 7:
                Mineral = "Potassium"
            elif Mineral == 8:
                Mineral = "Selenium"
            elif Mineral == 9:
                Mineral = "Zinc"

            # sets the filtered Mineral for later use in the search function
            FilterMineral = Mineral

            # addes the selected Mineral to the console so you can see the result
            print("Selected Mineral: ", Mineral)


        # sets what Other is selected
        if Other != 0:
            if Other == 1:
                Other = "Cholesterol"
            elif Other == 2:
                Other = "Water"
            elif Other == 3:
                Other = "Nutrition Density"

            # sets the filtered Other for later use in the search function
            FilterOther = Other

            # addes the selected Other to the console so you can see the result
            print("Selected Other: ", Other)




if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()