from pyscript import document, display


grade10= {"Clarence Mari", "Yoo Jeongyeon", "Im Nayeon", "Hirai Momo", "Minatozaki Sana"}

grade9= {"Park Jihyo", "Myoui Mina", "Kim Dahyun", "Son Chaeyoung", "Chou Tzuyu",}

grade8= {"Kim Min-ji", "Phạm Ngọc Hân / Hanni Pham", "Danielle Marsh", "Mo Ji-hye",}

grade7={"Kang Hae-rin", "Lee Hye-in"}

All_Grade_Levels= grade7 | grade8 | grade9 | grade10 



display( grade7 | grade8 | grade9 | grade10)#shows the members
display(len(grade10 | grade9 | grade8 | grade7))#gives the total number of the members

