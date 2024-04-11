from Event import Event
import tkinter as tk
from CalendarObject import CalendarObject
import main_menu


def main():
    # main while loop to reprompt for user input
    # Carter

    #Setting up main frame
    root_GUI = tk.Tk()
    root_GUI.title("Calendar")
    root_GUI.geometry("1200x800")

    # primary background that everything is set on
    main_frame = tk.Frame(root_GUI, bg = 'black')
    main_frame.pack(fill = 'both', expand = True)

     # Two column layout
    main_frame.columnconfigure(0, weight=1)  # For the left portion
    main_frame.columnconfigure(1, weight=1)  # For the right portion
    main_frame.rowconfigure(0, weight=1)

    event_text_frame = tk.LabelFrame(main_frame, bg = 'black', fg = 'white', highlightthickness = 0, font = ("Arial", 12))
    event_text_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky='nsew')

    calendar_visual = CalendarObject(event_text_frame)
    
    buttons_frame = tk.LabelFrame(main_frame, text = "Options", bg = 'lightblue')
    buttons_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')

    # called through the button only to reenable the button once adding to events is finished
    def add_event_and_enable_button():
        main_menu.gui_add_events(buttons_frame, calendar_visual, add_event_button) 
    
    add_event_button = tk.Button(buttons_frame, text = 'Add Event', command = lambda: [add_event_button.config(state = 'disabled'), add_event_and_enable_button()])
    add_event_button.pack()

    root_GUI.mainloop()


if __name__ == "__main__":
    main()
