import csv
from govhack_app import db
from govhack_app.location.models import Lga
from govhack_app.location.models import Postcode


def import_lga():
    with open('data/lga.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            # pcode = Postcode.query.filter_by(postcode=row[6]).first()
            # if pcode is None:
            #     pcode = Postcode(postcode=row[6])
            #     db.session.add(pcode)
            #     db.session.commit()
            lga = Lga.query.filter_by(lga_code=row[1]).first()
            if lga is None:
                lga = Lga(lga_code=row[1], lga_name=row[2], state=row[4], gccsa_name=row[-1])
                db.session.add(lga)

            # if pcode.postcode not in [pc.postcode for pc in lga.postcodes]:
            #     lga.postcodes.append(pcode)
            db.session.commit()
