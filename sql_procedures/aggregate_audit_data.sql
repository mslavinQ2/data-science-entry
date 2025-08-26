-- Stored procedure to aggregate audit data by day and action
CREATE OR REPLACE PROCEDURE aggregate_audit_data()
RETURNS STRING
LANGUAGE SQL
AS $$
    INSERT INTO audit_summary(day, action, count)
    SELECT DATE(timestamp), action, COUNT(*)
    FROM audit_events
    GROUP BY DATE(timestamp), action;
    RETURN 'Aggregated';
$$;
