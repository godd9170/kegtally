from common.utils import get_db_rows


def get_beers():
    return get_db_rows("""
        SELECT beer.name,
            COUNT(case when keg.litres = 50 then keg.id end) as fifty_count,
            COUNT(case when keg.litres = 30 then keg.id end) as thirty_count,
            COUNT(case when keg.litres = 20 then keg.id end) as twenty_count
        FROM inventory_beer beer 
        JOIN inventory_batch batch ON batch.beer_id = beer.id
        JOIN inventory_fill fill ON fill.batch_id = batch.id
        JOIN inventory_keg keg ON keg.id = fill.keg_id
        GROUP BY beer.name
    """)
