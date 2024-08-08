# -*- coding:utf-8 -*-
# 指モーションのキャラクタライズのスクリプト
# unity-chanのモデルのキャラクタライズも可能

# SDK import
from pyfbsdk import*

# skeleton mapping template
SkeletonMapping = {
    # "Property Name"       :"Bone Name"
    "ReferenceLink"         :"Character1_Reference",
    "HipsLink"              :"Character1_Hips",
    "LeftUpLegLink"         :"Character1_LeftUpLeg",
    "LeftLegLink"           :"Character1_LeftLeg",
    "LeftFootLink"          :"Character1_LeftFoot",
    "RightUpLegLink"        :"Character1_RightUpLeg",
    "RightLegLink"          :"Character1_RightLeg",
    "RightFootLink"         :"Character1_RightFoot",
    "SpineLink"             :"Character1_Spine",
    "LeftArmLink"           :"Character1_LeftArm",
    "LeftForeArmLink"       :"Character1_LeftForeArm",
    "LeftHandLink"          :"Character1_LeftHand",
    "RightArmLink"          :"Character1_RightArm",
    "RightForeArmLink"      :"Character1_RightForeArm",
    "RightHandLink"         :"Character1_RightHand",
    "HeadLink"              :"Character1_Head",
    "LeftToeBaseLink"       :"Character1_LeftToeBase",
    "RightToeBaseLink"      :"Character1_RightToeBase",
    "LeftShoulderLink"      :"Character1_LeftShoulder",
    "RightShoulderLink"     :"Character1_RightShoulder",
    "NeckLink"              :"Character1_Neck",
    "Spine1Link"            :"Character1_Spine1",
    "Spine2Link"            :"Character1_Spine2",
    "LeftHandThumb1Link"    :"Character1_LeftHandThumb1",
    "LeftHandThumb2Link"    :"Character1_LeftHandThumb2",
    "LeftHandThumb3Link"    :"Character1_LeftHandThumb3",
    "LeftHandThumb4Link"    :"Character1_LeftHandThumb4",
    "LeftHandIndex1Link"    :"Character1_LeftHandIndex1",
    "LeftHandIndex2Link"    :"Character1_LeftHandIndex2",
    "LeftHandIndex3Link"    :"Character1_LeftHandIndex3",
    "LeftHandIndex4Link"    :"Character1_LeftHandIndex4",
    "LeftHandMiddle1Link"   :"Character1_LeftHandMiddle1",
    "LeftHandMiddle2Link"   :"Character1_LeftHandMiddle2",
    "LeftHandMiddle3Link"   :"Character1_LeftHandMiddle3",
    "LeftHandMiddle4Link"   :"Character1_LeftHandMiddle4",
    "LeftHandRing1Link"     :"Character1_LeftHandRing1",
    "LeftHandRing2Link"     :"Character1_LeftHandRing2",
    "LeftHandRing3Link"     :"Character1_LeftHandRing3",
    "LeftHandRing4Link"     :"Character1_LeftHandRing4",
    "LeftHandPinky1Link"    :"Character1_LeftHandPinky1",
    "LeftHandPinky2Link"    :"Character1_LeftHandPinky2",
    "LeftHandPinky3Link"    :"Character1_LeftHandPinky3",
    "LeftHandPinky4Link"    :"Character1_LeftHandPinky4",
    "RightHandThumb1Link"   :"Character1_RightHandThumb1",
    "RightHandThumb2Link"   :"Character1_RightHandThumb2",
    "RightHandThumb3Link"   :"Character1_RightHandThumb3",
    "RightHandThumb4Link"   :"Character1_RightHandThumb4",
    "RightHandIndex1Link"   :"Character1_RightHandIndex1",
    "RightHandIndex2Link"   :"Character1_RightHandIndex2",
    "RightHandIndex3Link"   :"Character1_RightHandIndex3",
    "RightHandIndex4Link"   :"Character1_RightHandIndex4",
    "RightHandMiddle1Link"  :"Character1_RightHandMiddle1",
    "RightHandMiddle2Link"  :"Character1_RightHandMiddle2",
    "RightHandMiddle3Link"  :"Character1_RightHandMiddle3",
    "RightHandMiddle4Link"  :"Character1_RightHandMiddle4",
    "RightHandRing1Link"    :"Character1_RightHandRing1",
    "RightHandRing2Link"    :"Character1_RightHandRing2",
    "RightHandRing3Link"    :"Character1_RightHandRing3",
    "RightHandRing4Link"    :"Character1_RightHandRing4",
    "RightHandPinky1Link"   :"Character1_RightHandPinky1",
    "RightHandPinky2Link"   :"Character1_RightHandPinky2",
    "RightHandPinky3Link"   :"Character1_RightHandPinky3",
    "RightHandPinky4Link"   :"Character1_RightHandPinky4",
}

if len(FBSystem().Scene.Characters) > 0:
    check = FBMessageBox("Caution", "Some Character already exists.\n"
                                    +"Are you sure you want to delete them and create one?",
                        "Yes", "No")

    # delete existing characters
    if check == 1:
        for i in range(len(FBSystem().Scene.Characters)):
            charaList = FBSystem().Scene.Characters
            charaList[0].FBDelete()

# create character
chara = FBCharacter("FingerMotion")

# characterize
for LinkPropName in SkeletonMapping.keys():
    prop = chara.PropertyList.Find(LinkPropName)
    bone = FBFindModelByLabelName(SkeletonMapping[LinkPropName])
    prop.append(bone)
chara.SetCharacterizeOn(True)

if chara.GetCharacterizeError() == "":
    FBMessageBox("Message", "Characterize succeeded!", "OK")
else:
    FBMessageBox("Caution", chara.GetCharacterizeError(), "OK")




from pyfbsdk import*

chara = FBSystem().Scene.Characters[0]

for prop in chara.PropertyList:
    if prop.Name.endswith("Link") and len(prop) > 0:
        name = "\"" + prop[0].Name.replace("Character1_","") + "\""
        print("{:<18}".format(name), ": ", prop[0].Rotation.Data, ",")


# link名とFBVector3dの辞書を作成する。

from pyfbsdk import*

RotationMapping = {
    "Reference"        :  FBVector3d(0, -0, 0) ,
    "Hips"             :  FBVector3d(0, -0, 0) ,
    "LeftUpLeg"        :  FBVector3d(-0.000852655, -2.13217, 0.0175715) ,
    "LeftLeg"          :  FBVector3d(-0.000290668, -0.000152101, -0.0281547) ,
    "LeftFoot"         :  FBVector3d(0.000351992, -0.000423606, 0.0121993) ,
    "RightUpLeg"       :  FBVector3d(0.000848652, -0.00031764, 0.0159872) ,
    "RightLeg"         :  FBVector3d(-0.000850103, 0.000159739, -0.0285801) ,
    "RightFoot"        :  FBVector3d(0.000145294, 0.000288231, 0.0122334) ,
    "Spine"            :  FBVector3d(0, -0, 0) ,
    "LeftArm"          :  FBVector3d(0.000678463, 0.00132968, -0.00213781) ,
    "LeftForeArm"      :  FBVector3d(-0.0141008, -0.0278999, 0.128709) ,
    "LeftHand"         :  FBVector3d(0, 12.5038, -0.000234894) ,
    "RightArm"         :  FBVector3d(-0.000678008, -0.00135688, -0.00215091) ,
    "RightForeArm"     :  FBVector3d(0.0147893, 0.0286026, 0.130203) ,
    "RightHand"        :  FBVector3d(0.000649952, 0.000928655, -0.00277338) ,
    "Head"             :  FBVector3d(0, -0, 0) ,
    "LeftToeBase"      :  FBVector3d(-0.0328897, -0, 0) ,
    "RightToeBase"     :  FBVector3d(-0.000155234, -0, 0.000403213) ,
    "LeftShoulder"     :  FBVector3d(0, -0, 0) ,
    "RightShoulder"    :  FBVector3d(0, -0, 0) ,
    "Neck"             :  FBVector3d(0, -0, 0) ,
    "Spine1"           :  FBVector3d(0, -0, 0) ,
    "Spine2"           :  FBVector3d(0, -0, 0) ,
    "LeftHandThumb1"   :  FBVector3d(0, -0, 0) ,
    "LeftHandThumb2"   :  FBVector3d(-0.000840823, 0.194818, -0.468221) ,
    "LeftHandThumb3"   :  FBVector3d(0, -0, 0) ,
    "LeftHandThumb4"   :  FBVector3d(0, -0, 0) ,
    "LeftHandIndex1"   :  FBVector3d(0, -0, 0) ,
    "LeftHandIndex2"   :  FBVector3d(0.0208647, -2.85136, 0.642927) ,
    "LeftHandIndex3"   :  FBVector3d(0, -0, 0) ,
    "LeftHandIndex4"   :  FBVector3d(0, -0, 0) ,
    "LeftHandMiddle1"  :  FBVector3d(0, -0, 0) ,
    "LeftHandMiddle2"  :  FBVector3d(0.007101, -2.85187, 1.60404) ,
    "LeftHandMiddle3"  :  FBVector3d(-1.1984, -2.16398, -1.71074) ,
    "LeftHandMiddle4"  :  FBVector3d(0, -0, 0) ,
    "LeftHandRing1"    :  FBVector3d(0, -0, 0) ,
    "LeftHandRing2"    :  FBVector3d(-0.00703902, -1.69498, -0.629432) ,
    "LeftHandRing3"    :  FBVector3d(0, -0, 0) ,
    "LeftHandRing4"    :  FBVector3d(0, -0, 0) ,
    "LeftHandPinky1"   :  FBVector3d(0, -0, 0) ,
    "LeftHandPinky2"   :  FBVector3d(0, -0.655605, 0) ,
    "LeftHandPinky3"   :  FBVector3d(0, -0, 0) ,
    "LeftHandPinky4"   :  FBVector3d(0, -0, 0) ,
    "RightHandThumb1"  :  FBVector3d(0, -0, 0) ,
    "RightHandThumb2"  :  FBVector3d(0.000823626, -0.194826, -0.468223) ,
    "RightHandThumb3"  :  FBVector3d(0, -0, 0) ,
    "RightHandThumb4"  :  FBVector3d(0, -0, 0) ,
    "RightHandIndex1"  :  FBVector3d(0, -0, 0) ,
    "RightHandIndex2"  :  FBVector3d(0.0649267, 1.23615, 0.303176) ,
    "RightHandIndex3"  :  FBVector3d(0, -0, 0) ,
    "RightHandIndex4"  :  FBVector3d(0, -0, 0) ,
    "RightHandMiddle1" :  FBVector3d(0, -0, 0) ,
    "RightHandMiddle2" :  FBVector3d(-0.0571507, -2.846, 0.346299) ,
    "RightHandMiddle3" :  FBVector3d(0, -0, 0) ,
    "RightHandMiddle4" :  FBVector3d(0, -0, 0) ,
    "RightHandRing1"   :  FBVector3d(0, -0, 0) ,
    "RightHandRing2"   :  FBVector3d(-0.133978, -1.63096, 0.736599) ,
    "RightHandRing3"   :  FBVector3d(0, -0, 0) ,
    "RightHandRing4"   :  FBVector3d(0, -0, 0) ,
    "RightHandPinky1"  :  FBVector3d(0, -0, 0) ,
    "RightHandPinky2"  :  FBVector3d(0, 0.655702, 0) ,
    "RightHandPinky3"  :  FBVector3d(0, -0, 0) ,
    "RightHandPinky4"  :  FBVector3d(0, -0, 0) ,
}

for key in RotationMapping.keys():
    bone = FBFindModelByLabelName(key)
    if not bone == None:
        #print(prop[0].Name , RotationMapping[key])
        bone.Rotation.Data = RotationMapping[key]

chara = FBSystem().Scene.Characters[0]

for prop in chara.PropertyList:
    if prop.Name.endswith("Link") and len(prop) > 0:
        print(prop[0].Rotation.Data)

for prop in chara.PropertyList:
    if prop.Name.endswith("Link") and len(prop) > 0:
        print(prop[0].Rotation.Data)


# preRotationに合わせてみる
for key in RotationMapping.keys():
    bone = FBFindModelByLabelName(key)
    if not bone == None:
        bone.Rotation.Data = bone.PreRotation