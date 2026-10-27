 # Danh sách để lưu các công việc 
tasks = [] 
def add_task(task_name): 
"""Thêm một công việc mới vào danh sách.""" 
tasks.append(task_name) 
print(f"Đã thêm công việc: '{task_name}'") 
# --- Điểm bắt đầu của chương trình --- 
if __name__ == "__main__": 
print("Chào mừng đến với ứng dụng To-Do List!") 
add_task("Học bài Git và GitHub") 
add_task("Làm bài tập thực hành ở nhà") 
 def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        return True
    return False
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        return True
    return False