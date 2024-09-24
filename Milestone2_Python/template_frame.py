# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class NutritionApp
###########################################################################

class NutritionApp ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1200,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        everything = wx.BoxSizer( wx.VERTICAL )

        searchBarAndTable = wx.BoxSizer( wx.HORIZONTAL )

        self.searchInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        searchBarAndTable.Add( self.searchInput, 0, wx.ALL|wx.EXPAND, 5 )


        searchBarAndTable.Add( ( 10, 0), 0, 0, 5 )

        self.searchButton = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        searchBarAndTable.Add( self.searchButton, 0, wx.ALL, 5 )

        self.extraInfo = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.extraInfo.Wrap( -1 )

        searchBarAndTable.Add( self.extraInfo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        everything.Add( searchBarAndTable, 0, wx.EXPAND, 5 )

        filter_nutritionValue = wx.BoxSizer( wx.HORIZONTAL )

        choiceMacroChoices = [ _(u"Macronutrients"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber") ]
        self.choiceMacro = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMacroChoices, 0 )
        self.choiceMacro.SetSelection( 0 )
        filter_nutritionValue.Add( self.choiceMacro, 0, wx.ALL, 5 )

        choiceVitaminChoices = [ _(u"Vitamins"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K") ]
        self.choiceVitamin = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceVitaminChoices, 0 )
        self.choiceVitamin.SetSelection( 0 )
        filter_nutritionValue.Add( self.choiceVitamin, 0, wx.ALL, 5 )

        choiceMineralChoices = [ _(u"Minerals"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Sodium"), _(u"Zinc") ]
        self.choiceMineral = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMineralChoices, 0 )
        self.choiceMineral.SetSelection( 0 )
        filter_nutritionValue.Add( self.choiceMineral, 0, wx.ALL, 5 )

        choiceOtherChoices = [ _(u"Others"), _(u"Cholesterol"), _(u"Water"), _(u"Nutrition Density"), _(u"Caloric Value") ]
        self.choiceOther = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceOtherChoices, 0 )
        self.choiceOther.SetSelection( 3 )
        filter_nutritionValue.Add( self.choiceOther, 0, wx.ALL, 5 )

        self.minValueText = wx.StaticText( self, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minValueText.Wrap( -1 )

        filter_nutritionValue.Add( self.minValueText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.minValueInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValue.Add( self.minValueInput, 0, wx.ALL, 5 )

        self.maxValueText = wx.StaticText( self, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.maxValueText.Wrap( -1 )

        filter_nutritionValue.Add( self.maxValueText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.maxValueInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValue.Add( self.maxValueInput, 0, wx.ALL, 5 )


        everything.Add( filter_nutritionValue, 0, wx.EXPAND, 5 )

        filter_nutritionLevel = wx.BoxSizer( wx.HORIZONTAL )

        nutritionLevelFilterChoices = [ _(u"None"), _(u"Low"), _(u"Medium"), _(u"High") ]
        self.nutritionLevelFilter = wx.RadioBox( self, wx.ID_ANY, _(u"Nutrition Level Filter"), wx.DefaultPosition, wx.DefaultSize, nutritionLevelFilterChoices, 1, wx.RA_SPECIFY_COLS )
        self.nutritionLevelFilter.SetSelection( 0 )
        filter_nutritionLevel.Add( self.nutritionLevelFilter, 1, wx.ALL, 5 )


        everything.Add( filter_nutritionLevel, 0, wx.TOP|wx.EXPAND, 5 )

        filter_dietaryNeeds = wx.BoxSizer( wx.HORIZONTAL )

        choiceDietChoices = [ _(u"Dietary Needs"), _(u"Ketogenic Diet"), _(u"Low Sodium Diet"), _(u"Low Cholesterol Diet") ]
        self.choiceDiet = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDietChoices, 0 )
        self.choiceDiet.SetSelection( 0 )
        filter_dietaryNeeds.Add( self.choiceDiet, 0, wx.ALL, 5 )

        self.filterButton = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_dietaryNeeds.Add( self.filterButton, 0, wx.ALL, 5 )


        everything.Add( filter_dietaryNeeds, 0, wx.EXPAND, 5 )

        tableAndChart = wx.BoxSizer( wx.HORIZONTAL )

        table = wx.BoxSizer( wx.VERTICAL )

        self.foodData = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

        # Grid
        self.foodData.CreateGrid( 5, 5 )
        self.foodData.EnableEditing( True )
        self.foodData.EnableGridLines( True )
        self.foodData.EnableDragGridSize( False )
        self.foodData.SetMargins( 0, 0 )

        # Columns
        self.foodData.EnableDragColMove( False )
        self.foodData.EnableDragColSize( True )
        self.foodData.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.foodData.EnableDragRowSize( True )
        self.foodData.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.foodData.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        table.Add( self.foodData, 1, wx.ALL, 5 )


        tableAndChart.Add( table, 0, 0, 5 )

        chart = wx.BoxSizer( wx.VERTICAL )

        self.pieChartPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        chart.Add( self.pieChartPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.barChartPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        chart.Add( self.barChartPanel, 1, wx.EXPAND |wx.ALL, 5 )


        tableAndChart.Add( chart, 1, wx.EXPAND, 5 )


        everything.Add( tableAndChart, 1, wx.EXPAND, 5 )


        self.SetSizer( everything )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.searchButton.Bind( wx.EVT_BUTTON, self.searchFood )
        self.filterButton.Bind( wx.EVT_BUTTON, self.filterFood )
        self.foodData.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.test )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def searchFood( self, event ):
        event.Skip()

    def filterFood( self, event ):
        event.Skip()

    def test( self, event ):
        event.Skip()


