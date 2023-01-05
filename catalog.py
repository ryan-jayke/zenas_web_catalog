import snowflake.connector
import streamlit
import pandas

sql_query = "select * from zenas_athleisure_db.products.catalog_for_website"
my_fruit_list = pandas.read_csv("https://uni-klaus.s3.us-west-2.amazonaws.com/zenas_metadata/sweatsuit_sizes.txt")

streamlit.title('Zena\'s Amazing Athleisure Catalog')
