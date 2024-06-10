SELECT
    v.id AS venue_id,
    v.name AS venue_name,
    c.name AS classification_name,
    e.id AS event_id,
    e.name AS event_name,
    COUNT(DISTINCT ea.attractionid) AS num_attractions,
    AVG(e.minPrice) AS avg_min_price,
    AVG(e.maxPrice) AS avg_max_price
FROM
    venues v
JOIN
    events e ON v.id = e.venueid
JOIN
    classifications c ON e.classificationsid = c.id
JOIN
    event_attraction ea ON e.id = ea.eventid
GROUP BY
    v.id, v.name, c.name, e.id, e.name
HAVING
    COUNT(DISTINCT ea.attractionid) > 1
ORDER BY
    avg_max_price DESC