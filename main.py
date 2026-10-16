from pyscript import document, display

#Defines the variables
grade7 = {"Kang Hae-rin", "Lee Hye-in"}
grade8 = {"Kim Min-ji", "Phạm Ngọc Hân / Hanni Pham", "Danielle Marsh", "Mo Ji-hye"}
grade9 = {"Park Jihyo", "Myoui Mina", "Kim Dahyun", "Son Chaeyoung", "Chou Tzuyu"}
grade10 = {"Clarence Mari", "Yoo Jeongyeon", "Im Nayeon", "Hirai Momo", "Minatozaki Sana"}

#This will trigger the function after clickking the submit button
def verify_member(event):
  first_name = document.getElementById("fname").value
  last_name = document.getElementById("lname").value
  
  new_member_name = f"{first_name} {last_name}"
  
  new_member_set = {new_member_name}
  
  master_club_set = grade7 | grade8 | grade9 | grade10 | new_member_set # combining them 
  
  formatted_members_list = "<br>".join(sorted(master_club_set))#This will sort so that it is sorted properly
 
  total_members_count = len(master_club_set)#This provides the number of members
  
  output_content = f"<b>Total Number of Members:</b> {total_members_count}<br><br><b>Full List of All Members:</b><br>{formatted_members_list}"
  
  display(output_content, target="result", append=False)#This will display the code
  
