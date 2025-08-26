"""
API endpoint to receive audit data and insert into Snowflake via stored procedure.
"""
from fastapi import FastAPI, HTTPException, Request
import snowflake.connector
import os

app = FastAPI()

# Snowflake connection parameters (use environment variables in real use)
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER", "user")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD", "password")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT", "account")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "AUDIT_DB")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")

@app.post("/audit")
async def receive_audit(request: Request):
    data = await request.json()
    try:
        ctx = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cs = ctx.cursor()
        # Call stored procedure to insert audit data
        cs.execute(f"CALL insert_audit_data('{data['user_id']}', '{data['action']}', '{data['timestamp']}', '{data['details']}')")
        cs.close()
        ctx.close()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
