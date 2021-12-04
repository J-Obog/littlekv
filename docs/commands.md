## LittleKV Commands

These are the following commands that are currently supported:

### GET - `get <key>`

**Params:** key = Key to be retrieved

**Returns:** Value of key if it exists, otherwise "\<None>\"

### SET - `set <key> <value>`

**Params:** key = Key to be set (or updated if exists) | value = Value of key

**Returns:** "OK" if key was successfully set

### DEL - `del <key>`

**Params:** key = Key to be deleted (if exists)

**Returns:** "OK" if key was successfully deleted

### KEYS - `keys <pattern>`

**Params:** pattern = Regex pattern used to match keys

**Returns:** List of keys that fit criteria

### COUNT - `count`

**Params:** None

**Returns:** Number of keys in the data source

### CLEAR - `clear`

**Params:** None

**Returns:** "OK" if all keys were removed successfully

### PING - `ping`

**Params:** None

**Returns:** "PONG" if client was able to connect to server
