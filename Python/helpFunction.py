def helpFx(helpstr):
    import pandas as pd
    Help = pd.read_csv('help_function.csv',sep=";")
    print(Help["Response"][Help["Call"]==helpstr].get_values()[0])