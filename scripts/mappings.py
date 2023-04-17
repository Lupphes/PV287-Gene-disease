import pandas as pd

FOLDER = "./data/"

# Load the DisGeNET dataset
disgenet_data = pd.read_csv(FOLDER + "gene_disease_view.csv")

# Load the GAF file
gaf_columns = [
    "DB", "DB_Object_ID", "DB_Object_Symbol", "Qualifier", "GO_ID",
    "DB:Reference", "Evidence_Code", "With_or_From", "Aspect", "DB_Object_Name",
    "DB_Object_Synonym", "DB_Object_Type", "Taxon", "Date", "Assigned_By"
]
gaf_data = pd.read_csv(FOLDER + "goa_human.gaf", sep="\t", comment="!", names=gaf_columns, skiprows=12)

# Load the parsed GO file
parsed_go_data = pd.read_csv(FOLDER + "go.csv")

# Convert gene symbols to uppercase
disgenet_data['geneName'] = disgenet_data['geneName'].str.upper()
gaf_data['DB_Object_Symbol'] = gaf_data['DB_Object_Symbol'].str.upper()
parsed_go_data['id'] = parsed_go_data['id'].str.upper()

mapping_go = parsed_go_data.merge(gaf_data, left_on="id", right_on="DB_Object_Symbol")

# print(mapping_go[['id', 'DB_Object_Symbol']].head())

mapping_full = mapping_go.merge(disgenet_data.head(), left_on="DB", right_on="geneName")

# Print the first 5 rows of the combined data
print(mapping_full.head())

mapping_full.to_csv("combined_data.csv", index=False)

