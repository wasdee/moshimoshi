# moshi moshi~
> call a function in any python scripts using a formated string or json

## TLDR
```bash
pip install moshimoshi
```

```python
from moshimoshi import moshi
import json

moshi('flows.jobseeker:start', 123, sex="male")

async def foo():
    await moshi.moshi('flows.jobseeker:start', 123, sex="male")

json_format = json.dumps({
    "call": 'flows.jobseeker:start',
    "args": [123],
    "kwargs": {
        "sex": "male"
    }
})

moshi(json_format)
```

## Why it is calling 'Moshi Moshiii ~'?
It is the most ***kawaii*** way of call something, no exception to python function. This comes from my waifu named 'Kocho Shinobu', Demo Slayer.
> ⛑ Spoil Alert: This Video contain scenes and conversation of deep episodes.

[![Kocho Shinobu Moshi Moshi](https://img.youtube.com/vi/ZlhwmiCT9ao/0.jpg)](https://www.youtube.com/watch?v=ZlhwmiCT9ao)]
