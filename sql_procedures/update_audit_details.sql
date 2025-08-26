-- Stored procedure to update audit details
CREATE OR REPLACE PROCEDURE update_audit_details(audit_id INT, details STRING)
RETURNS STRING
LANGUAGE SQL
AS $$
    UPDATE audit_events SET details = details WHERE audit_id = audit_id;
    RETURN 'Updated';
$$;
