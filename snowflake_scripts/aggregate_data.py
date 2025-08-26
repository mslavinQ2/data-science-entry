"""
Aggregate audit data in Snowflake.
"""
import snowflake.connector

def get_daily_action_summary():
    ctx = snowflake.connector.connect(
        user='user', password='password', account='account', database='AUDIT_DB', schema='PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute("SELECT DATE(timestamp) as day, action, COUNT(*) FROM audit_events GROUP BY day, action")
    results = cs.fetchall()
    cs.close()
    ctx.close()
    return results
