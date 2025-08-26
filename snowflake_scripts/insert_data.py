"""
Insert data into Snowflake audit table using stored procedure.
"""
import snowflake.connector

def insert_audit_data(user_id, action, timestamp, details):
    ctx = snowflake.connector.connect(
        user='user', password='password', account='account', database='AUDIT_DB', schema='PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute(f"CALL insert_audit_data('{user_id}', '{action}', '{timestamp}', '{details}')")
    cs.close()
    ctx.close()
