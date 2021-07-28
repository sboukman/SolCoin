#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 03:33:35 2021

@author: sollyboukman
"""

**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages***

```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python3 -m pytest backend/tests
```

**Run the app and API**

Make sure to activate the virtual environment

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment

```
export PEER==True && python3 -m backend.app
```

