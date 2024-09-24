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
    def __init__(self,parent=None):
        super().__init__(parent)

        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")

        # Start from the index number 1 since index 0 doesn't count as Macronutrient, Vitamin, and/or Mineral.
        self.labelPie = self.choiceMacro.GetStrings()[1::]
        self.labelBar = self.choiceVitamin.GetStrings()[1::] + self.choiceMineral.GetStrings()[1::] + self.choiceOther.GetStrings()[1::]

        self.label = self.df.columns[1::]
        self.value = []

        # Remove/comment Line 61 if you want to see every column.
        self.df = self.df[["food"]]
        self.table = DataTable(self.df)

        self.foodData.SetTable(self.table, takeOwnership=True)
        self.foodData.EnableEditing(False)

        # Change SetColSize() to AutoSize() for testing
        self.foodData.SetColSize(0, 350)
        # self.foodData.AutoSize()

        self.Show(True)
        self.Layout()

    def test(self, event):
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

        self.foodData.SetGridCursor(row, col)

        # [row, 0] ensures that we only get the food name.
        foodName = self.df.iloc[row, 0]

        dataFrame = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        test = DataTable(dataFrame)
        test = test.data

        searchData = test["food"]

        loc = []
        for item in searchData:
            if re.findall(foodName, item):
                loc.append(True)
            else:
                loc.append(False)

        search_result = dataFrame[loc]
        labelAll = self.label

        percentageBar = []
        percentagePie = []

        valueBar = []
        valuePie = []

        for i in range(len(labelAll)):
            if labelAll[i] in self.labelBar:
                valueBar.append(search_result.iloc[0][labelAll[i]])
            elif labelAll[i] in self.labelPie:
                valuePie.append(search_result.iloc[0][labelAll[i]])

        """
        .concatenate had to be done for valueBar specifically straight up just because 
        Sodium comes up BEFORE the other minerals.
        
        My initial plan for valueBar is to include all values for the Vitamin first and then Minerals after that.
        """
        valueBar = np.concatenate((valueBar[1:-1], valueBar[0], valueBar[-1]), axis=None)
        for i in range(len(valuePie)):
            percentagePie.append(f"{self.labelPie[i]}: {(round((valuePie[i]/sum(valuePie))* 100, 2))}%")

        self.createPieChart(self, percentagePie, valuePie, colorPie)
        self.createBarChart(self, percentageBar, valueBar, colorBar)

    # def countPercentage(self, values):
    #     for value in values:
    #         percentage = [value/sum(values)] * 100
    #     return percentage

    def createPieChart(self, event, labelArray, valueArray, colorArray):
        pieChart = self.pieChartPlot(labelArray, valueArray, colorArray)
        h, w = self.pieChartPanel.GetSize()
        pieChart.set_size_inches(h / pieChart.get_dpi(), w / pieChart.get_dpi())
        canvas = FigureCanvasWxAgg(self.pieChartPanel, -1, pieChart)
        canvas.SetSize(self.pieChartPanel.GetSize())

    def createBarChart(self, event, labelArray, valueArray, colorArray):
        barChart = self.barChartPlot(labelArray, valueArray, colorArray)
        h, w = self.barChartPanel.GetSize()
        barChart.set_size_inches(h / barChart.get_dpi(), w / barChart.get_dpi())
        canvas = FigureCanvasWxAgg(self.barChartPanel, -1, barChart)
        canvas.SetSize(self.barChartPanel.GetSize())

    def barChartPlot(self, labelArray, valueArray, colorArray):
        x = self.labelBar
        y = valueArray
        colors = colorArray
        barChart, (ax1) = plt.subplots(1)

        barChart.subplots_adjust(top=0.93, bottom=0.25)

        bars = ax1.bar(x, y, color=colors)
        print(len(bars))

        for i in range(len(bars)):
            bar = bars[i]
            value = valueArray[i]
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, value, f'{height:.0f}', ha='center', va='bottom', fontsize="6")

        plt.yticks(fontsize=6)
        plt.xticks(rotation=90, fontsize=5.5)
        ax1.set_title(u'Bar', fontsize=7)
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

        ax1.set_title('Minerals')
        ax1.pie(sizes, explode=explode, colors=colors, shadow=True)
        ax1.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)

        ax1.axis('equal')
        return pieChart

    def searchFood( self, event ):
        key_word = self.searchInput.GetValue()

        # Ensures that only the food row is shown in the table.
        df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        df = df[["food"]]

        foods = df["food"]
        loc = []
        for item in foods:
            if re.findall(key_word, item):
                loc.append(True)
            else:
                loc.append(False)

        search_result = df[loc]
        tabel = DataTable(search_result)
        self.foodData.ClearGrid()
        self.foodData.SetTable(tabel,True)
        self.foodData.EnableEditing(False)

        self.foodData.SetColSize(0, 350)
        # self.foodData.AutoSize()

        num_rows = sum(loc)
        label_to_static_txt = "The number of rows: "+str(num_rows)
        self.extraInfo.SetLabel(label_to_static_txt)

        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()