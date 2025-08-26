"""
Update audit data in Snowflake using stored procedure.
"""
import snowflake.connector

def update_audit_data(audit_id, details):
    ctx = snowflake.connector.connect(
        user='user', password='password', account='account', database='AUDIT_DB', schema='PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute(f"CALL update_audit_details({audit_id}, '{details}')")
    cs.close()
    ctx.close()
