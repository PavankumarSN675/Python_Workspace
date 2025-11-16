"""
✅ 1. Reading a Qt Table (QTableWidget / QTableView)

This is the most common case in Squish.

Read a single cell
def read_cell(table_obj, row, column):
    return table_obj.item(row, column).text

Read all rows & columns
def read_table(table_obj):
    rows = table_obj.rowCount
    cols = table_obj.columnCount
    data = []

    for r in range(rows):
        rowData = []
        for c in range(cols):
            cell = table_obj.item(r, c)
            rowData.append(cell.text if cell else "")
        data.append(rowData)

    return data

Usage
table = waitForObject(":MainWindow.Table_QTableWidget")
table_data = read_table(table)

for row in table_data:
    test.log(str(row))

✅ 2. Reading Qt QTableView (Model-based tables)

QTableView uses a model, so we use:

model = table.model()
index = model.index(row, column)
value = model.data(index)

Example (full table)
def read_qtableview(table_obj):
    model = table_obj.model()
    rows = model.rowCount()
    cols = model.columnCount()
    table_data = []

    for r in range(rows):
        rowData = []
        for c in range(cols):
            index = model.index(r, c)
            rowData.append(str(model.data(index)))
        table_data.append(rowData)

    return table_data

table = waitForObject(":MainWindow.Table_QTableView")
data = read_qtableview(table)

"""