class Patient(db.Model):
    __tablename__= 'patients'

    id= db.Column(db.Integer)
    birth_year=db.Column(db.integer,
                         db.CheckContraint('birth_year <  2023'),
                         nullable=False)
    
    death_year =  db.Column(db.Integer)

    __table_args__= (db.CheckContraint('(death_year is NULL) OR (death_year >= birth_year)'),)