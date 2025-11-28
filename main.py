import pyautogui
import time
import os
import requests
import pygetwindow as gw

pyautogui.FAILSAFE = True 

notepad_icon_small_image = 'notepad_icon_small.png'
notepad_icon_medium_image = 'notepad_icon_medium.png'
notepad_icon_large_image = 'notepad_icon_large.png'
opened_noptepad_icon_image = 'opened_notepad_icon.png'
overwrite_save_popup_image = 'overwrite_popup.png'

OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "tjm-project")

def setup_directory():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")
    else:
        print(f"Directory exists: {OUTPUT_DIR}")

def define_icon_size():
    pyautogui.hotkey('win', 'm')
    time.sleep(2)

    icon_options = [
    (notepad_icon_small_image, "small", 0.9),
    (notepad_icon_medium_image, "medium", 0.9),
    (notepad_icon_large_image, "large", 0.9)
    ]

    for img_path, size_name, conf_level in icon_options:
        try:
            if pyautogui.locateCenterOnScreen(img_path, confidence=conf_level):
                print(f"Notepad icon size is {size_name}")
                return img_path
        except pyautogui.ImageNotFoundException:
            continue 
        except Exception as e:
            print(f"Error checking {size_name}: {e}")
            continue
    return False

def close_all_existing_notepads():
    """
    LOOPS through ALL open Notepad windows.
    Activates them one by one, maximizes, and closes them gracefully.
    """
    print("--- STEP 0: Cleaning up open Notepad windows ---")
    
    notepad_windows = gw.getWindowsWithTitle('Notepad')
    
    if not notepad_windows:
        print("   -> No existing Notepad windows found.")
        return

    print(f"   -> Found {len(notepad_windows)} open Notepad window(s). Closing them...")

    for win in notepad_windows:
        try:
            if not win.isActive:
                win.activate()
            time.sleep(0.5)

            print(f"   -> Closing window: {win.title}")
            pyautogui.hotkey('ctrl', 'shift', 'w')
            time.sleep(0.5)

            pyautogui.hotkey('alt', 'n')
            time.sleep(0.5)
            
        except Exception as e:
            print(f"   -> Could not close a window: {e}")
            try:
                win.close()
            except:
                pass

    print("--- Cleanup Complete ---\n")
    time.sleep(1)

def get_posts():
    print("Fetching data from API...")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
        if response.status_code == 200:
            return response.json()[:10]
    except requests.exceptions.RequestException as e:
        print(e)
        return []

def locate_and_open_notepad(correct_notepad_size_image):
    print("Step 1: Searching for Notepad icon...")
    try:
        pyautogui.hotkey('win', 'm')

        location = pyautogui.locateCenterOnScreen(correct_notepad_size_image, confidence=0.9)

        if location:
            print(f"   -> Icon found at {location}")
            pyautogui.moveTo(location)

            time.sleep(0.5) 
            pyautogui.doubleClick()
            return True
        else:
            print("   -> Icon NOT found.")
            return False
    except Exception as e:
        print(f"   -> Error searching for icon: {e}")
        return False
    
def verify_window_opened(timeout=10):

    print("Step 2: Verifying Notepad opened...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            if pyautogui.locateOnScreen(opened_noptepad_icon_image, confidence=0.8):
                print("   -> SUCCESS: Notepad window detected!")
                return True
        except pyautogui.ImageNotFoundException:
            pass
        
        time.sleep(1)
        print("   -> Waiting for window...")

    print("   -> FAILED: Notepad window did not appear within timeout.")
    return False

def clean_start():
    try:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
    except pyautogui.ImageNotFoundException:
        pass 
    return True
        
def save_and_close(post_id):

    filename = f"post_{post_id}.txt"
    full_path = os.path.join(OUTPUT_DIR, filename)

    print(f"[Action] Saving {filename}...")
    
    pyautogui.hotkey('ctrl', 'shift', 's') 
    time.sleep(1.0)

    pyautogui.write(full_path)
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(1.0)

    try:
        if pyautogui.locateOnScreen(overwrite_save_popup_image, confidence=0.8):
            pyautogui.press('left')
            pyautogui.press('enter')
    except pyautogui.ImageNotFoundException:
        pass 
    
    print("[Action] Closing Notepad...")
    pyautogui.hotkey('ctrl', 'w')
    try:
        if pyautogui.locateOnScreen(opened_noptepad_icon_image, confidence=0.8):
            return False
    except pyautogui.ImageNotFoundException:
            pass
    time.sleep(1.0) 

def write_into_notepad(post):
    post_id = post['id']
    title = post['title']
    body = post['body']

    print(f"\nProcessing Post ID: {post_id}")

    content = f"Title: {title}\n\n{body}"
    pyautogui.write(content, interval=0.1)
    save_and_close(post_id)

def main():
    pyautogui.FAILSAFE = True
    print("--- STARTING AUTOMATION JOB ---")
    close_all_existing_notepads()
    setup_directory()
    correct_notepad_size_image = define_icon_size()
    posts = get_posts()
    if not posts:
        print("No posts fetched. Exiting.")
        return

    for post in posts:

        if not locate_and_open_notepad(correct_notepad_size_image):
            print("CRITICAL: Could not find Notepad. Stopping.")
            break
        if not verify_window_opened():
            print("CRITICAL: Could not open Notepad. Stopping.")
            break

        time.sleep(1) 
        clean_start()
         
        write_into_notepad(post)
        time.sleep(1)

if __name__ == "__main__":
    main()