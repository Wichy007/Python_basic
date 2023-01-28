'''
#การกำหนดตัวแปร และสัญลักษ์ทางคณิตศาตร์

ประเภทข้อมูล
integer เลขจำนวนเต็ม
floating เลขทศนิยม
string ตัวอักษร
boolean ค่าจริงหรือเท็จ

x = 4
y = 2

x+y = 6 การรวมกัน
x-y = 2 การลบกัน
x*y = 8 การคูณกัน
x/y = 2 การหารกัน
x%y = 0 เศษจากการหาร
x**y = 16 ยกกำลัง
x//y = 2 ผลหารแบบไม่เอาเศษ หากมีเศษจะคืนค่าแค่จำนวนเต็ม

การเปรียบเทียบ(ส่วนใหญ่มักคืนค่าเป็น boolean)

> มากกว่า
>= มากกว่าหรือเท่ากับ
< น้อยกว่า
<= น้อยกว่าหรือเท่ากับ
== เท่ากับ
!= ไม่เท่ากับ

ค่าทางตรรกศาสตร์ (แสดงผลเป็น Boolean)
^ และ
v หรือ


x = 5
print(x)
x = 2
print(x)

x = 4
y = 3

z = x + y
print(z)

x = str(4.5)
y = '12'
z = x + y
print(z)

x = 5
x = x+3

--------------------------------------------------------------------------
#การสร้างเงื่อไข if, elif, else

score = 50


if score >= 80:
    print('Grade A')
    print('eiei')
elif score >= 70:
    print('Grade B')
elif score >= 60:
    print('Grade C')
else:
    print('Grade D')

--------------------------------------------------------------------------
#for loop การสร้างฟังก์ชันทำงานวนซ้ำ


for i in range(1,7):
    if i % 3 == 0: # เงื่อนไขเมื่อ i หารสาม ลงตัว (มีเศษเท่ากับศูนย์)
        break
# continue จะทำให้ลูปข้ามลูปนั้นไปเมื่อเงื่อนไขเป็นจริง
# break จะทำให้ลูปหยุดเมื่อเงื่อนไขเป็นจริง
    double = i * 2
    print(double)

--------------------------------------------------------------------------
# while loop ฟังชันก์วนซ้ำ
i = 3
while i => 3 :
    print(i)
    i += 1
    if i == 10:
        break


--------------------------------------------------------------------------
#การสร้าง Function ใว้ใช้งานเอง

def get_box_area(x,y,z):

    width = x
    lenght = y
    height = z
    if x < 0 or y < 0 or  z < 0:
        return 0
    box_area = width * lenght * height
    #print(box_area)
    return box_area # return ทำให้ฟังก์ชันคืนค่ากลับไปเก็บในตัวแปรที่เราตั้งขึ้น ในที่นี้คือ box_area และทำให้ฟังก์ชันหยุดทำงานได้ด้วย

print(get_box_area(-1,2,3))
print(get_box_area(2,3,4))
print(get_box_area(x=2,z=2,y=2))

--------------------------------------------------------------------------
# การสร้าง Module เพื่อเก็บฟังก์ชันต่างๆแยกไฟล์ใว้เพื่อรอเรียกใช้โดยการ Import



--------------------------------------------------------------------------
# การสร้าง desktop Application


import tkinter as tk

def set_massage():
    text = text_input.get()
    title_label.configure(text=text)



window = tk.Tk()
window.title('JustPython')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text='เมื่อรักฉันเกิด')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='Okay', command=set_massage)
ok_button.pack()



window.mainloop()

--------------------------------------------------------------------------
# แบบฝึกการสร้างแอปสูตรคูณ

'''

'''import tkinter as tk

def show_output():
    number = int(number_input.get())
    # คำสั่ง get จะคืนค่าเป็นข้อความ (string)
    if number == 0:
        output_label.configure(text='ผิดที่ใว้ใจ')
        return

    output = ''

    for i in range(1,13):
        output += str(number) + 'x' + str(i) + '=' + str(number*i) + '\n'


    output_label.configure(text=output)



window = tk.Tk()
window.title('JustPython')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window,text='สูตรคูณแม่')
title_label.pack(pady=20) # parameter padx, pady คือการเพิ่มพื้นที่ว่างในแนวแกน x และ y

number_input = tk.Entry(master=window, width=15)
number_input.pack()



go_button =tk.Button(master=window,text='ได้แก่',command=show_output, width=15, height=2)
go_button.pack(pady=20)

output_label = tk.Label(master=window)
output_label.pack(pady=20)


window.mainloop()
'''
import time as t
i = 4

while i > 3 :
    print(i)
    i += 1
    t.sleep(5)

