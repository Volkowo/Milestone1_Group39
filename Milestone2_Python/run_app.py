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

        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        self.df = self.df[["food"]]
        self.table = DataTable(self.df)

        self.foodData.SetTable(self.table, takeOwnership=True)
        self.foodData.SetColSize(0, 350)

        self.Show(True)
        self.Layout()

    def searchFood( self, event ):
        key_word = self.searchInput.GetValue()

        df = self.table.data

        descs = df["food"]
        loc = []
        for item in descs:
            if re.search(key_word, item):
                loc.append(True)
            else:
                loc.append(False)

        search_result = df[loc]
        tabel = DataTable(search_result)
        self.foodData.ClearGrid()
        self.foodData.SetTable(tabel,True)
        self.foodData.SetColSize(0, 350)

        num_rows = sum(loc)
        label_to_static_txt = "The number of rows: "+str(num_rows)
        self.extraInfo.SetLabel(label_to_static_txt)

        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()