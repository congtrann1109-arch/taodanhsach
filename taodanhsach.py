import pyperclip  # pip install pyperclip

step = 30
count = 8
suffixes = ["LE", "LC", "C", "RC", "RE"]

while True:
    run = input("Nhập thông tin Run (Enter để thoát): ")
    if run.strip() == "":
        break

    min_value = input("Nhập thông tin (một số nguyên): ")
    if not min_value.strip().isdigit():
        print("❌ Vui lòng nhập số nguyên!")
        continue

    min_value = int(min_value)

    results = []
    for i in range(count):
        value = min_value + i * step
        for s in suffixes:
            results.append(f"{run}-{value}-{s}")

    output = "\n".join(results)
    try:
        pyperclip.copy(output)
        print("\n✅ Danh sách đã được sao chép vào clipboard:\n")
    except:
        print("\n⚠️ Không copy được clipboard (máy build online). Dưới đây là kết quả:\n")

    print(output)
    input("\n➡️ Ấn phím bất kỳ để tạo danh sách mới, hoặc Enter để thoát...")
