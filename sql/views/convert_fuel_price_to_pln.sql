DROP VIEW IF EXISTS fuel_pln;


CREATE OR REPLACE VIEW fuel_pln AS
SELECT fuel.date,
       fuel.country,
       fuel.fuel_type,
       fuel.price_eur_per_litre,
       n.eur_to_pln_rate,
       ROUND(fuel.price_eur_per_litre * n.eur_to_pln_rate, 2) AS fuel_to_pln
FROM fuel
LEFT JOIN LATERAL (
    SELECT eur_to_pln_rate
    FROM nbp_eur
    WHERE nbp_eur.date <= fuel.date
    ORDER BY nbp_eur.date DESC
    LIMIT 1
) AS n ON true;