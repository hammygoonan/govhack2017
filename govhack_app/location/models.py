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
    score_1_year = db.Column(db.Integer, nullable=False)
    score_5_year = db.Column(db.Integer, nullable=False)
    score_10_year = db.Column(db.Integer, nullable=False)
    avg_income = db.Column(db.Integer, nullable=False)
    income_below_threshold = db.Column(db.Enum('Low', 'Medium', 'High'))
    property_growth = db.Column(db.Float, nullable=False)
    population_growth = db.Column(db.Float, nullable=False)
    seifa = db.Column(db.Float, nullable=False)
    places_needed_1_year = db.Column(db.Integer, nullable=False)
    places_needed_5_year = db.Column(db.Integer, nullable=False)
    places_needed_10_year = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.postcode = kwargs.get('postcode')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
        self.score_1_year = kwargs.get('score_1_year')
        self.score_5_year = kwargs.get('score_5_year')
        self.score_10_year = kwargs.get('score_10_year')
        self.avg_income = kwargs.get('avg_income')
        self.income_below_threshold = kwargs.get('income_below_threshold')
        self.property_growth = kwargs.get('property_growth')
        self.population_growth = kwargs.get('population_growth')
        self.seifa = kwargs.get('seifa')
        self.places_needed_1_year = kwargs.get('places_needed_1_year')
        self.places_needed_5_year = kwargs.get('places_needed_5_year')
        self.places_needed_10_year = kwargs.get('places_needed_10_year')

    def serialise(self):
        return {
            'postcode': self.postcode,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'score_1_year': self.score_1_year,
            'score_5_year': self.score_5_year,
            'score_10_year': self.score_10_year,
            'avg_income': self.avg_income,
            'income_below_threshold': self.income_below_threshold,
            'property_growth': self.property_growth,
            'population_growth': self.population_growth,
            'seifa': self.seifa,
            'places_needed_1_year': self.places_needed_1_year,
            'places_needed_5_year': self.places_needed_5_year,
            'places_needed_10_year': self.places_needed_10_year,
            'lga': [{'name': lga.lga_name} for lga in self.lgas]
            }
