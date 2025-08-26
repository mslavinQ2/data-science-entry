-- Table to store audit summaries
CREATE TABLE audit_summary (
    summary_id INT AUTOINCREMENT PRIMARY KEY,
    day DATE,
    action VARCHAR(100),
    count INT
);
