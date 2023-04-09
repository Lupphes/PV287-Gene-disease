import obonet
import csv

graph = obonet.read_obo("./data/go.obo")

# Open the CSV file for writing
with open("./data/go.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["id", "name", "namespace", "def", "synonym"])

    # Write each node as a row in the CSV file
    for node_id, data in graph.nodes(data=True):
        name = data.get("name", "")
        namespace = data.get("namespace", "")
        definition = data.get("def", "")
        synonyms = ", ".join(data.get("synonym", []))
        writer.writerow([node_id, name, namespace, definition, synonyms])
