import sys
import os

# def before_all(context):
#     # Thêm đường dẫn đến thư mục steps trong main vào sys.path
#     steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main", "steps"))
#     print(f"🔍 Đang thêm đường dẫn steps: {steps_path}")  # Debug dòng này
#     if steps_path not in sys.path:
#         sys.path.insert(0, steps_path)
#     else:
#         print("✅ Đường dẫn steps đã có trong sys.path")
#
# def after_all(context):
#     # Kiểm tra xem sys.path có chứa bước này không
#     print(f"🔍 Đang kiểm tra sys.path: {sys.path}")

def before_scenario(context, scenario):
    print(f"--- START: {scenario.name}")

def after_scenario(context, scenario):
    print(f"--- END: {scenario.name}")
    if hasattr(context, "driver"):
        context.driver.quit()
