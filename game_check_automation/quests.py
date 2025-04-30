import pyautogui
import time
import pandas as pd
import os
from select_area import get_user_selected_area
from select_folder import select_folder
from select_file import select_file
import sys


def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


base_path = get_base_path()
images_dir = os.path.join(base_path, '_internal', 'images')


def clean_ids(ids):
    cleaned_qids = []
    for i in ids:
        if pd.isna(i):
            continue  # Skip NaN values
        # Check if the ID ends with '_NAME' and remove it
        cleaned_qid = str(i)
        if cleaned_qid.endswith('_NAME'):
            cleaned_qid = cleaned_qid[:-5]  # Remove the last 5 characters
        cleaned_qids.append(cleaned_qid)
    return cleaned_qids


def automate_quests():

    # images_dir = 'images'
    # Select folder to save screenshots
    screenshots_folder = select_folder()
    if not screenshots_folder:
        print("No folder selected. Exiting...")
        return

    # Select the Excel file with IDs
    excel_file = select_file()
    if not excel_file:
        print("No file selected. Exiting...")
        return

    # Load IDs from the Excel file
    ids_df = pd.read_excel(excel_file)
    ids = ids_df['ID'].dropna().astype(str).tolist()  # Ensure all IDs are treated as strings
    # Clean IDs
    cleaned_qids = clean_ids(ids)

    # Get the user-selected region
    x, y, width, height = get_user_selected_area()
    region = (x, y, width, height)

    try:
        # Step 1: Skip the initial dialog
        close_dlg = pyautogui.locateOnScreen(os.path.join(images_dir, 'close.png'), confidence=0.9, grayscale=True)
        if close_dlg:
            pyautogui.click(close_dlg)

            time.sleep(2)

            # Perform 3 sec hold on the profile icon
            profile = pyautogui.locateOnScreen(os.path.join(images_dir, 'profile.png'), confidence=0.9, grayscale=True)
            pyautogui.moveTo(profile)
            pyautogui.mouseDown()
            time.sleep(3)
            pyautogui.mouseUp()

            time.sleep(2)

            # Skip tutorial
            move_skip_x = region[0] + int(width * 0.5)
            move_skip_y = region[1] + int(height * 0.72)
            skip_ok = pyautogui.moveTo(move_skip_x, move_skip_y)
            pyautogui.click(skip_ok)

            time.sleep(5) # wait for animation
    except:
        pass

    # Step 2: Open cheats menu
    profile = pyautogui.locateOnScreen(os.path.join(images_dir, 'profile.png'), confidence=0.9, grayscale=True)
    pyautogui.moveTo(profile)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

    time.sleep(2)

    # Open Time cheats
    try:
        time_cheats = pyautogui.locateOnScreen(os.path.join(images_dir, 'time.png'), confidence=0.9,  grayscale=True)
        if time_cheats:
            pyautogui.click(time_cheats)

    except:
        try:
            time_cheats_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'timeja.png'), confidence=0.9,
                                                  grayscale=True)
            if time_cheats_ja:
                pyautogui.click(time_cheats_ja)
        except:
            time_cheats_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'timeko.png'), confidence=0.9,
                                                      grayscale=True)
            pyautogui.click(time_cheats_ko)
    time.sleep(1)

    # Reset Speed
    move_reset_x = region[0] + int(width * 0.20)
    move_reset_y = region[1] + int(height * 0.70)
    reset_speed = pyautogui.moveTo(move_reset_x, move_reset_y)
    pyautogui.click(reset_speed)
    time.sleep(1)

    # Increase time rate
    move_rate_x = region[0] + int(width * 0.12)
    move_rate_y = region[1] + int(height * 0.63)
    time_rate_plus = pyautogui.moveTo(move_rate_x, move_rate_y)
    pyautogui.click(time_rate_plus, clicks=5, interval=0.25)
    time.sleep(1)

    # Close the time cheats menu
    pyautogui.press('esc')
    time.sleep(1)

    # Step 3: Enter the cheats UI windows and open the UI Quest tab
    try:
        ui_cheats = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiwin.png'), confidence=0.9,  grayscale=True)
        if ui_cheats:
            pyautogui.click(ui_cheats)
    except:
        try:
            ui_cheats_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiwinja.png'), confidence=0.9, grayscale=True)
            if ui_cheats_ja:
                pyautogui.click(ui_cheats_ja)
        except:
            ui_cheats_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiwinko.png'), confidence=0.9,
                                                    grayscale=True)
            pyautogui.click(ui_cheats_ko)

    time.sleep(1)

    try:
        ui_quest = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiquests.png'), confidence=0.9,  grayscale=True)
        if ui_quest:
            pyautogui.click(ui_quest)
    except:
        try:
            ui_quest_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiquestsja.png'), confidence=0.9,
                                               grayscale=True)
            if ui_quest_ja:
                pyautogui.click(ui_quest_ja)
        except:
            ui_quest_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'uiquestsko.png'), confidence=0.9,
                                                   grayscale=True)
            pyautogui.click(ui_quest_ko)

    time.sleep(1)

    # Loop to enter IDs and perform actions
    for id in cleaned_qids:
        # Step 4: Enter the ID and perform actions

        move_qinput_x = region[0] + int(width * 0.23)
        move_qinput_y = region[1] + int(height * 0.66)
        quest_id_field = pyautogui.moveTo(move_qinput_x, move_qinput_y)
        pyautogui.click(quest_id_field)
        time.sleep(1)

        pyautogui.write(str(id))
        time.sleep(1)

        try:
            show_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'show.png'), confidence=0.9,  grayscale=True)
            if show_btn:
                pyautogui.click(show_btn)
        except:
            try:
                show_btn_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'showja.png'), confidence=0.9,
                                                       grayscale=True)
                if show_btn_ja:
                    pyautogui.click(show_btn_ja)
            except:
                show_btn_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'showko.png'), confidence=0.9,
                                                       grayscale=True)
                pyautogui.click(show_btn_ko)

        time.sleep(1)


        # Take the first screenshot
        qst_screenshot_1 = pyautogui.screenshot(region=region)
        qst_screenshot_1_path = os.path.join(screenshots_folder, f'{id}_1.jpeg')
        qst_screenshot_1.save(qst_screenshot_1_path, format='JPEG')
        time.sleep(1)

        # Expand the quest window, if no expand button skip
        try:
            expand_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'expandbtn.png'), confidence=0.9,  grayscale=True)
            pyautogui.click(expand_btn)
            time.sleep(1)

            # Take the second screenshot of expanded window
            qst_screenshot_2 = pyautogui.screenshot(region=region)
            qst_screenshot_2_path = os.path.join(screenshots_folder, f'{id}_2.jpeg')
            qst_screenshot_2.save(qst_screenshot_2_path, format='JPEG')
            time.sleep(1)
        except:
            pass

        # Close the first window and open another one
        pyautogui.press('esc')

        move_x = region[0] + int(width * 0.24)
        move_y = region[1] + int(height * 0.21)
        pyautogui.moveTo(move_x, move_y)
        time.sleep(1)

        pyautogui.click(move_x, move_y)
        time.sleep(1)

        try:
            show_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'show.png'), confidence=0.9, grayscale=True)
            if show_btn:
                pyautogui.moveTo(show_btn)
                pyautogui.click(show_btn)
        except:
            try:
                show_btn_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'showja.png'), confidence=0.9,
                                                       grayscale=True)
                if show_btn_ja:
                    pyautogui.moveTo(show_btn_ja)
                    pyautogui.click(show_btn_ja)
            except:
                show_btn_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'showko.png'), confidence=0.9,
                                                       grayscale=True)
                pyautogui.moveTo(show_btn_ko)
                pyautogui.click(show_btn_ko)
        time.sleep(1)

        # Take the third screenshot
        qst_screenshot_3 = pyautogui.screenshot(region=region)
        qst_screenshot_3_path = os.path.join(screenshots_folder, f'{id}_3.jpeg')
        qst_screenshot_3.save(qst_screenshot_3_path, format='JPEG')
        time.sleep(1)

        # Open quest window
        mouse_x, mouse_y = pyautogui.position()
        move_right = mouse_y + 50
        time.sleep(1)

        pyautogui.click(move_right)
        time.sleep(1)

        # Expand the quest window, if no expand button skip
        try:
            expand_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'expandbtn.png'), confidence=0.9,  grayscale=True)
            pyautogui.click(expand_btn)
            time.sleep(1)

            # Take the forth screenshot
            qst_screenshot_4 = pyautogui.screenshot(region=region)
            qst_screenshot_4_path = os.path.join(screenshots_folder, f'{id}_4.jpeg')
            qst_screenshot_4.save(qst_screenshot_4_path, format='JPEG')
            time.sleep(1)
        except:
            # Take the forth screenshot
            qst_screenshot_4 = pyautogui.screenshot(region=region)
            qst_screenshot_4_path = os.path.join(screenshots_folder, f'{id}_4.jpeg')
            qst_screenshot_4.save(qst_screenshot_4_path, format='JPEG')
            time.sleep(1)

        # Close the window
        pyautogui.press('esc')
        time.sleep(1)

        # Clear the input field by holding backspace for 3 seconds
        quest_id_field = pyautogui.moveTo(move_qinput_x, move_qinput_y)
        pyautogui.click(quest_id_field)
        time.sleep(1)

        # Clear the input field by pressing backspace for each character in the ID
        for char in range(len(str(id))):
            pyautogui.press('backspace')
        time.sleep(1)


# # usage
# automate_sherlock_quests()

