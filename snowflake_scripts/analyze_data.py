"""
Analyze audit data in Snowflake.
"""
import snowflake.connector

def get_action_counts():
    ctx = snowflake.connector.connect(
        user='user', password='password', account='account', database='AUDIT_DB', schema='PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute("SELECT action, COUNT(*) FROM audit_events GROUP BY action")
    results = cs.fetchall()
    cs.close()
    ctx.close()
    return results
