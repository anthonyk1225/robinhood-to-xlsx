def write_sum(worksheet, workbook, row):
  worksheet.set_column(
    'K12:K13',
    15,
  )

  worksheet.add_table(
    'K12:K13', {
      'columns': [
        {
          'header': 'Total Dividends',
        },
      ],
    },
  )

  worksheet.write_formula(
    'K13',
    f"=SUM(A2:A{row})",
    workbook.add_format(
      {
        'bold': True,
        'num_format': '$0.00',
      },
    ),
  )

def handle_formulas(worksheet, workbook, data):
  row = len(data) + 1
  write_sum(worksheet, workbook, row)

  