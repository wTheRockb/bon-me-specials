# bon-me-specials
Script to report on what the Bon Me Food Truck daily lunch special is!

## Setup

`pip install -r requirements.txt`
Installs `requests`, the sole dependancy.

Requires a `secret.txt` with a valid [twitter app key](https://apps.twitter.com/) on the first line.

Run with `python bon_me.py` and any tweets covering the daily food truck specials will be printed to stdout.