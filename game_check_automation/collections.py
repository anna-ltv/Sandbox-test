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


def clean_cl_ids(ids):
    cleaned_ids = []
    for i in ids:
        if pd.isna(i):
            continue  # Skip NaN values
        # Remove 'COL_' prefix and '_NAME' suffix
        cleaned_id = str(i).replace('COL_', '').replace('_NAME', '')
        cleaned_ids.append(cleaned_id)
    return cleaned_ids


def automate_collections():
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
    ids = ids_df['Collection ID'].dropna().astype(str).tolist()
    # Clean IDs
    cleaned_ids = clean_cl_ids(ids)

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
    if profile:
        pyautogui.moveTo(profile)
        pyautogui.mouseDown()
        time.sleep(3)
        pyautogui.mouseUp()
    else:
        print("Profile button not found.")

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

    # Open coin crystals menu
    try:
        coins_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'coin.png'), confidence=0.9,  grayscale=True)
        if coins_btn:
            pyautogui.click(coins_btn)
    except:
        try:
            coins_btn_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'coinja.png'), confidence=0.9, grayscale=True)
            if coins_btn_ja:
                pyautogui.click(coins_btn_ja)
        except:
            coins_btn_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'coinko.png'), confidence=0.9,
                                                    grayscale=True)
            pyautogui.click(coins_btn_ko)

    time.sleep(1)

    # Add Crystals
    move_crystals_x = region[0] + int(width * 0.3)
    move_crystals_y = region[1] + int(height * 0.25)
    crystals_field = pyautogui.moveTo(move_crystals_x, move_crystals_y)
    pyautogui.vscroll(-5)
    pyautogui.click(crystals_field)
    time.sleep(1)

    # button UP
    move_up_x = region[0] + int(width * 0.42)
    move_up_y = region[1] + int(height * 0.2)
    up_btn = pyautogui.moveTo(move_up_x, move_up_y)
    pyautogui.click(up_btn)
    time.sleep(1)

    # Save button click
    try:
        save_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'save.png'), confidence=0.9,  grayscale=True)
        if save_btn:
            pyautogui.click(save_btn)
    except:
        try:
            save_btn_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'saveja.png'), confidence=0.9, grayscale=True)
            if save_btn_ja:
                pyautogui.click(save_btn_ja)
        except:
            save_btn_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'saveko.png'), confidence=0.9,
                                                    grayscale=True)
            pyautogui.click(save_btn_ko)

    time.sleep(1)

    # Step 3: Press Show UI Cheats
    try:
        show_ui_cheats = pyautogui.locateOnScreen(os.path.join(images_dir, 'showui.png'), confidence=0.9,  grayscale=True)
        if show_ui_cheats:
            pyautogui.click(show_ui_cheats)
    except:
        try:
            show_ui_cheats_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'showuija.png'), confidence=0.9, grayscale=True)
            if show_ui_cheats_ja:
                pyautogui.click(show_ui_cheats_ja)
        except:
            show_ui_cheats_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'showuiko.png'), confidence=0.9,
                                                    grayscale=True)
            pyautogui.click(show_ui_cheats_ko)

    time.sleep(1)

    # Close the cheats menu
    pyautogui.press('esc')
    time.sleep(1)

    # Loop to enter collection IDs and perform actions
    for id in cleaned_ids:
        # Open collections
        open_collections = pyautogui.locateOnScreen(os.path.join(images_dir, 'collections.png'), confidence=0.9,  grayscale=True)
        pyautogui.click(open_collections)

        time.sleep(1)

        # Step 4: Enter the ID and perform actions
        cl_input_field = pyautogui.locateOnScreen(os.path.join(images_dir, 'colfield.png'), confidence=0.9,  grayscale=True)
        pyautogui.click(cl_input_field)

        time.sleep(1)

        pyautogui.write(str(id))
        time.sleep(1)

        # Press Find button
        try:
            find_col_btn = pyautogui.locateOnScreen(os.path.join(images_dir, 'findcol.png'), confidence=0.9,  grayscale=True)
            if find_col_btn:
                pyautogui.click(find_col_btn)
        except:
            try:
                find_col_btn_ja = pyautogui.locateOnScreen(os.path.join(images_dir, 'findcolja.png'), confidence=0.9,
                                                             grayscale=True)
                if find_col_btn_ja:
                    pyautogui.click(find_col_btn_ja)
            except:
                find_col_btn_ko = pyautogui.locateOnScreen(os.path.join(images_dir, 'findcolko.png'), confidence=0.9,
                                                             grayscale=True)
                pyautogui.click(find_col_btn_ko)

        time.sleep(1)

        # Take the first screenshot
        screenshot_1 = pyautogui.screenshot(region=region)
        screenshot_1_path = os.path.join(screenshots_folder, f'{id}_1.jpeg')
        screenshot_1.save(screenshot_1_path, format='JPEG')
        time.sleep(1)

        # Coordinates for moving and clicking items
        x_offsets = [0.085, 0.21, 0.34, 0.47, 0.6]
        y_offset = 0.43
        add_x_offsets = [0.125, 0.25, 0.38, 0.51, 0.64]
        add_y_offset = 0.49

        # Loop over each item
        for i in range(5):
            # Move and click the item
            move_x = region[0] + int(width * x_offsets[i])
            move_y = region[1] + int(height * y_offset)
            pyautogui.moveTo(move_x, move_y)
            pyautogui.click()
            time.sleep(1)

            # Take screenshot
            screenshot = pyautogui.screenshot(region=region)
            screenshot_path = os.path.join(screenshots_folder, f'{id}_{i + 2}.jpeg')
            screenshot.save(screenshot_path, format='JPEG')
            time.sleep(1)

            # Press Esc
            pyautogui.press('esc')
            time.sleep(1)

            # Click Add button
            add_x = region[0] + int(width * add_x_offsets[i])
            add_y = region[1] + int(height * add_y_offset)
            pyautogui.moveTo(add_x, add_y)
            pyautogui.click()

        # Move to the last item
        move_x6 = region[0] + int(width * 0.86)
        move_y6 = region[1] + int(height * 0.43)
        last_col_item = pyautogui.moveTo(move_x6, move_y6)
        pyautogui.click(last_col_item)
        time.sleep(1)

        screenshot_7 = pyautogui.screenshot(region=region)
        screenshot_7_path = os.path.join(screenshots_folder, f'{id}_7.jpeg')
        screenshot_7.save(screenshot_7_path, format='JPEG')
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)

        # Collect assemblers
        move_assem_x = region[0] + int(width * 0.76)
        move_assem_y = region[1] + int(height * 0.49)
        opn_assemblers = pyautogui.moveTo(move_assem_x, move_assem_y)
        pyautogui.click(opn_assemblers)
        time.sleep(1)

        move_buy_x = region[0] + int(width * 0.51)
        move_buy_y = region[1] + int(height * 0.83)
        buy_assemblers = pyautogui.moveTo(move_buy_x, move_buy_y)
        pyautogui.click(buy_assemblers)
        time.sleep(1)

        # Assemble collection
        move_collect_x = region[0] + int(width * 0.89)
        move_collect_y = region[1] + int(height * 0.54)
        collect_col = pyautogui.moveTo(move_collect_x, move_collect_y)
        pyautogui.click(collect_col)
        time.sleep(2)

        screenshot_8 = pyautogui.screenshot(region=region)
        screenshot_8_path = os.path.join(screenshots_folder, f'{id}_8.jpeg')
        screenshot_8.save(screenshot_8_path, format='JPEG')
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)


# # usage
# automate_sherlock_collections()

