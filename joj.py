import streamlit as st
import sqlite3
from streamlit_lottie import st_lottie
import requests
from PIL import Image


# Funkcija za učitavanje Lottie animacije s URL-a
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_style(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Postavljanje konfiguracije stranice
st.set_page_config(page_title="Cleanliness")


local_style("Style/style.css")

# Funkcija za stvaranje tablice recenzija u bazi podataka
def create_reviews_table():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (id INTEGER PRIMARY KEY, stan TEXT, recenzija TEXT, datum TEXT)''')
    conn.commit()
    conn.close()


class WebsiteConfiguration:
    title = ""
    contact_title = ""
    contact_phone = ""
    contact_email = ""
    offers_and_promotions = ""
    special_offers = ""
    page_watermark = ""
    deep_cleaning = ""
    deep_cleaning_desc = ""
    deep_cleaning_price = ""
    regular_maintenance = ""
    regular_maintenance_desc = ""
    regular_maintenance_price = ""
    garden_cleaning = ""
    garden_cleaning_desc = ""
    garden_cleaning_price = ""
    car_cleaning = ""
    car_cleaning_desc = ""
    car_cleaning_price = ""
    special_offers_text = ""


def configure_website_info(website_conf : WebsiteConfiguration, language):
    # postaviti varijable
    if language == "Hrvatski":
        website_conf.title = "Čistoća"
        website_conf.contact_title = "Javite nam se putem telefona ili e-poštom!"
        website_conf.contact_phone = "Telefon: 123-456-789"
        website_conf.contact_email = "Email: tvoj.mail@gmail.com"
        website_conf.offers_and_promotions = "Ponude i Promocije:"
        website_conf.special_offers = "Posebne ponude"
        website_conf.page_watermark = "©2024 Čistoća"
        website_conf.deep_cleaning = "Dubinsko čišćenje"
        website_conf.deep_cleaning_desc = "Ova usluga uključuje temeljito čišćenje kaučeva i podova."
        website_conf.deep_cleaning_price = "Cijena: 1000€ mjesečno"
        website_conf.regular_maintenance = "Redovno održavanje"
        website_conf.regular_maintenance_desc = "Ova usluga obuhvaća redovno usisavanje i brisanje prašine, kao i pranje prozora."
        website_conf.regular_maintenance_price = "Cijena: 800€ mjesečno"
        website_conf.garden_cleaning = "Čišćenje vrta"
        website_conf.garden_cleaning_desc = "Ova usluga uključuje temeljito čišćenje vrta."
        website_conf.garden_cleaning_price = "Cijena: 1200€ mjesečno"
        website_conf.car_cleaning = "Čišćenje automobila"
        website_conf.car_cleaning_desc = "Ova usluga uključuje temeljito čišćenje unutrašnjosti i eksterijera automobila."
        website_conf.car_cleaning_price = "Cijena: 500€ mjesečno"
        website_conf.special_offers_text = "- **10% popusta za nove klijente!**\n- **Program vjernosti: Nakon svakog 5. čišćenja, 50% popusta na sljedeće!**\n- **Besplatno procjenjivanje: Kontaktirajte nas za besplatnu procjenu vaših potreba za čišćenjem!**"
    else:
        website_conf.title = "Cleanliness"
        website_conf.contact_title = "Contact us by phone or email!"
        website_conf.contact_phone = "Phone: 123-456-789"
        website_conf.contact_email = "Email: your.email@gmail.com"
        website_conf.offers_and_promotions = "Offers and Promotions:"
        website_conf.special_offers = "Special Offers"
        website_conf.page_watermark = "©2024 Cleanliness"
        website_conf.deep_cleaning = "Deep Cleaning"
        website_conf.deep_cleaning_desc = "This service includes thorough cleaning of sofas and floors."
        website_conf.deep_cleaning_price = "Price: €1000 per month"
        website_conf.regular_maintenance = "Regular Maintenance"
        website_conf.regular_maintenance_desc = "This service includes regular vacuuming and dusting, as well as window washing."
        website_conf.regular_maintenance_price = "Price: €800 per month"
        website_conf.garden_cleaning = "Garden Cleaning"
        website_conf.garden_cleaning_desc = "This service includes thorough cleaning of the garden area."
        website_conf.garden_cleaning_price = "Price: €1200 per month"
        website_conf.car_cleaning = "Car Cleaning"
        website_conf.car_cleaning_desc = "This service includes thorough cleaning of the interior and exterior of the car."
        website_conf.car_cleaning_price = "Price: €500 per month"
        website_conf.special_offers_text = "- **10% discount for new clients!**\n- **Loyalty program: After every 5th cleaning, 50% off the next one!**\n- **Free assessment: Contact us for a free assessment of your cleaning needs!**"


# Glavna funkcija
def main():
    # create_reviews_table()

    main_container = st.container()

    # Odabir jezika
    lang = st.sidebar.selectbox("Select language", ["Hrvatski", "English"])

    website_info = WebsiteConfiguration()

    configure_website_info(website_info, lang)
    # zamjeniti title, contant_title, ... s website_info.title, website_info, content_title

    if lang == "Hrvatski":
        title = "Čistoća"
        contact_title = "Javite nam se putem telefona ili e-poštom!"
        contact_phone = "Telefon: 123-456-789"
        contact_email = "Email: tvoj.mail@gmail.com"
        offers_and_promotions = "Ponude i Promocije:"
        special_offers = "Posebne ponude"
        page_watermark = "©2024 Čistoća"
        deep_cleaning = "Dubinsko čišćenje"
        deep_cleaning_desc = "Ova usluga uključuje temeljito čišćenje kaučeva i podova."
        deep_cleaning_price = "Cijena: 1000€ mjesečno"
        regular_maintenance = "Redovno održavanje"
        regular_maintenance_desc = "Ova usluga obuhvaća redovno usisavanje i brisanje prašine, kao i pranje prozora."
        regular_maintenance_price = "Cijena: 800€ mjesečno"
        garden_cleaning = "Čišćenje vrta"
        garden_cleaning_desc = "Ova usluga uključuje temeljito čišćenje vrta."
        garden_cleaning_price = "Cijena: 1200€ mjesečno"
        car_cleaning = "Čišćenje automobila"
        car_cleaning_desc = "Ova usluga uključuje temeljito čišćenje unutrašnjosti i eksterijera automobila."
        car_cleaning_price = "Cijena: 500€ mjesečno"
        special_offers_text = "- **10% popusta za nove klijente!**\n- **Program vjernosti: Nakon svakog 5. čišćenja, 50% popusta na sljedeće!**\n- **Besplatno procjenjivanje: Kontaktirajte nas za besplatnu procjenu vaših potreba za čišćenjem!**"
    else:
        title = "Cleanliness"
        contact_title = "Contact us by phone or email!"
        contact_phone = "Phone: 123-456-789"
        contact_email = "Email: your.email@gmail.com"
        offers_and_promotions = "Offers and Promotions:"
        special_offers = "Special Offers"
        page_watermark = "©2024 Cleanliness"
        deep_cleaning = "Deep Cleaning"
        deep_cleaning_desc = "This service includes thorough cleaning of sofas and floors."
        deep_cleaning_price = "Price: €1000 per month"
        regular_maintenance = "Regular Maintenance"
        regular_maintenance_desc = "This service includes regular vacuuming and dusting, as well as window washing."
        regular_maintenance_price = "Price: €800 per month"
        garden_cleaning = "Garden Cleaning"
        garden_cleaning_desc = "This service includes thorough cleaning of the garden area."
        garden_cleaning_price = "Price: €1200 per month"
        car_cleaning = "Car Cleaning"
        car_cleaning_desc = "This service includes thorough cleaning of the interior and exterior of the car."
        car_cleaning_price = "Price: €500 per month"
        special_offers_text = "- **10% discount for new clients!**\n- **Loyalty program: After every 5th cleaning, 50% off the next one!**\n- **Free assessment: Contact us for a free assessment of your cleaning needs!**"

    if lang == "Hrvatski":
        options = ["Početna", "Usluge", "Novo Polje"]  # Dodana opcija "Novo Polje"
        selected_option = st.radio("Navigacija", options)
    else:
        options = ["Home", "Services", "New Field"]  # Dodana opcija "New Field"
        selected_option = st.radio("Navigation", options)

    if selected_option == "Početna" or selected_option == "Home":
        if lang == "Hrvatski":
            with main_container:
                st.markdown("""
                    ## O nama
                    Dobrodošli na našu platformu za čišćenje. Posvećeni smo pružanju visokokvalitetnih usluga čišćenja našim klijentima.
                    Naša misija je učiniti vaše životne i radne prostore čistima i udobnima.
                    Ako imate bilo kakvih pitanja ili upita, slobodno nas kontaktirajte putem telefona ili e-pošte.
                """)
        else:
            with main_container:
                st.markdown("""
                    ## About Us
                    Welcome to our cleaning platform. We are dedicated to providing high-quality cleaning services to our clients.
                    Our mission is to make your living and working spaces clean and comfortable.
                    If you have any questions or inquiries, feel free to contact us by phone or email.
                """)

        input_title_string = ""
        input_name_string = ""
        input_email_string = ""
        input_msg_string = ""

        if lang == "Hrvatski":
            input_title_string = "Dođite u Kontakt s Nama!"
            input_name_string = "Vase ime"
            input_email_string = "Vas email"
            input_msg_string = "Vasa poruka"
        else:
            input_title_string = "Get in Contact With Us!"
            input_name_string = "Your name"
            input_email_string = "Your email"
            input_msg_string = "Your message"

        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header(input_title_string)
            st.write("##")

        # Documention: https://formsubmit.co/ !!! change email address !!!
        contact_form = f"""
            <form action="https://formsubmit.co/ante.arambasic00@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="{input_name_string}" length=31000 required>
             <input type="email" name="email" placeholder="{input_email_string}" required>
             <textarea name=ˇmessage" id="message" placeholder="{input_msg_string}" required></textarea><br />
             <button type="submit">Send</button>
        </form>
        """
        left_colum, right_colum = st.columns([0.6, 0.4])

        with left_colum:
            st.markdown(contact_form, unsafe_allow_html=True)

        with right_colum:
            # Dodavanje Lottie animacije ispod teksta "O nama"
            lottie_coding = load_lottieurl("https://lottie.host/365598bf-526c-4951-96f1-75ca60aa92c3/WOWxrN6RTX.json")
            if lottie_coding:
                st_lottie(lottie_coding, height=375, key="coding", )

        st.sidebar.title(contact_title)
        st.sidebar.write("\n\n### " + contact_phone)
        st.sidebar.write(contact_email)
        st.sidebar.write("##")

        # Dodavanje linkova između sekcija "Contact us by phone or email!" i "Offers and Promotions:"
        if lang == "Hrvatski":
            st.sidebar.markdown(
                """
                ### Korisni linkovi:
                - [O nama](https://www.example.com/about)
                - [Usluge](https://www.example.com/services)
                - [Kontakt](https://www.example.com/contact)
                """,
                unsafe_allow_html=True,
            )
        else:
            st.sidebar.markdown(
                """
                ### Useful Links:
                - [About Us](https://www.example.com/about)
                - [Services](https://www.example.com/services)
                - [Contact](https://www.example.com/contact)
                """,
                unsafe_allow_html=True,
            )
    elif selected_option == "Usluge" or selected_option == "Services":
        with st.expander(deep_cleaning):
            st.write(deep_cleaning_desc)
            st.write(deep_cleaning_price)
        st.write("##")

        with st.expander(regular_maintenance):
            st.write(regular_maintenance_desc)
            st.write(regular_maintenance_price)
        st.write("##")

        st.sidebar.write("\n\n### " + offers_and_promotions)
        with st.sidebar.expander(special_offers):
            st.write(special_offers_text)

        # Dodavanje dodatnih polja za čišćenje vrta i čišćenje automobila
        with st.expander(garden_cleaning):
            st.write(garden_cleaning_desc)
            st.write(garden_cleaning_price)
        st.write("##")

        with st.expander(car_cleaning):
            st.write(car_cleaning_desc)
            st.write(car_cleaning_price)
        st.write("##")

    # Dodavanje watermark-a
    st.markdown(
        f"""<div style="position: fixed; bottom: 10px; right: 10px; color: lightgrey;">{page_watermark}</div>""",
        unsafe_allow_html=True,
    )

    # Dodavanje novog polja ispod navigacije
    if selected_option == "Novo Polje" or selected_option == "New Field":
        with st.container():
            st.header("My Projects")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                # Instert image
                image = Image.open("images/slikar.png")
                st.image(image, caption="Slika", use_column_width=True)
            with text_column:
                st.subheader("Naslov")
                st.write("Ovdje su slike prije i poslije čišćenja.")

        st.write("##")  # Dodan razmak ispod "Novo Polje"


if __name__ == "__main__":
    main()
