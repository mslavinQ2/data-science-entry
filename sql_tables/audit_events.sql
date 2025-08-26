-- Table to store audit events
CREATE TABLE audit_events (
    audit_id INT AUTOINCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    action VARCHAR(100),
    timestamp TIMESTAMP,
    details STRING
);
