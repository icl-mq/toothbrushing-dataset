#%%
import os
from pathlib import Path

#%%
rootdir = (Path(os.getcwd()) / "data").resolve()


# %%
for f in sorted(rootdir.glob('**/')):
    if f.is_dir():
        print(f"{f.name}\t{(f / 'labels.json').is_file()}")
# %%
