
# รับความน่าจะเป็นการเลือกกล่อง
p_red = float(input("ความน่าจะเป็นเลือกกล่องแดง (เช่น 0.4): "))
p_blue = float(input("ความน่าจะเป็นเลือกกล่องน้ำเงิน (เช่น 0.6): "))

# รับจำนวนผลไม้ในกล่องแดง
apple_red = int(input("จำนวน Apple ในกล่องแดง: "))
orange_red = int(input("จำนวน Orange ในกล่องแดง: "))

# รับจำนวนผลไม้ในกล่องน้ำเงิน
apple_blue = int(input("จำนวน Apple ในกล่องน้ำเงิน: "))
orange_blue = int(input("จำนวน Orange ในกล่องน้ำเงิน: "))

# คำนวณผลรวมแต่ละกล่อง
total_red = apple_red + orange_red
total_blue = apple_blue + orange_blue

# ความน่าจะเป็นแบบมีเงื่อนไข
p_a_given_red = apple_red / total_red
p_o_given_red = orange_red / total_red

p_a_given_blue = apple_blue / total_blue
p_o_given_blue = orange_blue / total_blue

# ความน่าจะเป็นหยิบได้ Apple และ Orange
p_F_a = p_a_given_red * p_red + p_a_given_blue * p_blue
p_F_o = p_o_given_red * p_red + p_o_given_blue * p_blue

# Bayes: ความน่าจะเป็นว่าถ้าหยิบได้ Orange มาจากกล่องแดง
p_red_given_o = (p_o_given_red * p_red) / p_F_o

# แสดงผลลัพธ์
print("\n=== ผลลัพธ์ ===")
print(f"P(F = Apple) = {p_F_a:.4f}")
print(f"P(F = Orange) = {p_F_o:.4f}")
print(f"P(Red | Orange) = {p_red_given_o:.4f}")
