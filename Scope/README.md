# python101
 ถ้าเรานำตัวแปรแบบ Global มากำหนดค่าอย่างใดอย่างหนึ่งแล้วเหมือนการสร้างตัวแปรขึ้นมาใหม่ ซึ่งผลที่ได้ คือตัวแปร Global นั้นจะกลายเป็นตัวแปรแบบ Local ในฟังก์ชั่นที่เรียกใช้งาน แต่ก็จะไม่ส่งผลต่อตัวแปร Global เดิม และไม่ส่งผลต่อฟังก์ชันอื่นๆที่เรียกใช้ตัวแปรนั้น

หากเราจำเป็นต้องแก้ไขค่าของตัวแปรแบบ Global ในฟังก์ชันใดฟังก์ชันหนึ่งและให้ส่งผลไปถึงฟังก์ชันอื่นๆ ที่เรียกใช้ตัวแปรแบบดังกล่าวด้วย สามารถทำการได้โดยการระบุคีย์เวิร์ด global นำหน้าชื่อตัวแปรนั้น