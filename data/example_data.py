import csv
from govhack_app import db
from govhack_app.location.models import Postcode, Demand, Lga


def example_data():
    for csv_file in [{'age': '0-4', 'file': 'data/input1.csv'},
                     {'age': '5-9', 'file': 'data/input2.csv'},
                     {'age': '10-14', 'file': 'data/input3.csv'}]:
        with open(csv_file['file']) as f:
            reader = csv.reader(f)
            for row in reader:
                pcode = Postcode.query.filter_by(postcode=row[0]).first()
                if pcode is None:
                    pcode = Postcode(postcode=row[0], longitude=row[7], latitude=row[8])
                    lga = Lga.query.filter(Lga.lga_name.like('%{}%'.format(row[6]))).first()
                    pcode.lgas.append(lga)
                    db.session.add(pcode)
                    db.session.commit()
                total_childcare_facilities = None
                if row[1]:
                    total_childcare_facilities = row[1]
                government_funded_places = None
                if row[2].strip():
                    government_funded_places = int(row[2].strip())
                seifa = None
                if row[3].strip():
                    seifa = float(row[3].strip())
                population_growth = None
                if row[4].strip():
                    population_growth = float(row[4].strip())
                property_median_price = None
                if row[5].replace(',', '').replace('$', '').strip():
                    property_median_price = float(row[5].replace(',', '').replace('$', '').strip())
                score_1_year = None
                if row[9].strip():
                    score_1_year = int(row[9].strip())
                score_5_year = None
                if row[10].strip():
                    score_5_year = int(row[10].strip())
                score_10_year = None
                if row[11].strip():
                    score_10_year = int(row[11].strip())
                places_needed_1_year = None
                if row[12].strip():
                    places_needed_1_year = int(row[12].strip())
                places_needed_5_year = None
                if row[13].strip():
                    places_needed_5_year = int(row[13].strip())
                places_needed_10_year = None
                if row[14].strip():
                    places_needed_10_year = int(row[14].strip())
                demand = Demand(postcode_id=pcode.id,
                                total_childcare_facilities=total_childcare_facilities,
                                government_funded_places=government_funded_places,
                                seifa=seifa,
                                age=csv_file['age'],
                                population_growth=population_growth,
                                property_median_price=property_median_price,
                                score_1_year=score_1_year,
                                score_5_year=score_5_year,
                                score_10_year=score_10_year,
                                places_needed_1_year=places_needed_1_year,
                                places_needed_5_year=places_needed_5_year,
                                places_needed_10_year=places_needed_10_year)
                db.session.add(demand)
                db.session.commit()
