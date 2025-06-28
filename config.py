from argparse import Namespace

config = Namespace(
    reference_date = "2024-11-29", # Ensure exchange is open on this day
    reference_nav = 14.64,
    reference_no_of_unit = 125345459,
    stock_dict = {"RY.TO": 8.6, "MFC.TO" : 8.3, "CM.TO" : 8.0, "SLF-PC.TO" : 7.4, 
                  "TRP.TO": 6.8, "TD.TO" : 6.3, "TRI.TO" : 5.7, "ENB.TO" : 5.3, 
                  "BNS.TO" : 6.3, "BMO.TO" : 5.2, "SU.TO" : 5.1, "NA.TO" : 5.0, 
                  "BCE.TO" : 4.1, "T.TO" : 2.8, "L.TO" : 1.6, "TA.TO" : 1.3,
                  "CIX.TO" : 1.0, "X.TO" : 0.9, "SOBO.TO" : 0.7, "AGF-B.TO" : 0.6,
                  "EMA.TO" : 0.2}, # Key is the ticker of the stock, value is the percentage held by the mutual fund
    cash = 9.6 # Percentage
)