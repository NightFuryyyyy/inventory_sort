# inventory_sort

[Tools Used](#tools-used) • [Demo](#demo) • [How to Use](#how-to-use) • [Build](#build)

## Tools Used
- Qt Designer
- PyQt6
- PyInstaller


## Demo

![screen_recording](https://github.com/user-attachments/assets/c2b2b789-4353-4cf8-b95a-6af07a1e48a1)

## How to Use

> The pre-built binary is **Windows-only**. To build for other platforms, see [Build](#build).

1. Click [this link](https://github.com/NightFuryyyyy/inventory_sort/releases/latest/download/inventory_sort.exe) to download the latest release.
2. Download the [sample dataset](https://github.com/NightFuryyyyy/inventory_sort/blob/main/inventory.json) or create a JSON file according to this schema:
   ```JSON
   {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Generated Schema",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "category": {
            "type": "string"
          },
          "quantity": {
            "type": "integer"
          },
          "price": {
            "type": "integer"
          },
          "restock_date": {
            "type": "string",
            "format": "date"
          }
        },
        "required": [
          "id",
          "name",
          "category",
          "quantity",
          "price",
          "restock_date"
        ]
      }
   }
   ```
3. Run the executable.
4. Click on the "Open" button and select your JSON file.
5. Use the bottom drop-down lists to sort the records.

## Build

1. Clone the repository.
   ```bash
   git clone https://github.com/NightFuryyyyy/inventory_sort
   ```
2. Change directory to the new folder.
   ```bash
   cd ./inventory_sort
   ```
3. Build the executable using PyInstaller.
   ```bash
   pyinstaller -w --onefile ./app.py -n "inventory_sort"
   ```
The executable can be found in the `dist` folder.
