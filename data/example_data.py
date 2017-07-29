import csv
from govhack_app import db
from govhack_app.location.models import Lga
from govhack_app.location.models import Postcode


def example_data():
    with open('data/example_dataset.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            lga = Lga.query.filter(Lga.lga_name.like('%{}%'.format(row[1]))).first()
            pcode = Postcode(postcode=row[0],
                             longitude=row[2],
                             latitude=row[3],
                             score_1_year=row[4],
                             score_5_year=row[5],
                             score_10_year=row[6],
                             avg_income=row[7],
                             income_below_threshold=row[8],
                             property_growth=row[9],
                             population_growth=row[10],
                             seifa=row[11],
                             places_needed_1_year=row[12],
                             places_needed_5_year=row[13],
                             places_needed_10_year=row[14])
            pcode.lgas.append(lga)
            db.session.add(pcode)
            db.session.commit()
