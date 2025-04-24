import behave.__main__
import os
import sys

def main():
    # 🛠 Add src/main vào sys.path để Behave tìm thấy step trong steps/
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # 📍 Lấy path đến thư mục features
    feature_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "features"))

    # ✅ Gọi Behave
    behave.__main__.main([
        feature_path,
        "--no-capture",
        "--format=pretty"
        # "--tags=~@screenshot"
    ])

if __name__ == "__main__":
    main()
