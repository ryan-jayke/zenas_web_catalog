import snowflake.connector
import streamlit
import pandas

sql_query = "select * from zenas_athleisure_db.products.catalog_for_website"


streamlit.title('Zena\'s Amazing Athleisure Catalog')
