from sql.operations.splits import create_splits, get_splits

def handle_splits(data):
  symbols = []
  split_data = []

  for item in data:
    symbols.append(item["symbol"])

  symbols = set(symbols)

  for symbol in symbols:
    rows = get_splits(symbol)

    # if len(rows) == 0:
    #   print("Hitting the API for /splits")
    #   splits = call_splits(symbol)
    #   print("Done hitting the API for /splits")
    #   for split in splits:
    #     try:
    #       create_splits(
    #         split["symbol"],
    #         split["date"],
    #         split["fromFactor"],
    #         split["toFactor"]
    #       )
    #       split_data += splits
    #     except Exception as e:
    #       print("An error occured, trying to insert a row into splits ", e)
    # else:
    for row in rows:
      (
        symbol,
        date,
        from_factor,
        to_factor,
      ) = row

      simple_name = "split" if to_factor > from_factor else "reverse split"

      row = {
        "symbol": symbol,
        "last_transaction_at": date,
        "from_factor": from_factor,
        "to_factor": to_factor,
        "fees": 0,
        "price": 0,
        "quantity": round(to_factor / from_factor, 4),
        "side": "None",
        "simple_name": simple_name
      }

      split_data.append(row)

  return split_data
