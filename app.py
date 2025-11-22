import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# 1. ĐỌC FILE CẤU HÌNH YAML
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Lỗi: Không tìm thấy file 'config.yaml'.")
    st.stop()

# 2. KHỞI TẠO AUTHENTICATOR (Truyền toàn bộ dictionary config)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
# Gọi hàm login. Đặt form ở cột chính ('main')
name, authentication_status, username = authenticator.login('Đăng nhập', 'main')

# 3. Xử lý logic theo trạng thái
if authentication_status:
    # --- Đã Đăng nhập thành công ---
    
    # Hiển thị nút Đăng xuất ở thanh bên (sidebar)
    with st.sidebar:
        st.success(f"Chào mừng, {name}!")
        authenticator.logout('Đăng xuất', 'main') 
        
    # --- NỘI DUNG ỨNG DỤNG CHÍNH ĐẶT Ở ĐÂY ---
    st.title("Ứng Dụng Chuyển Giọng Nói")
    st.info("Bạn đã đăng nhập thành công.")
    # ... (Phần code xử lý chuyển đổi giọng nói của bạn) ...

elif authentication_status == False:
    # --- Đăng nhập thất bại ---
    st.error('Tên đăng nhập/Mật khẩu không chính xác')

elif authentication_status == None:
    # --- Chưa đăng nhập (Lần đầu truy cập) ---
    st.title("Vui lòng Đăng nhập để sử dụng Ứng dụng")
    st.info('Nhập tên người dùng và mật khẩu của bạn để tiếp tục.')

