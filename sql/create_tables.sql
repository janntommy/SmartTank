CREATE TABLE IF NOT EXISTS nbp_transformed (
    date DATE PRIMARY KEY,
    eur_to_pln_rate NUMERIC(10, 4)
);


CREATE TABLE IF NOT EXISTS fuel_transformed (
    date DATE,
    country VARCHAR(3),
    fuel_type VARCHAR(50),
    price_eur_per_litre NUMERIC(10,4)
);