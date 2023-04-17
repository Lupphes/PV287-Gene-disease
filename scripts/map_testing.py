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

# Sort DisGeNET dataset by 'geneName' column
disgenet_data_sorted = disgenet_data.sort_values(by="geneName")

# Print the first 5 rows of the 'geneName' column
print("DisGeNET data (sorted by geneName):")
print(disgenet_data_sorted['geneName'].head())

# Sort GAF data by 'DB_Object_Symbol' column
# gaf_data_sorted = gaf_data.sort_values(by="DB_Object_Symbol")

# Print the first 5 rows of the 'DB_Object_Symbol' column
print("\nGAF data (sorted by DB_Object_Symbol):")
print(gaf_data['DB_Object_Symbol'].head())

# Sort parsed GO data by 'ID' column
parsed_go_data_sorted = parsed_go_data.sort_values(by="id")

# Print the first 5 rows of the 'ID' column
print("\nParsed GO data (sorted by ID):")
print(parsed_go_data_sorted['id'].head())
