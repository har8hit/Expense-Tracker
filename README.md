# Expense Tracker

Expense Tracker is a CLI application to keep records of expenses.

- **Programming Language:** Python
- **Modules used:** Typer, tempfile, os, shutil, date, etc.

## Requirements

1. Python must be installed.
2. The Typer module must be installed.
   - If Typer is not installed, open any terminal and run:
     ```bash
     pip install typer
     ```

## How to Use

1. Clone `Expense-Tracker.py` to your system.
   ```bash
   gh repo clone har8hit/Expense-Tracker
   ```
   or
   ```bash
   git clone https://github.com/har8hit/Expense-Tracker.git
   ```
   #### OR Download Expense_Tracekr.py manualy.
3. Use Typer commands to run the commands listed below.

## Command Syntax

```bash
typer [Module_or_Path] run [command] [argument]...
```

- **`[Module_or_Path]`** — `Expense-Tracker.py`
- **`--help`** — Can be used after the module or after a command to get the required help.

### Getting help on the available commands

<img width="957" height="343" alt="Help output listing available commands" src="https://github.com/user-attachments/assets/64d3da3d-61ce-47a5-af08-70ef50a66762" />

### Getting help on the arguments for the `add` command

<img width="962" height="192" alt="Help output for the add command arguments" src="https://github.com/user-attachments/assets/a86e6ec3-46d4-4e14-806d-939b4e54c918" />

## Commands

### `add`

Add an expense.

**Required arguments:** `description` (use `_` instead of space), `amount`

<img width="961" height="98" alt="Example of using the add command" src="https://github.com/user-attachments/assets/5662abe5-0f64-4694-8823-931b82acda70" />

### `update`

Update an existing record.

**Required arguments:** `id`, `description` (use `_` instead of space), `amount`

<img width="960" height="53" alt="Example of using the update command" src="https://github.com/user-attachments/assets/c8be7955-cf01-40a5-9341-efdbafccd574" />

### `delete`

Delete an existing record.

**Required argument:** `id`

<img width="955" height="48" alt="Example of using the delete command" src="https://github.com/user-attachments/assets/28ae14f4-536f-4c15-8715-9c48953df196" />

### `show`

Get all records.

**Required argument:** None

<img width="960" height="61" alt="Example of using the show command" src="https://github.com/user-attachments/assets/83cd7170-081a-471b-ba56-b1fa28373020" />

### `summary`

Get a summary of all records.

**Required argument:** None

*(After adding dummy records)*

<img width="963" height="46" alt="Example of using the summary command" src="https://github.com/user-attachments/assets/a0a07b1e-466d-41b9-925b-86d6f0af9dbc" />

### `monthly-summary`

Get a summary of a particular month.

**Required argument:** `month` (in `MM` format)

<img width="963" height="49" alt="Example of using the monthly-summary command" src="https://github.com/user-attachments/assets/1aa46d8a-2045-4fd1-a969-b436dc346f46" />

### `export`

Export records as a `.csv` file to a specific path.

**Required argument:** `path`

<img width="960" height="49" alt="Example of using the export command" src="https://github.com/user-attachments/assets/833b804f-2818-4def-991e-88a562ffc8af" />

### `open-csv`

Open records as a `.csv` file directly, without exporting to a specific location.

**Required argument:** None

<img width="963" height="33" alt="Example of using the open-csv command" src="https://github.com/user-attachments/assets/2f50763f-b699-459a-b55e-a620e7713e35" />

<img width="703" height="500" alt="CSV file opened showing expense records" src="https://github.com/user-attachments/assets/26de5613-2656-487d-a35b-3a2199fe16c1" />
