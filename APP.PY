
import streamlit as st

# Tiêu đề ứng dụng
st.title("THẨM ĐỊNH TÍN DỤNG")
st.write("Tính tỷ lệ DTI và đánh giá khả năng vay vốn của khách hàng.")

# 1. Nhập thông tin khách hàng
st.header("1. Thông tin khách hàng")

STV = st.number_input(
    "Số tiền vay (đồng)",
    min_value=0,
    value=800_000_000,
    step=10_000_000
)

THV = st.number_input(
    "Thời hạn vay (năm)",
    min_value=1,
    value=5,
    step=1
)

LS = st.number_input(
    "Lãi suất vay (%/năm)",
    min_value=0.0,
    value=12.0,
    step=0.5
) / 100

TN = st.number_input(
    "Thu nhập hàng tháng (đồng)",
    min_value=1,
    value=45_000_000,
    step=1_000_000
)

NC = st.number_input(
    "Khoản nợ cũ phải trả hàng tháng (đồng)",
    min_value=0,
    value=10_000_000,
    step=1_000_000
)

CPSH = st.number_input(
    "Chi phí sinh hoạt mỗi người/tháng (đồng)",
    min_value=0,
    value=4_000_000,
    step=500_000
)

SN = st.number_input(
    "Số người trong gia đình",
    min_value=1,
    value=3,
    step=1
)

# 2. Tính toán DTI
st.header("2. Kết quả thẩm định")

# Tiền gốc trả mỗi tháng + tiền lãi tháng đầu
tien_tra_no_moi = STV / (THV * 12) + STV * (LS / 12)

# Tổng nghĩa vụ trả nợ mỗi tháng
tong_no = tien_tra_no_moi + NC

# Thu nhập sau khi trừ chi phí sinh hoạt
thu_nhap_con_lai = TN - CPSH * SN

# Kiểm tra dữ liệu trước khi tính DTI
if thu_nhap_con_lai <= 0:
    st.error("Thu nhập sau chi phí sinh hoạt phải lớn hơn 0. Không thể tính DTI.")
else:
    DTI = tong_no / thu_nhap_con_lai

    # Hiển thị kết quả
    st.metric("Tỷ lệ DTI", f"{DTI:.2%}")

    st.write(f"**Tiền trả khoản vay mới (tháng đầu):** {tien_tra_no_moi:,.0f} đồng")
    st.write(f"**Tổng nghĩa vụ trả nợ hàng tháng:** {tong_no:,.0f} đồng")
    st.write(f"**Thu nhập sau chi phí sinh hoạt:** {thu_nhap_con_lai:,.0f} đồng")

    # 3. Kết luận theo yêu cầu cuối của đề bài
    if DTI < 0.7:
        st.error("KẾT LUẬN: KHÔNG ĐƯỢC VAY")
    else:
        st.success("KẾT LUẬN: ĐƯỢC PHÉP CHO VAY")

