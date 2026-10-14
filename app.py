
import streamlit as st

st.title("THẨM ĐỊNH TÍN DỤNG")
st.write("Nhập thông tin khách hàng để tính tỷ lệ DTI.")

# 1. NHẬP DỮ LIỆU
st.header("1. Thông tin khách hàng")

STV = st.number_input(
    "Số tiền vay (đồng)",
    min_value=1_000_000,
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
)

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

# 2. TÍNH TOÁN
if st.button("TÍNH DTI"):
    # Chuyển lãi suất từ % sang số thập phân
    lai_suat_thang = LS / 100 / 12

    # Tiền gốc trả mỗi tháng
    tien_goc_thang = STV / (THV * 12)

    # Tiền lãi tháng đầu
    tien_lai_thang_dau = STV * lai_suat_thang

    # Tổng tiền trả khoản vay mới trong tháng đầu
    tien_tra_no_moi = tien_goc_thang + tien_lai_thang_dau

    # Tổng nghĩa vụ trả nợ, gồm khoản vay mới và nợ cũ
    tong_no = tien_tra_no_moi + NC

    # Thu nhập sau khi trừ chi phí sinh hoạt
    thu_nhap_con_lai = TN - CPSH * SN

    st.header("2. Kết quả thẩm định")

    if thu_nhap_con_lai <= 0:
        st.error(
            "Không thể tính DTI vì thu nhập sau chi phí sinh hoạt "
            "phải lớn hơn 0."
        )
    else:
        # Tính tỷ lệ DTI
        DTI = tong_no / thu_nhap_con_lai

        st.metric("Tỷ lệ DTI", f"{DTI:.2%}")

        st.write(
            f"**Tiền gốc trả mỗi tháng:** "
            f"{tien_goc_thang:,.0f} đồng"
        )

        st.write(
            f"**Tiền lãi tháng đầu:** "
            f"{tien_lai_thang_dau:,.0f} đồng"
        )

        st.write(
            f"**Tổng nghĩa vụ trả nợ:** "
            f"{tong_no:,.0f} đồng/tháng"
        )

        st.write(
            f"**Thu nhập sau chi phí sinh hoạt:** "
            f"{thu_nhap_con_lai:,.0f} đồng/tháng"
        )

        # 3. KẾT LUẬN
        st.header("3. Kết luận")

        if DTI < 0.70:
            st.success("ĐƯỢC PHÉP CHO VAY")
        else:
            st.error("KHÔNG ĐƯỢC PHÉP CHO VAY")
