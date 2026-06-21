import typer
import csv
import os
import shutil
import tempfile
from datetime import date


app=typer.Typer()

@app.command()
def add(discription: str, amount: float):
    file_path = "tracker.csv"
    max_id = 0
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row and row[0]:
                    try:
                        max_id = max(max_id, int(row[0]))
                    except ValueError:
                        pass
    next_id = max_id + 1
    t_date = date.today()
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            writer.writerow(["ID", "Date", "Discription", "Amount"])
        writer.writerow([next_id, t_date, discription, amount])
    typer.echo(f"Added expense: {discription} (Amount: {amount}) with ID: {next_id}")

@app.command()
def update(id:int, discription:str,amount:int):
    file_path = 'tracker.csv'
    temp_fd,temp_path = tempfile.mkstemp()
    os.close(temp_fd)
    status = False
    with open(file_path, 'r',newline='') as file , open(temp_path,'w',newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)
        header = next(reader,None)
        if header:
            writer.writerow(header)
        for row in reader:
            if row:
                try:
                    row_id = int(row[0])
                except ValueError:
                    row_id = None
                if row_id == id:
                    writer.writerow([id,row[1],discription,amount])
                    status = True
                else:
                    writer.writerow(row)
    os.replace(temp_path,file_path)
    if status:
        typer.echo(f"Expense with ID {id} updated successfully.")
    else:
        typer.echo(f"Expense with ID {id} not found.")

@app.command()
def delete(id: int):
    file_path = 'tracker.csv'
    if not os.path.exists(file_path):
        typer.echo("No tracker file found.")
        raise typer.Exit()

    temp_fd, temp_path = tempfile.mkstemp()
    os.close(temp_fd)
    
    deleted = False
    with open(file_path, 'r', newline='') as f, open(temp_path, 'w', newline='') as t:
        reader = csv.reader(f)
        writer = csv.writer(t)
        
        header = next(reader, None)
        if header:
            writer.writerow(header)
            
        for row in reader:
            if row:
                try:
                    row_id = int(row[0])
                except ValueError:
                    row_id = None
                
                if row_id == id:
                    deleted = True
                else:
                    writer.writerow(row)
                    
    os.replace(temp_path, file_path)
    if deleted:
        typer.echo(f"Expense with ID {id} deleted successfully.")
    else:
        typer.echo(f"Expense with ID {id} not found.")

@app.command()
def show():
    file_path='tracker.csv'
    if not os.path.exists(file_path):
        typer.echo("No tracker file found")
    else:
        with open(file_path,'r',newline='') as file:
            reader = csv.reader(file)
            header = next(reader,None)
            if header:
                typer.echo(typer.style(f"{"ID":<5} | {"Date":<10} | {"Discription":<20} | {"Amount":<10}", fg="white", bold=True))
            for row in reader:
                if row:
                    typer.echo(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<20} | {row[3]:<10}")

@app.command()
def summary():
    file_path = 'tracker.csv'
    if not os.path.exists(file_path):
        typer.echo("No tracker file found.")
    else:
        with open(file_path,'r',newline='') as file:
            reader = csv.reader(file)
            next(reader,None)
            total=0.0
            for row in reader:
                if row:
                    try:
                        total+=float(row[3])
                    except ValueError:
                        pass
            typer.echo(typer.style(f"Total expense: {total}", fg="green", bold=True))

@app.command()
def monthly_summary(month:int):
    file_path = 'tracker.csv'
    if not os.path.exists(file_path):
        typer.echo("No tracker file found.")
    else:
        with open(file_path,'r',newline='') as file:
            reader = csv.reader(file)
            next(reader,None)
            total=0.0
            for row in reader:
                if row:
                    try:
                        date = int(row[1][5:7])
                        if month == date :
                            total+=float(row[3])
                    except ValueError:
                        pass
            typer.echo(typer.style(f"Total expense in {month} : {total}", fg="green", bold=True))

@app.command()
def export(path: str):
    file_path = 'tracker.csv'
    if not os.path.exists(file_path):
        typer.echo("No tracker file found")
        raise typer.Exit()
    else:
        shutil.copy2(file_path,path)
        typer.echo(f"Tracker.csv exported to {path}")

@app.command()
def open_csv():
    file_path = 'tracker.csv'
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        typer.echo("No tracker csv file found.")

if __name__ == "__main__":
    app()
