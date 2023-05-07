-- Selects bands with Glam Rock as their
-- style and ranks them by their longevity
SELECT band_name,
IFNULL(split, year(current_date())) - formed AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC;
