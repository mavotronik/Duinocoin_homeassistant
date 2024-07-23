# Duinocoin_homeassistant

List of sensors to show balance, verification status, number of warnings.

## Installation
1. Install  Python Scipts Pro component by link: https://github.com/AlexxIT/PythonScriptsPro
2. Edit your `configuration.yaml`, add this:
```
python_script:
   requirements:
     - requests
```
3. Copy this file to your package directory.
4. In the package file replace `<username>` to your username.
5. Save file and restart homeassistant. Sensors should appear.
