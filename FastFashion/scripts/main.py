import pandas as pd
import sys
sys.path.append( 'C:/Users/sonum/OneDrive/Desktop/FastFashion/scripts/GraphCode')
from GraphCode import BarGraph , createGraph
from DataCleaning import cleaning
from DataManupulation import ManupulateDataFunctions as mDf

carbonProducedByGender = pd.read_csv('data\carbonProducedByGender.csv');
carbonProducedByGeneration = pd.read_csv('data\carbonProducedByGeneration.csv');
FastFashionMain = pd.read_csv("data\FastFashionMain.csv");

mDf.manuplateDataMain(FastFashionMain);
createGraph.main(FastFashionMain);