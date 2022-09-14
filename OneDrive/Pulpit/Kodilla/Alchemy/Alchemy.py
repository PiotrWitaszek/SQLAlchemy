from ast import Delete
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from sqlalchemy import create_engine, engine

engine = create_engine("sqlite:///base.db", echo=True)

meta = MetaData()
conn = engine.connect()

stations = Table(
    "stations",
    meta,
    Column("id", Integer, primary_key=True),
    Column("station", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("elevation", Float),
    Column("name", String),
    Column("country", String),
    Column("state", String),
)


measure = Table(
    "measure",
    meta,
    Column("id", Integer, primary_key=True),
    Column("station", String),
    Column("date", String),
    Column("precipe", Float),
    Column("tobs", Float),
)

meta.create_all(engine)
print(engine.table_names())


if __name__ == "__main__":
    ins = stations.insert()
    conn.execute(
        ins,
        [
            {
                "station": "USC00519397",
                "latitude": 21.2716,
                "longitude": 157.8168,
                "elevation": 3.0,
                "name": "WAIKIKI",
                "country": "US",
                "state": "HI",
            },
            {
                "station": "USC00513117",
                "latitude": 21.4234,
                "longitude": 157.8015,
                "elevation": 14.6,
                "name": "KANEOHE",
                "country": "US",
                "state": "HI",
            },
            {
                "station": "USC00514830",
                "latitude": 21.5213,
                "longitude": 157.8374,
                "elevation": 7.0,
                "name": "KUALOA RANCH HEADQUARTERS",
                "country": "US",
                "state": "HI",
            },
            {
                "station": "USC00517948",
                "latitude": 21.3934,
                "longitude": 157.9751,
                "elevation": 11.9,
                "name": "PEARL CITY",
                "country": "US",
                "state": "HI",
            },
            {
                "station": "USC00518838",
                "latitude": 21.4992,
                "longitude": 158.0111,
                "elevation": 6.0,
                "name": "UPPER WAHIAWA",
                "country": "US",
                "state": "HI",
            },
        ],
    )
    conn = engine.connect()
    s = stations.select()
    result = conn.execute(s)
    for row in result:
        print(row)

    ins = measure.insert()
    conn.execute(
        ins,
        [
            {
                "station": "USC00519397",
                "date": "2010-01-01",
                "precipe": 0.08,
                "tobs": 65,
            },
            {
                "station": "USC00519397",
                "date": "2010-01-02",
                "precipe": 157.8015,
                "tobs": 63,
            },
            {
                "station": "USC00519397",
                "date": "2010-01-03",
                "precipe": 0.0,
                "tobs": 74,
            },
            {
                "station": "USC00519397",
                "date": "2010-01-04",
                "precipe": 0.0,
                "tobs": 76,
            },
            {
                "station": "USC00519397",
                "date": "2010-01-06",
                "precipe": 0.0,
                "tobs": 73,
            },
        ],
    )
    a = measure.select()
    result = conn.execute(a)
    for row in result:
        print(row)
    s = measure.update().where(measure.c.date == "2010-01-04").values(precipe=222.0)
    result = conn.execute(s)
    result = conn.execute(a)
    for row in result:
        print(row)
    s = measure.delete().where(measure.c.date == "2010-01-04")
    result = conn.execute(s)
    result = conn.execute(a)
    for row in result:
        print(row)
    s = measure.delete()
    result = conn.execute(s)
    result = conn.execute(a)
    for row in result:
        print(row)
