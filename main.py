# This is a sample Python script.
#import display


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# key lengths


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Roller Screw and Range Percentages
    rollerScrewLength = 0.03  # 3 cm
    plantarRangePercent = 0.5  # 50%
    dorsiRangePercent = 0.5  # 50%

    # Total Allowable System Height
    height = 0.18  # 18 cm

    # Total Allowable System Width
    width = 0.070  # 7 cm

    # Total Allowable Front to back
    frontToBack = 0.1  # 10 cm

    # footplateHeight
    plateThickness = 0.005  # 5 mm
    platespace = 0.010  # 10 mm
    plateLength = 0.18  # 18 cm

    # Moment ratio
    momentRatio = 3  # ratio of force on screw from force on foot toe

    # Pin Location

    # Mass

    # Total Spring Stiffness
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    res = 30

    toeForce = 1000  # 1000 N

    xTry = np.linspace(0.01, 0.0655, res)
    yTry = np.linspace(plateThickness + platespace, 0.115, res)

    ankleJointCenterX = np.zeros(res)
    #ankleJointCenterY = np.linspace(plateThickness+platespace, 0.72,res)
    ankleJointCenterY = np.linspace(plateThickness+platespace, 0.3, res)

    # appliedMoment = (plateLength+xTry)*toeForce
    # screwForce = appliedMoment/(yTry)

    appliedMoment = np.zeros(res * res * res * res)
    screwForce = np.zeros(res * res * res * res)
    recordedXPin = np.zeros(res * res * res * res)
    recordedYPin = np.zeros(res * res * res * res)
    recordedAnkleX = np.zeros(res * res * res * res)
    recordedAnkleY = np.zeros(res * res * res * res)
    perceivedAnkleTorque = np.zeros(res * res * res * res)


    # IndexI = (len(A)**4)*i
    #         IndexII = IndexI+ii*(len(A)**3)
    #         IndexJ = IndexII+j*(len(A)**2)
    #         IndexK = IndexJ+k*(len(A)**1)
    #         IndexL = IndexK+l#*(len(A))

    for i in range(0, res):
        for j in range(0, res):
            for k in range(0, res):
                for p in range(0, res):
                    # print(index)
                    index = (i * res ** 3) + (j * res ** 2) + (k * res) + p
                    appliedMoment[index] = (plateLength + xTry[i]) * toeForce
                    screwForce[index] = appliedMoment[index] / (0.18-(0.036)-yTry[j]) # - ankleJointCenterY[k])
                    perceivedAnkleTorque[index] = screwForce[index]*(0.18-(0.036)-ankleJointCenterY[k])

                    recordedXPin[index] = xTry[i]
                    recordedYPin[index] = yTry[j]
                    recordedAnkleX[index] = ankleJointCenterX[p]
                    recordedAnkleY[index] = ankleJointCenterY[k]


    finalFrame = pd.DataFrame({'appliedMoment': appliedMoment, 'screwForce': screwForce, 'recordedXPin': recordedXPin,
                               'recordedYPin': recordedYPin, 'recordedAnkleX': recordedAnkleX,
                               'recordedAnkleY': recordedAnkleY, 'perceivedAnkleTorque': perceivedAnkleTorque})

    print(finalFrame)
    import plotly.express as px

    finalFrame = finalFrame[finalFrame['screwForce'] > 0]
    df = finalFrame[finalFrame['screwForce'] > 0]
    df = df[df['screwForce'] < 3000]
    df = df[df['perceivedAnkleTorque'] > 0]

    sortedFrame = df.sort_values(by=['perceivedAnkleTorque'], ascending=False)
    print(sortedFrame)

    

    fig = px.scatter_3d(df, x='recordedXPin', y='recordedYPin', z='recordedAnkleY',
                        color='perceivedAnkleTorque', opacity=0.7)

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    # pinX = 0
    # pinY = 0

    # screwForce = toeForce*momentRatio

    # maximize toeForce/screwForce
    # subject to

    # only goes up by 1mm

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
