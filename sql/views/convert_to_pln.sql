DROP VIEW IF EXISTS fuel_gold;
CREATE OR REPLACE VIEW fuel_pln AS
    SELECT fuel.date, fuel.country, fuel.fuel_type, fuel.price_eur_per_litre, nbp_eur.eur_to_pln_rate, ROUND((fuel.price_eur_per_litre * nbp_eur.eur_to_pln_rate), 2) AS fuel_to_pln
    FROM fuel
    INNER JOIN nbp_eur ON fuel.date = nbp_eur.date
    WHERE fuel.date >= '2026-01-01'