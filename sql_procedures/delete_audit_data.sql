-- Stored procedure to delete audit data
CREATE OR REPLACE PROCEDURE delete_audit_data(audit_id INT)
RETURNS STRING
LANGUAGE SQL
AS $$
    DELETE FROM audit_events WHERE audit_id = audit_id;
    RETURN 'Deleted';
$$;
