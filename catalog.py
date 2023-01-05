import snowflake.connector
import streamlit
import pandas

catalog_list = pandas.read_sql_query("select * from zenas_athleisure_db.products.catalog_for_website")

streamlit.title('Zena\'s Amazing Athleisure Catalog')
