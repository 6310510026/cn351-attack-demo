# cn351-attack-demo

Test Access Controls
   6.3 Test with Limited Access
Installation
   1. cd cn351-attack-demo
   2. python -m venv .venv
   3. python -m pip install django
   4. python manage.py runserver

Description
   Contacts: เป็นเว็บที่เก็บรายชื่อเบอร์โทรศัพท์
   ในการทดสอบด้วยการเข้าถึงที่ถูกจำกัด โจมตีผ่าน URL ที่ทราบ โดยช่องโหว่ที่เกิดขึ้น คือ การกำหนดให้ user ไม่สามารถคลิกหรือมองเห็น link ที่ถูกจำกัดสิทธิ์ได้ แต่ยังสามารถเข้าถึงสิทธิ์นั้นผ่าน URL ได้ ทำให้ user มีโอกาสในการเข้าถึงสิทธิ์ที่ถูกจำกัดได้เหมือนกับ admin
   
     admin (สิทธิ์สูงกว่า user)
       - admin สามารถเพิ่มเบอร์โทรศัพท์ได้
       - admin สามารถดู แก้ไข และลบเบอร์โทรศัพท์ที่ admin และ user สร้างเพิ่มเข้ามาได้ 

     user (สิทธิ์ต่ำกว่า admin)
	 - user สามารถเพิ่มเบอร์โทรศัพท์ได้
       - user สามารถดูเบอร์โทรศัพท์ที่ admin และ user เพิ่มเข้ามาได้
       - user สามารถแก้ไขและลบได้ เฉพาะเบอร์โทรศัพท์ที่ user นั้นเป็นคนเพิ่มเข้ามาเท่านั้น
   
     Roles
       admin
       username: admin
       password: 1234

       user
       username: user
       password: user1234

       user
       username: myname
       password: mypass1234
