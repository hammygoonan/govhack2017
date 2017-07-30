from govhack_app import db


lga_postcode = db.Table(
    'lga_postcode',
    db.Column('lga_id', db.Integer, db.ForeignKey('lgas.id')),
    db.Column('postcode_id', db.Integer, db.ForeignKey('postcodes.id'))
    )


class Lga(db.Model):

    __tablename__ = 'lgas'

    id = db.Column(db.Integer, primary_key=True)
    lga_code = db.Column(db.Integer, unique=True, nullable=False)
    lga_name = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    gccsa_name = db.Column(db.String(120))
    postcodes = db.relationship('Postcode', secondary=lga_postcode,
                                backref=db.backref('lgas', lazy='dynamic'))

    def __init__(self, **kwargs):
        self.lga_code = kwargs.get('lga_code')
        self.lga_name = kwargs.get('lga_name')
        self.state = kwargs.get('state')
        self.postcode = kwargs.get('postcode')
        self.gccsa_name = kwargs.get('gccsa_name')


class Postcode(db.Model):

    __tablename__ = 'postcodes'

    id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    demands = db.relationship('Demand', backref='postcode', lazy='dynamic')

    def __init__(self, **kwargs):
        self.postcode = kwargs.get('postcode')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')

    def serialise(self):
        return {
            'postcode': self.postcode,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'lga': [{'name': lga.lga_name} for lga in self.lgas]
            }


class Demand(db.Model):

    __tablename__ = 'demands'

    id = db.Column(db.Integer, primary_key=True)
    postcode_id = db.Column(db.Integer, db.ForeignKey('postcodes.id'), nullable=False)
    government_funded_places = db.Column(db.Integer)
    seifa = db.Column(db.Float)
    age = db.Column(db.Enum('0-4', '5-9', '10-14'))
    population_growth = db.Column(db.Float)
    property_median_price = db.Column(db.Float)
    score_1_year = db.Column(db.Integer)
    score_5_year = db.Column(db.Integer)
    score_10_year = db.Column(db.Integer)
    places_needed_1_year = db.Column(db.Integer)
    places_needed_5_year = db.Column(db.Integer)
    places_needed_10_year = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.postcode_id = kwargs.get('postcode_id')
        self.government_funded_places = kwargs.get('government_funded_places')
        self.seifa = kwargs.get('seifa')
        self.age = kwargs.get('age')
        self.population_growth = kwargs.get('population_growth')
        self.property_median_price = kwargs.get('property_median_price')
        self.score_1_year = kwargs.get('score_1_year')
        self.score_5_year = kwargs.get('score_5_year')
        self.score_10_year = kwargs.get('score_10_year')
        self.places_needed_1_year = kwargs.get('places_needed_1_year')
        self.places_needed_5_year = kwargs.get('places_needed_5_year')
        self.places_needed_10_year = kwargs.get('places_needed_10_year')

    def serialise(self):
        population_growth = None
        if self.population_growth:
            population_growth = round(self.population_growth * 100, 2)
        return {
            'postcode': self.postcode.serialise(),
            'government_funded_places': self.government_funded_places,
            'seifa': self.seifa,
            'age': self.age,
            'population_growth': population_growth,
            'property_median_price': self.property_median_price,
            'score_1_year': self.score_1_year,
            'score_5_year': self.score_5_year,
            'score_10_year': self.score_10_year,
            'places_needed_1_year': self.places_needed_1_year,
            'places_needed_5_year': self.places_needed_5_year,
            'places_needed_10_year': self.places_needed_10_year
            }
