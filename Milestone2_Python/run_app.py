import wx.grid
import matplotlib

matplotlib.use('WXAgg')
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

import wx
import wx.grid
import pandas as pd
import re

from all_functions import *
from template_frame import NutritionApp as Frame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

colorBar = [
    '#FF5733',
    '#33FF57',
    '#3357FF',
    '#FF33FF',
    '#FFFF33',
    '#FF8C33',
    '#33FFF6',
    '#9933FF',
    '#FF3333',
    '#33FF99',
    '#3375FF',
    '#FF3399',
    '#FFC300',
    '#DAF7A6',
    '#C70039',
    '#900C3F',
    '#581845',
    '#FFC0CB',
    '#6495ED',
    '#B8860B',
    '#7FFF00',
    '#FF6347'
]

colorPie = [
    '#FF5733',
    '#33FF57',
    '#3357FF',
    '#FFFF33',
    '#FF33FF',
    '#33FFF6',
    '#9933FF',
    '#B8860B'
]


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
    def __init__(self, parent=None):
        super().__init__(parent)

        self.dfMergeResult = pd.DataFrame(columns=["food"])

        self.dfMacro_value = []
        self.dfVitamin_value = []
        self.dfMineral_value = []
        self.dfOther_value = []

        self.searchResult_value = []
        self.searchResult_valueFinal = []
        self.searchResult_level = []
        self.searchResult_diet = []

        FilterMacro = ""
        FilterVitamin = ""
        FilterMineral = ""
        FilterOther = ""
        diet = 0

        # Remove/comment the line below if you want to see every column.
        self.df = loadData(r"Food_Nutrition_Dataset.csv", True)
        self.loadTable(self.df)

        listOfMacro = self.choiceMacro.GetStrings()
        listOfVitamin = self.choiceVitamin.GetStrings()
        listOfMineral = self.choiceMineral.GetStrings()
        listOfOthers = self.choiceOther.GetStrings()

        self.labelPie, self.labelBar = getLabelPieBar(listOfMacro, listOfVitamin, listOfMineral, listOfOthers)
        # print(self.labelPie)
        # print(self.labelBar)
        # THIS IS SPECIFICALLY FOR self.label which is the whole label
        dataForLabel = pd.read_csv(r"Food_Nutrition_Dataset.csv")
        self.label = list(dataForLabel.columns[1::])

        self.value = []

        self.Show(True)
        self.Layout()

        # USED FOR FILTER - NUTRITION LEVEL
        dataFrame_dict = loadData(r"Food_Nutrition_Dataset.csv")
        self.maxValueDict = findNutritionValue(self.label, dataFrame_dict)
        print(self.maxValueDict)

    def searchFood(self, event):
        keyWord = self.searchInput.GetValue()
        keyWord = keyWord.lower()

        # Ensures that only the food row is shown in the table.
        dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", True)

        search_result = determineFoodSearch(dataFrame, self.dfMergeResult, keyWord)

        self.df = search_result
        self.foodData.ClearGrid()
        self.loadTable(search_result)
        self.Layout()

    def nutritionBreakdown(self, event):
        """
        I found out that adding a custom function in "OnGridCellLeftClick" does some
        funny stuff to the default behavior.
        What I mean is that there was no grid at all when we click on a column because
        I assigned "OnGridCellLeftClick" to a new function.

        .SetGridCursor() allows us to replicate the default behavior where the column we are currently clicking at
        will have a border/grid around it. There might be a better way to do this, but I can't be asked.
        """

        # This also lets us get the name the content that's in that row.
        row = event.GetRow()
        col = event.GetCol()

        # "Highlights" the current column that's being chosen
        self.foodData.SetGridCursor(row, col)

        # [row, 0] ensures that we only get the food name.
        foodName = self.df.iloc[row, 0]
        # print(foodName)

        # Searches for the food(s) based on user's CLICK input
        dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
        searchData = dataFrame["food"]

        loc = []
        loc = findResult_generic(foodName, searchData)
        search_result = dataFrame[loc]

        # Iterate and store each nutrient to the appropriate place.
        # Anything related to Vitamin goes to the array that's for pie chart, while the rest goes to the bar chart.
        labelAll = self.label
        percentageBar = []
        percentagePie = []
        valueBar = []
        valuePie = []

        # print(search_result.iloc[0])

        valueBar, valuePie = findResult_breakdown(labelAll, self.labelBar, search_result)
        # print(valueBar, valuePie)

        valueBar = concatBarX(valueBar)
        percentagePie = createLabel(valuePie, self.labelPie)

        self.createChart(self.pieChartPlot(percentagePie, valuePie, colorPie), self.pieChartPanel)
        self.createChart(self.barChartPlot(percentageBar, valueBar, colorBar), self.barChartPanel)

    def explanationText(self, event):
        radioValue = self.nutritionLevelFilter.GetStringSelection()
        labelText = checkRadio(radioValue)
        self.text_filterResult.SetLabel(labelText)

    def explanationText_diet(self, event):
        dietDropdown = self.choiceDiet.GetStringSelection()
        labelText = checkDiet(dietDropdown)
        self.text_filterResult.SetLabel(labelText)

    def filterFood(self, event):
        # .GetStringCollection() -> Gets the string
        # .GetSelection() -> gets the number

        # Resets the value everytime the filter button is clicked
        self.searchResult_value = []
        self.searchResult_valueFinal = pd.DataFrame(self.searchResult_value, columns=["food"])
        self.searchResult_level = pd.DataFrame(self.searchResult_level, columns=["food"])
        self.searchResult_diet = pd.DataFrame(self.searchResult_diet, columns=["food"])

        macro = self.choiceMacro.GetStringSelection()
        vitamin = self.choiceVitamin.GetStringSelection()
        mineral = self.choiceMineral.GetStringSelection()
        other = self.choiceOther.GetStringSelection()
        nutritionLevel = self.nutritionLevelFilter.GetStringSelection()
        nutrientFilter = self.choiceNutrient.GetStringSelection()
        diet = self.choiceDiet.GetStringSelection()

        # MIN/MAX VALUE - NUTRITION VALUE
        minMacro = self.minValueInput_macro.GetValue()
        maxMacro = self.maxValueInput_macro.GetValue()

        minVitamin = self.minValueInput_vitamin.GetValue()
        maxVitamin = self.maxValueInput_vitamin.GetValue()

        minMineral = self.minValueInput_mineral.GetValue()
        maxMineral = self.maxValueInput_mineral.GetValue()

        minOther = self.minValueInput_other.GetValue()
        maxOther = self.maxValueInput_other.GetValue()

        defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
        dropdownArray = [macro, vitamin, mineral, other]
        minArray = [minMacro, minVitamin, minMineral, minOther]
        maxArray = [maxMacro, maxVitamin, maxMineral, maxOther]

        # ARRAY AND VARIABLES FOR FILTERS:
            # FOR FINAL RESULT
        searchResultMsg = ""
        mergeResult = []

            # FOR LEVEL FILTER
        errorRadio = ""
        errorDropdown = ""
        errorRadio = False
        errorDropdown = False

            # FOR VALUE FILTER
        errorMsgOne = ""
        errorMsgTwo = ""
        errorMsgThree = ""
        isError_filterValue = True
        isError_filterLevel = True
        isNotChosen_filterDiet = True
        errorNutrient = []
        errorValue = []
        errorComparison = []


        # ERROR CHECKING
        # A. Nutrition Value
        print(dropdownArray, minArray, maxArray)
        searchResultArray_value = []

        errorNutrient, errorValue, errorComparison, isError_filterValue = checkDropdownAndInput_value(
            dropdownArray,
            minArray,
            maxArray,
            isError_filterValue,
            searchResultArray_value
        )

        errorMsgOne, errorMsgTwo, errorMsgThree = generateErrorMessage_value(
            errorNutrient,
            errorValue,
            errorComparison)

        # B. Nutrition Level
        errorRadio, errorDropdown, isError_filterLevel = checkRadioAndDropdown_level(nutritionLevel,
                                                                                          nutrientFilter)

        # SETTING THE ERROR MESSAGE
        self.errorMsg_filterValue1.SetLabel(errorMsgOne)
        self.errorMsg_filterValue2.SetLabel(errorMsgTwo)
        self.errorMsg_filterValue3.SetLabel(errorMsgThree)
        self.errorMsg_level1.SetLabel(errorRadio)
        self.errorMsg_level2.SetLabel(errorDropdown)

        errorMessages = [errorMsgOne, errorMsgTwo, errorMsgThree, errorRadio, errorDropdown]

        # Checks for error and do the filter (if there are no errors)
        self.searchResult_valueFinal, self.searchResult_level, self.searchResult_diet = errorChecking_filters(
            isError_filterValue,
            isError_filterLevel,
            searchResultArray_value,
            self.maxValueDict,
            nutrientFilter,
            nutritionLevel,
            diet
        )

        # MERGE RESULT(S); Yeah there are a lot of parameters for this one.
        mergeResult, searchResultMsg = processFinalResult(
            isError_filterValue,
            minArray,
            isError_filterLevel,
            nutritionLevel,
            self.searchResult_valueFinal,
            self.searchResult_level,
            self.searchResult_diet,
            errorMessages,
            defaultDropdown,
            dropdownArray,
            minArray,
            maxArray,
            nutritionLevel,
            nutrientFilter,
            diet
        )

        if mergeResult is not None:
            self.text_filterResult.SetLabel(searchResultMsg)
            self.dfMergeResult = mergeResult
            self.df = mergeResult

            if len(mergeResult) > 0:
                self.foodData.ClearGrid()
                self.loadTable(self.dfMergeResult)
                self.Layout()

        self.text_filterResult.SetLabel(searchResultMsg)
        print("FINAL RESULT:", mergeResult)

    def resetFilter( self, event ):
        self.choiceMacro.SetSelection(0)
        self.minValueInput_macro.SetLabelText("")
        self.maxValueInput_macro.SetLabelText("")

        self.choiceVitamin.SetSelection(0)
        self.minValueInput_vitamin.SetLabelText("")
        self.maxValueInput_vitamin.SetLabelText("")

        self.choiceMineral.SetSelection(0)
        self.minValueInput_mineral.SetLabelText("")
        self.maxValueInput_mineral.SetLabelText("")

        self.choiceOther.SetSelection(0)
        self.minValueInput_other.SetLabelText("")
        self.maxValueInput_other.SetLabelText("")

        self.nutritionLevelFilter.SetSelection(0)
        self.choiceNutrient.SetSelection(0)

        self.choiceDiet.SetSelection(0)

        self.errorMsg_filterValue2.SetLabel("")
        self.errorMsg_filterValue1.SetLabel("")
        self.errorMsg_filterValue3.SetLabel("")
        self.errorMsg_level1.SetLabel("")
        self.errorMsg_level2.SetLabel("")
        self.text_extraFilterInfo.SetLabel("")
        self.text_filterResult.SetLabel("")


# UI Related
    def createChart(self, plotChart, panel):
        chart = plotChart
        h, w = panel.GetSize()
        chart.set_size_inches(h / chart.get_dpi(), w / chart.get_dpi())
        canvas = FigureCanvasWxAgg(panel, -1, chart)
        canvas.SetSize(panel.GetSize())

    def barChartPlot(self, labelArray, valueArray, colorArray):
        x = self.labelBar
        y = valueArray
        colors = colorArray
        barChart, (ax1) = plt.subplots(1)

        barChart.subplots_adjust(top=0.93, bottom=0.25)

        bars = ax1.bar(x, y, color=colors)
        # print(len(bars))

        """
        The code to set the text above the bars were mostly obtained from Stackoverflow:
        https://stackoverflow.com/questions/40489821/how-to-write-text-above-the-bars-on-a-bar-plot-python
        
        However, I modified the code to fit it into the context of this software.
        """
        for i in range(len(bars)):
            bar = bars[i]
            value = valueArray[i]
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, value, f'{height:.0f}', ha='center', va='bottom',
                     fontsize="6")

        plt.yticks(fontsize=6)

        # Rotates the label in x axis by 90 degress
        plt.xticks(rotation=90, fontsize=7)
        ax1.set_title('Vitamins, Macronutrients, and Others', fontsize=9)
        return barChart

    def pieChartPlot(self, labelArray, valueArray, colorArray):
        labels = labelArray
        sizes = valueArray
        colors = colorArray

        # Since the value of explode will be same for every section, we can just multiply the array with the label's length
        explode = [0.05] * len(self.labelPie)
        pieChart, (ax1) = plt.subplots(1)

        # Moves the chart to the left. This was done so we can see the legend as well
        pieChart.subplots_adjust(left=0.1, right=0.5)

        ax1.set_title('Minerals', fontsize=9)
        ax1.pie(sizes, explode=explode, colors=colors, shadow=True)

        # This lets us set the legend to the right side of the chart.
        ax1.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=7)

        ax1.axis('equal')
        return pieChart

    def loadTable(self, dataFrame):
        table = DataTable(dataFrame)
        self.foodData.SetTable(table, takeOwnership=True)
        self.foodData.EnableEditing(False)
        self.foodData.SetColSize(0, 350)


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
