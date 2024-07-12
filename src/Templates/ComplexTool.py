# -*- coding: utf-8 -*-
# characterに関する情報を表示するスクリプト

from pyfbsdk import*
from pyfbsdk_additions import*

class Composition:
    def __init__(self):
        print("some additional class")

class SampleTool:
    def __init__(self, toolname:str):
        self.tool = FBCreateUniqueTool(toolname)
        self.tool.StartSizeX = 200
        self.tool.StartSizeY = 250
        self.UICreate(self.tool)
        self.UIConfigure(self.tool)

    def ReturnCreatedTool(self) -> FBTool:
        return self.tool

    ### list callback function
    def ListCallBack(self, control:FBList, event):
        print("list changed", "index : " + str(control.ItemIndex))

    ### button callback funtion
    def ButtonCallBack(self, control:FBButton, event):
        print("Button pushed")

    ### UI Creation funciton
    def UICreate(self, tool:FBTool):
        # UI Elements
        self.Label1 = FBLabel()
        self.List1 = FBList()
        self.Button1 = FBButton()

        lx = 10     # default x position
        ly = 10     # default y position
        lw = 180    # default width
        lh = 25     # default height

        # region for label
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("Label1","Label1", x, y, w, h)

        # region for character List
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly+lh,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("List1","List1", x, y, w, h)

        # region for Information Display
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly+lh*2,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("Button1","Button1", x, y, w, h)

        # grant control for each regiton to VisualComponents
        tool.SetControl("Label1", self.Label1)
        tool.SetControl("List1", self.List1)
        tool.SetControl("Button1", self.Button1)


    ### UI Configuration function
    def UIConfigure(self, tool:FBTool):
        self.Label1.Caption = "Label Sample"

        self.List1.style = FBListStyle.kFBDropDownList
        for i in range(5):
            # list item must be string
            self.List1.Items.append(str(i))
        self.List1.OnChange.Add(self.ListCallBack)
        
        self.Button1.Caption = "Button Sample"
        self.Button1.OnClick.Add(self.ButtonCallBack)

if __name__ in ('__main__', 'builtins'):
    t = SampleTool("Tool Name")
    ShowTool(t.ReturnCreatedTool())