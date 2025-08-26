-- Stored procedure to insert a user
CREATE OR REPLACE PROCEDURE insert_user(user_id VARCHAR, name VARCHAR, email VARCHAR)
RETURNS STRING
LANGUAGE SQL
AS $$
    INSERT INTO users(user_id, name, email)
    VALUES (user_id, name, email);
    RETURN 'User Inserted';
$$;
