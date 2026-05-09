CREATE TABLE rider_logs (
    rider_id INT,
    timestamp DATETIME,
    speed FLOAT,
    acceleration FLOAT,
    turn_angle FLOAT,
    proximity_alert INT,
    rider_score FLOAT
);

SELECT AVG(rider_score) AS avg_score
FROM rider_logs;

SELECT COUNT(*) AS harsh_brake_events
FROM rider_logs
WHERE acceleration < -4;

SELECT rider_id, rider_score
FROM rider_logs
WHERE rider_score < 70;