import json
import geojson

with open('D:/tugas_akhir/data/tambang_papua.geojson') as f:
    geojson_data = geojson.load(f)

# Reformatting the GeoJSON with indentation for readability
with open('D:/tugas_akhir/data/tambang_papua_f.geojson', 'w') as f:
    json.dump(geojson_data, f, indent=2)

