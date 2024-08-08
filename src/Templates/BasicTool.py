# -*- coding: utf-8 -*-
# 基本的なツールのテンプレート

from pyfbsdk import *
from pyfbsdk_additions import *

def PopulateLayout(tool:FBTool):
    x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
    tool.AddRegion("MainRegion","RegionName", x, y, w, h)
    
    vbox = FBVBoxLayout( FBAttachType.kFBAttachTop )
    tool.SetControl("MainRegion",vbox)
    
    Label1 = FBLabel()
    Label1.Caption = "Label1"
    vbox.Add(Label1, 30)

    List1 = FBList()
    List1.style = FBListStyle.kFBDropDownList
    for i in range(5):
        # list item must be string
        List1.Items.append(str(i))
    vbox.Add(List1, 30, space = 10)

    Button1 = FBButton()
    Button1.Caption = "Button1"
    vbox.Add(Button1, 10, space = 10, width = 200, height = 50)


def CreateTool():
    # Tool creation will serve as the hub for all other controls
    # t = FBCreateUniqueTool("BasicTool")
    t = FBCreateUniqueTool("Vertical sample")
    t.StartSizeX = 400
    t.StartSizeY = 400
    PopulateLayout(t)    
    ShowTool(t)

CreateTool()