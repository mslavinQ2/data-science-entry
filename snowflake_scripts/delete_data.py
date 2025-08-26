"""
Delete audit data in Snowflake using stored procedure.
"""
import snowflake.connector

def delete_audit_data(audit_id):
    ctx = snowflake.connector.connect(
        user='user', password='password', account='account', database='AUDIT_DB', schema='PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute(f"CALL delete_audit_data({audit_id})")
    cs.close()
    ctx.close()
