# Static-Data Reconciliation Mini-Project

## What
- Compares two Excel sources (`source_A.xlsx`, `source_B.xlsx`) by ISIN.
- Flags mismatches (walks through `Ticker`, `Name`, `Currency`) & uniques.

## Why
- Ensures front- to back-office data integrity for critical reference data.

## How to run
- **Python**: `python reconcile.py`
- **VBA**: Open `Reconcile.bas` in Editor, run `Reconcile` macro.

## Key techniques
- Python: `pandas.merge(..., indicator=True)`
- VBA: `Scripting.Dictionary`, sheet looping
