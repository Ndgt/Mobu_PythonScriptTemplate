# -*- coding: utf-8 -*-
# characterに関する情報を表示するスクリプト

from pyfbsdk import*
from pyfbsdk_additions import*

class CharaInfo:
    def __init__(self, chara:FBCharacter):
        self.sum_BoneNum = 0
        self.Referece = False
        self.CollectInfo(chara)

    def CollectInfo(self, target:FBCharacter):
        for prop in target.PropertyList:
            # survey sum_BoneNum
            if prop.Name.endswith("Link") and len(prop) > 0:
                self.sum_BoneNum += 1

            # survey Reference
            if prop.Name == "ReferenceLink":
                if len(prop) > 0:
                    self.Referece = True
        
    def ReturnBoneNum(self) -> int:
        return self.sum_BoneNum
    
    def IsSetReference(self) -> str:
        if self.Referece:
            return "Yes"
        else:
            return "No"
        

class CharaInfoTool:
    def __init__(self, toolname:str):
        self.tool = FBCreateUniqueTool(toolname)
        self.tool.StartSizeX = 200
        self.tool.StartSizeY = 250
        self.UICreate(self.tool)
        self.UIConfigure(self.tool)

    def ReturnCreatedTool(self) -> FBTool:
        return self.tool

    def DisplayUpdate(self, database:CharaInfo):
        self.InfoDisplay.Caption = str(database.ReturnBoneNum()) + "\n" \
                                 + database.IsSetReference()
    
    ### when character list changed
    def ListCallBack(self, control, event):
        idx = control.ItemIndex
        chara = FBSystem().Scene.Characters[idx]
        self.DisplayUpdate(CharaInfo(chara))

    ### UI Creation funciton
    def UICreate(self, tool):
        # UI Elements
        self.ListTitleLabel = FBLabel()
        self.charaList = FBList()
        self.InfoDisplay = FBLabel()

        lx = 10     # default x position
        ly = 10     # default y position
        lw = 180    # default width
        lh = 25     # default height

        # region for label
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("ListTitleLabel","ListTitleLabel", x, y, w, h)

        # region for character List
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly+lh,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("charaList","charaList", x, y, w, h)

        # region for Information Display
        x = FBAddRegionParam(lx,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(ly+lh*2+10,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(lw,FBAttachType.kFBAttachLeft,"")
        h = FBAddRegionParam(lh,FBAttachType.kFBAttachNone,"")
        tool.AddRegion("InfoDisplay","InfoDisplay", x, y, w, h)

        # grant control for each regiton to VisualComponents
        tool.SetControl("ListTitleLabel", self.ListTitleLabel)
        tool.SetControl("charaList", self.charaList)
        tool.SetControl("InfoDisplay", self.InfoDisplay)


    ### UI Configuration function
    def UIConfigure(self, tool):
        self.ListTitleLabel.Caption = "Character:"
    
        self.charaList.Style = FBListStyle.kFBDropDownList
        for chara in FBSystem().Scene.Characters:
            self.charaList.Items.append(chara.Name)
        self.charaList.OnChange.Add(self.ListCallBack) # connect callback
        
        if len(self.charaList.Items) != 0:
            chara = FBSystem().Scene.Characters[0]
            self.DisplayUpdate(CharaInfo(chara))


if __name__ in ('__main__', 'builtins'):
    t = CharaInfoTool("charcter Information")
    ShowTool(t.ReturnCreatedTool())