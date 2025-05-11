## 0x00. Pagination

### Project Overview
This project focuses on implementing pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination. The goal is to efficiently handle large datasets by breaking them into manageable chunks (pages) and providing metadata for navigation.

### Resources
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

### Learning Objectives
By the end of this project, you should be able to:
- Paginate a dataset using simple `page` and `page_size` parameters.
- Implement hypermedia pagination with metadata.
- Create deletion-resilient pagination to handle dataset changes between queries.

### Requirements
- **Environment**: Ubuntu 18.04 LTS with Python 3.7.
- **File format**:
  - First line must be `#!/usr/bin/env python3`.
  - All files must end with a newline.
- **Style**: Pycodestyle (version 2.5.*).
- **Documentation**:
  - Modules and functions must have descriptive docstrings.
  - Type annotations for all functions and coroutines.
- **Dataset**: Use [`Popular_Baby_Names.csv`](Popular_Baby_Names.csv) for testing.

### Tasks

#### 0. Simple Helper Function
**File**: `0-simple_helper_function.py`  
Implement a function `index_range` that takes `page` and `page_size` and returns a tuple of start and end indices for pagination.

**Example**:
```python
index_range(1, 7)  # returns (0, 7)
index_range(3, 15)  # returns (30, 45)

Author: Dzeble Kwame 
