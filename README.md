# Parallel Loop Library

Execute for-loops in parallel with ease!

## Installation
```bash
pip install -e .  # For local development
```

## Usage
```python
from kolluri_parallel import parallel_for

def process_item(item):
    # Your computation here
    return (item, item ** 2)

results = parallel_for(
    iterable=range(1, 6),
    func=process_item,
    max_workers=3
)
```

## Features
- Thread/process pool executors
- Error handling
- Simple API