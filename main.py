import streamlit as st
from lib_product import Product, ProductList
import pandas as pd
from lib_utils import generate_random_id

st.title("Produk App")

if "product_list" not in st.session_state:
    st.session_state.product_list = ProductList("EveryPlast")
    st.session_state.product_list.load_products_from_csv("product-items.csv")

page = st.sidebar.selectbox("Pilih Halaman", ["Daftar Produk", "Tambah Produk", "Manajemen Produk"])

if page == "Daftar Produk":
    st.write("## Daftar Produk")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    products = st.session_state.product_list.get_active_products()

    if products:
        cols = st.columns(3)
        
        for i, product in enumerate(products):
            with cols[i % 3]:
                st.container()
                st.write(f"**{product.name}**")
                st.write(f"Rp{product.price:,.0f}")
                st.write("---")

    else:
        st.write("Yah maaf, tidak ada produk saat ini :(")

elif page == "Tambah Produk":
    st.write("## Tambah Produk")
    
    with st.form(key='add_product_form'):
        product_name = st.text_input("Nama Produk")
        product_price = st.number_input("Harga Produk", min_value=0)
        submit_button = st.form_submit_button(label='Tambah Produk')

        if submit_button:
            product_id = generate_random_id()

            new_product = Product(name=product_name, price=product_price, id=product_id)
            
            st.session_state.product_list.add_product(new_product)

            new_row = pd.DataFrame([[new_product.id, new_product.name, new_product.price]], columns=["ID", "Product_Name", "Price"])
            new_row.to_csv("product-items.csv", mode='a', header=False, index=False)

            st.success("Produk berhasil ditambahkan!")


elif page == "Manajemen Produk":
    st.write("## Manajemen Produk")
    
    products = st.session_state.product_list.get_all_products()
    
    if products:
        for product in products:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write(f"**{product.name}**")
            with col2:
                st.write(f"Rp{product.price:,.0f}")
            with col3:
                if product.is_active:
                    if st.button("Deactivate", key=product.id):
                        product.deactivate()
                        st.success(f"{product.name} dinonaktifkan.")
                        st.rerun()
                else:
                    if st.button("Activate", key=product.id):
                        product.activate()
                        st.success(f"{product.name} diaktifkan.")
                        st.rerun()

    else:
        st.write("Yah maaf, tidak ada produk saat ini :(")