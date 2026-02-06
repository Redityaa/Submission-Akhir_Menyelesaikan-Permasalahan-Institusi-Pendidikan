import streamlit as st
import pandas as pd
import joblib
import json

# Konfigurasi Halaman
st.set_page_config(
    page_title="Jaya Jaya Institut - Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load Model & Columns
@st.cache_resource
def load_assets():
    try:
        model = joblib.load('model/model.joblib')
        with open('model/model_columns.json', 'r') as f:
            columns = json.load(f)
        return model, columns
    except FileNotFoundError:
        st.error("File model atau columns tidak ditemukan. Pastikan Anda sudah menjalankan notebook dan menyimpan model!")
        return None, None

model, model_columns = load_assets()

# Judul & Deskripsi
st.title("🎓 Sistem Deteksi Dini Dropout Mahasiswa")
st.markdown("""
Aplikasi ini dirancang untuk membantu Jaya Jaya Institut mendeteksi siswa yang berisiko **Dropout** sedini mungkin 
berdasarkan data akademik dan demografis mereka.
""")

st.divider()

if model is not None:
    # Form Input Data (Dibagi 3 Kolom)
    col1, col2, col3 = st.columns(3)

    # Dictionary untuk menyimpan input user
    input_data = {}

    with col1:
        st.subheader("👤 Data Demografis")
        input_data['Marital status'] = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6], index=0, help="1: Single, 2: Married, 3: Widower, 4: Divorced 5: Facto union 6: Legally separated")
        input_data['Gender'] = st.selectbox("Gender", [0, 1], format_func=lambda x: "Wanita" if x == 0 else "Pria")
        input_data['Age at enrollment'] = st.number_input("Usia saat Mendaftar", min_value=17, max_value=70, value=20)
        input_data['Displaced'] = st.selectbox("Status Rantau (Displaced)", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        input_data['International'] = st.selectbox("Mahasiswa Internasional", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        
        with st.expander("Detail Orang Tua & Lainnya"):
            input_data["Mother's qualification"] = st.number_input("Kualifikasi Ibu", value=1, help="1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 22 - Technical-professional course 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)")
            input_data["Father's qualification"] = st.number_input("Kualifikasi Ayah", value=1, help="1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 22 - Technical-professional course 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)")
            input_data["Mother's occupation"] = st.number_input("Pekerjaan Ibu", value=1, help="0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants")
            input_data["Father's occupation"] = st.number_input("Pekerjaan Ayah", value=1, help="0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants")
            input_data['Nacionality'] = st.number_input("Kewarganegaraan", value=1, help="1 - Portuguese; 2 - German; 6 - Spanish; 11 - Italian; 13 - Dutch; 14 - English; 17 - Lithuanian; 21 - Angolan; 22 - Cape Verdean; 24 - Guinean; 25 - Mozambican; 26 - Santomean; 32 - Turkish; 41 - Brazilian; 62 - Romanian; 100 - Moldova (Republic of); 101 - Mexican; 103 - Ukrainian; 105 - Russian; 108 - Cuban; 109 - Colombian")
            input_data['Educational special needs'] = st.selectbox("Kebutuhan Khusus", [0, 1])

    with col2:
        st.subheader("💰 Data Finansial & Makro")
        input_data['Tuition fees up to date'] = st.selectbox("SPP Tepat Waktu?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak (Nunggak)")
        input_data['Scholarship holder'] = st.selectbox("Penerima Beasiswa?", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        input_data['Debtor'] = st.selectbox("Memiliki Hutang?", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        
        st.markdown("---")
        st.caption("Indikator Ekonomi Makro")
        input_data['Unemployment rate'] = st.number_input("Tingkat Pengangguran", value=10.0)
        input_data['Inflation rate'] = st.number_input("Tingkat Inflasi", value=1.0)
        input_data['GDP'] = st.number_input("GDP", value=0.0)

    with col3:
        st.subheader("📚 Data Akademik")
        
        # Semester 1
        st.markdown("**Semester 1**")
        input_data['Curricular units 1st sem (credited)'] = st.number_input("SKS Diakui (Sem 1)", value=0)
        input_data['Curricular units 1st sem (enrolled)'] = st.number_input("SKS Diambil (Sem 1)", value=5)
        input_data['Curricular units 1st sem (evaluations)'] = st.number_input("Jumlah Evaluasi (Sem 1)", value=5)
        input_data['Curricular units 1st sem (approved)'] = st.number_input("SKS Lulus (Sem 1)", value=5)
        input_data['Curricular units 1st sem (grade)'] = st.number_input("Nilai Rata-rata (Sem 1)", value=12.0)
        input_data['Curricular units 1st sem (without evaluations)'] = st.number_input("Tanpa Evaluasi (Sem 1)", value=0)

        # Semester 2
        st.markdown("**Semester 2**")
        input_data['Curricular units 2nd sem (credited)'] = st.number_input("SKS Diakui (Sem 2)", value=0)
        input_data['Curricular units 2nd sem (enrolled)'] = st.number_input("SKS Diambil (Sem 2)", value=5)
        input_data['Curricular units 2nd sem (evaluations)'] = st.number_input("Jumlah Evaluasi (Sem 2)", value=5)
        input_data['Curricular units 2nd sem (approved)'] = st.number_input("SKS Lulus (Sem 2)", value=5, help="Fitur paling berpengaruh!")
        input_data['Curricular units 2nd sem (grade)'] = st.number_input("Nilai Rata-rata (Sem 2)", value=12.0)
        input_data['Curricular units 2nd sem (without evaluations)'] = st.number_input("Tanpa Evaluasi (Sem 2)", value=0)

        # Input tambahan
        with st.expander("Input Akademik Lainnya"):
             input_data['Application mode'] = st.number_input("Mode Aplikasi", value=1, help="1 - 1st phase - general contingent 2 - Ordinance No. 612/93 5 - 1st phase - special contingent (Azores Island) 7 - Holders of other higher courses 10 - Ordinance No. 854-B/99 15 - International student (bachelor) 16 - 1st phase - special contingent (Madeira Island) 17 - 2nd phase - general contingent 18 - 3rd phase - general contingent 26 - Ordinance No. 533-A/99, item b2) (Different Plan) 27 - Ordinance No. 533-A/99, item b3 (Other Institution) 39 - Over 23 years old 42 - Transfer 43 - Change of course 44 - Technological specialization diploma holders 51 - Change of institution/course 53 - Short cycle diploma holders 57 - Change of institution/course (International)")
             input_data['Application order'] = st.number_input("Urutan Aplikasi", value=1, help="between 0 - first choice; and 9 last choice")
             input_data['Course'] = st.number_input("Kode Jurusan", value=1, help="33 - Biofuel Production Technologies 171 - Animation and Multimedia Design 8014 - Social Service (evening attendance) 9003 - Agronomy 9070 - Communication Design 9085 - Veterinary Nursing 9119 - Informatics Engineering 9130 - Equinculture 9147 - Management 9238 - Social Service 9254 - Tourism 9500 - Nursing 9556 - Oral Hygiene 9670 - Advertising and Marketing Management 9773 - Journalism and Communication 9853 - Basic Education 9991 - Management (evening attendance)")
             input_data['Daytime/evening attendance\t'] = st.selectbox("Waktu Kuliah", [1, 0], format_func=lambda x: "Siang" if x == 1 else "Malam")
             input_data['Previous qualification'] = st.number_input("Kualifikasi Sebelumnya", value=1, help="1 - Secondary education 2 - Higher education - bachelor's degree 3 - Higher education - degree 4 - Higher education - master's 5 - Higher education - doctorate 6 - Frequency of higher education 9 - 12th year of schooling - not completed 10 - 11th year of schooling - not completed 12 - Other - 11th year of schooling 14 - 10th year of schooling 15 - 10th year of schooling - not completed 19 - Basic education 3rd cycle (9th/10th/11th year) or equiv. 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 42 - Professional higher technical course 43 - Higher education - master (2nd cycle)")
             input_data['Previous qualification (grade)'] = st.number_input("Nilai Kualifikasi Sebelumnya", value=130.0)
             input_data['Admission grade'] = st.number_input("Nilai Ujian Masuk", value=130.0)

    # Tombol Prediksi
    st.divider()
    
    # Konversi dictionary ke DataFrame sesuai urutan kolom model
    input_df = pd.DataFrame([input_data])
    
    input_df = input_df[model_columns]

    if st.button("🔍 Prediksi Risiko Dropout"):
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        st.subheader("Hasil Analisis:")
        
        if prediction == 0:
            st.error(f"⚠️ **BERISIKO TINGGI DROPOUT**")
            st.write(f"Probabilitas Dropout: **{probability[0]*100:.2f}%**")
            st.warning("Rekomendasi: Segera jadwalkan sesi bimbingan konseling dan cek status keuangan mahasiswa.")
        else:
            st.success(f"✅ **DIPREDIKSI LULUS (GRADUATE)**")
            st.write(f"Probabilitas Lulus: **{probability[1]*100:.2f}%**")
            st.info("Rekomendasi: Pertahankan performa akademik.")

else:
    st.warning("Model belum dimuat.")