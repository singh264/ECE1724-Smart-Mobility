# Graph-Search-Algorithms
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/singh264/smart-mobility/graphs/contributors) 
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://github.com/singh264/smart-mobility/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/singh264/smart-mobility/pulls)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/singh264/smart-mobility/master)

---
# Important Notes  

### main.ipynb
- This will act as a main file for the project

### exp.ipnb
- Includes experimental codes. Use this to test out code. 

### sample_codes
- Includes demo algorithms provided by professor.  
- Utilities folder is included one level up. Hence, you will need to make the following modification when running/testing any of the algorithms in this folder. 
  ```python
  import sys
  sys.path.append("../")
  from utilities include *
  ```

### bing_traffic
- Module contains `bing_live_traffic_incidents_api.py` that retrieve live traffic incidents from the Bing Traffic API for a given bounding box on the map. 
- Checkout this [Wiki](https://github.com/singh264/smart-mobility/wiki/Bing-Traffic) to learn more about the Bing Traffic API.
