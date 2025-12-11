import pandas as pd

# Load CSV
IEP_df = pd.read_csv("IEP_df_interpolated.csv", low_memory=False)

# Strip any whitespace from column names (common source of errors)
IEP_df.columns = IEP_df.columns.str.strip()

#==============================
# Effluent Treatment Data
#==============================


# List of columns (tags) you want to pull
tags_of_interest = [
    "255FI305_MV",
    "301BOD136.RMV",
    "301BOD450",
    "301CI051_ALM",
    "301CI061_ALM",
    "301DO002_MV",
    "301DO003_MV",
    "301FC053",
    "301FC063",
    "301FC251",
    "301FC260",
    "301FC301",
    "301FC302",
    "301FC303",
    "301FC421_MV",
    "301FI012_RMV",
    "301FI681_MV",
    "301LI592",
    "301LT440_MV",
    "301LT524_MV",
    "301OI001.MV",
    "301OPC051_MV",
    "301OPC061_MV",
    "301ORP420_MV",
    "301PHI136_MV",
    "301TI570",
    "301TT410_MV",
    "402FI112.MV",
    "525FI900.MV"
]

# Pull only the columns you want into a new DataFrame
effluent_treatment_df = IEP_df[tags_of_interest]

# Check the result
print(effluent_treatment_df.head())
print(f"Number of rows: {effluent_treatment_df.shape[0]}")
print(f"Number of columns: {effluent_treatment_df.shape[1]}")

# Save to CSV in parent folder
effluent_treatment_df.to_csv("effluent_treatment_df.csv", index=False)

#====================================
# Paper Quality Data
#====================================

quality_tags_of_interest = [
    "525BW014.MV",
    "DRYTONSHR",
    "QCSBRIGHTNESS"
]
# two tags missing because data was too stringy (525I545.BRK  & 525SI585.MV )
# in the future, I will process it further and turn the 'none' values to 0


#pull above columns into separate df
quality_df = IEP_df[quality_tags_of_interest]

#Save to CSV in parent folder
quality_df.to_csv('quality_df.csv', index=False)

#=======================
# Pulp Mill Data
#=======================

pulp_mill_tags_of_interest = [
    "260F209",
    "260F765",
    "260F769",
    "260F771",
    "290FC025_MV",
    "291F209",
    "291F765",
    "291F769",
    "291F771",
    "291FC162.MV",
    "298FC050.MV",
    "298FC130.MV",
    "298FC140.MV",
    "298FC272_MV",
    "298FC883.MV",
    "298FC891",
    "298FC893",
    "525FC007.MV",
    "525FC085",
    "525FC093"
]

#pull above columns into separate df
pulp_mill_df = IEP_df[pulp_mill_tags_of_interest]

#Save to CSV in parent folder
pulp_mill_df.to_csv('pulp_mill_df.csv', index = False)

#=============================
# Outcome Data
#=============================

outcome_tags_of_interest = [
    "301AI569",
    "301BOD451",
    "301OPC052_MV",
    "301OPC062_MV"
]

#pull above columns into separate df
outcomes_df = IEP_df[outcome_tags_of_interest]

#Save to CSV in parent folder
outcomes_df.to_csv('outcome_data.csv', index = False)