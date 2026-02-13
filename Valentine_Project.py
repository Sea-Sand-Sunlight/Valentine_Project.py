import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime
import os

# 1. Cấu hình giao diện
st.set_page_config(page_title="Love Mainnet 2026", page_icon="❤️", layout="centered")

# 2. CSS Tùy chỉnh: Màu tím và Font chữ lớn
st.markdown("""
    <style>
    /* Chỉnh dòng chúc mừng to như Subheader và có màu tím */
    .valentine-purple {
        font-family: 'Dancing Script', cursive;
        color: #8E44AD; /* Màu tím sang trọng */
        text-align: center;
        font-size: 32px; /* Kích thước tương đương Subheader */
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Tính toán thời gian HODL
start_date = datetime(2025, 6, 14)
now = datetime.now()
duration = now - start_date

# Header báo cáo
st.title("📊 LOVE MILESTONES REPORT")
st.subheader("Hệ thống: Tình yêu của Sea Thiên Bình & Rosy Bọ Cạp")

st.metric(label="⏱️ Tổng thời gian vận hành hệ thống (HODL)", 
          value=f"{duration.days} ngày", 
          delta="Chỉ số hạnh phúc đang tăng trưởng mạnh 🚀")

st.write("---")

# 4. Bug Report
st.error("### ⚠️ CRITICAL BUG REPORT")
st.warning("**CẢNH BÁO: Phát hiện 01 'Bug' nghiêm trọng!**")
st.info("**Lỗi: Em là 'Bug' duy nhất mà anh không bao giờ muốn fix.**")
st.success("**Status: Cứ để lỗi này tồn tại mãi mãi nhé!**")

# Dòng chữ chúc mừng: To như Subheader và màu Tím
st.markdown('<p class="valentine-purple">Chúc mừng Valentine, cô bé QA khó tính của anh! ❤️</p>', unsafe_allow_html=True)

# 5. Hình ảnh kỷ niệm
image_path = "ky_niem.jpg"
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Bản ghi hình ảnh: Khoảnh khắc hạnh phúc (UAT Passed)", use_container_width=True)

# 6. Nhạc tự động phát và HIỂN THỊ (Không giấu nữa)
st.write("### 🎵 Theme Song: Em đồng ý (I Do)")
st.video("https://www.youtube.com/watch?v=MW79zgnSF40&autoplay=1")

st.write("---")

# 7. Timeline - Trạng thái: In Love, Boom, Perfect, Running
st.write("### 📅 Dòng thời gian hệ thống (Timeline)")
data = {
    "Thời gian": ["23/09/1989", "25/10/1996", "04/05/2025", "14/06/2025", "14/02/2026"],
    "Sự kiện": [
        "Ngày anh Sea Thiên Bình chào đời",
        "Ngày em Rosy Bọ Cạp xuất hiện",
        "Ngày 2 đứa “va” vào cuộc đời nhau",
        "Ngày 'tình eo' chính thức gõ cửa con tim 2 đứa",
        "Happy Valentine kỷ niệm 8 tháng “iu” nhau (không ngừng nghỉ)"
    ],
    "Trạng thái": ["✅ In Love", "✅ In Love", "✅ Boom", "✅ Perfect", "🚀 Running"]
}
st.table(pd.DataFrame(data))

# 8. Biểu đồ Uptime
st.write("### 📈 Biểu đồ hiệu năng (Uptime)")
st.line_chart(pd.DataFrame([85, 92, 95, 99, 101], columns=["Chỉ số hạnh phúc (%)"]))

st.write("---")

# 9. Secret Log - Hiệu ứng Tuyết rơi lãng mạn
st.write("### 🔐 Secret Log (Phân quyền truy cập)")
access_code = st.text_input("Nhập Access Code (Gợi ý: 4 số ngày sinh của em):", type="password")
if access_code == "2510":
    st.snow() 
    st.info("### 💌 Message for Rosy:")
    st.markdown("""
    Cảm ơn Em yêu đã là 1 phần cực kỳ quan trọng trong cuộc đời anh, My Valentine 🥰 
    **Mãi bên nhau Em nhé!**
    """)
elif access_code:
    st.error("Access Denied! Sai mật mã rồi cô bé ơi.")

st.write("---")

# 10. Nút bấm LTS
if st.button("🚀 KÍCH HOẠT CHẾ ĐỘ LONG-TERM SUPPORT (LTS)"):
    st.snow()
    st.success("Hệ thống thông báo: Đã chuyển sang chế độ Vận hành vĩnh viễn (Lifetime Subscription)!")
    st.write("Dự án tình yêu đã chính thức vào giai đoạn Mainnet ổn định. Chúc mừng hai đứa mình!")

st.caption("© 2026 Valentine Report | Optimized for M1 Pro & iMac 128GB | Approved by QA Boss")

