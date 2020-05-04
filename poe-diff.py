###
# Grabs items (only equipables) and logs them to the db as Item types
#
#
###
from Item import *
import time
import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from constants import *

URLBASE="https://www.pathofexile.com/api/public-stash-tabs?id="
CODE="700101476-715004424-682104626-771750899-736628041"
CATEGORIES=("accessories","armour","jewels","weapons")

def main(session):
    code, stash = scrapeAPI(CODE)

    while True:
        totCount = 0
        diffCount = 0 # Look into adding differences only
        last_stash = stash
        code, stash = scrapeAPI(code)

        for box in stash:
            for item in box['items']:
                if item['extended']['category'] in CATEGORIES:
                    session.add(Item(league="Delirium",
                                       item_type=item['extended']['baseType'] if 'baseType' in item['extended'].keys() else None,
                                       base_name=item['typeLine'] if "typeLine" in item.keys() else None,
                                       explicits="||".join(item['explicitMods']) if "explicitMods" in item.keys() else None,
                                       implicits=item['implicitMods'] if "implicitMods" in item.keys() else None,
                                       price=item['note'] if "note" in item.keys() else None,))

        # Commit per api code
        session.commit()
        print("\tNext-code: " + code)
        time.sleep(1)


def scrapeAPI(code):
    res = requests.get(URLBASE+code)
    if res.status_code == requests.codes.ok:
        res = json.loads(res.text)
        next_id = res['next_change_id'] if res['next_change_id'] != "" else code
        stashes = res['stashes']
    return next_id, stashes


if __name__ == '__main__':
    # Setup sqlalchemy stuff
    engine = create_engine(ENGINE_CON, echo=True)
    con = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    main(session)
