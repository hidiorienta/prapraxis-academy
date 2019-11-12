# Reading JSON content from a file
import json
with open('/tmp/file.json', 'r') as f:
    data = json.load(f)

# Writing JSON content to a file using the dump method
import json
with open('/tmp/file.json', 'w') as f:
    json.dump(data, f, sort_keys=True)

