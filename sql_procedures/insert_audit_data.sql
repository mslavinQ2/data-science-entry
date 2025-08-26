-- Stored procedure to insert audit data
CREATE OR REPLACE PROCEDURE insert_audit_data(user_id VARCHAR, action VARCHAR, timestamp TIMESTAMP, details STRING)
RETURNS STRING
LANGUAGE SQL
AS $$
    INSERT INTO audit_events(user_id, action, timestamp, details)
    VALUES (user_id, action, timestamp, details);
    RETURN 'Inserted';
$$;
