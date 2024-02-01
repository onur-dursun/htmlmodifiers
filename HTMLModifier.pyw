import tkinter as tk
from tkinter import filedialog

def generate_output():
    # Get input values from text boxes
    title = entry_entries["Title"].get()
    subtitle = entry_entries["Subtitle"].get()
    price = entry_entries["Price"].get()
    portfolio_link = entry_entries["Portfolio Link"].get()
    sales_link = entry_entries["Sales Link"].get()
    background_url = entry_entries["Background URL"].get()

    # Process the input (modify as needed)
    output_text = """<a class="wpb_wrapper" href=\"""" + portfolio_link + """\">
    <div class="pricing-table active MinimalStyle kd-animated fadeInUp highlight-box kd-animate" style="background-image: url(""" + background_url + """) !important;" data-animation-delay="200">
        <div class="row pricing-title">
            <h5 class="pricing-title-content" style="color: #ffffff;">""" +title + """</h5>
        </div>
        <div class="row pricing">
            <div class="col-lg-3 col-md-3 col-sm-3">
                <div class="row">
                    <span class="pricing-price default-plan sale-no" style="color: #ffffff;">
                        <span class="pt-normal-price"> <span class="currency">$</span>""" + price + """</span>
                    </span>
                </div>
                <span class="pricing-subtitle" style="color: #ffffff;">""" + subtitle + """</span>
            </div>
            <div style="height: 100px; width: 100%; clear: both;"></div>
            <a href=\"""" + sales_link + """\" target="_blank" class="tt_button icon_right tt_primary_button btn_primary_color hover_solid_white">
                <span class="prim_text">Purchase Now</span><i class="fas fa-level-up-alt iconita" style="font-size: 13px;"></i>
            </a>
            <div style="height: 50px; width: 100%; clear: both;"></div>
        </div>
    </div>
</a>"""
    
    # Update the output text box
    output_box.config(state=tk.NORMAL)  # Enable editing
    output_box.delete(1.0, tk.END)  # Clear previous content
    output_box.insert(tk.END, output_text)  # Insert new content
    output_box.config(state=tk.DISABLED)  # Disable editing
    save_content()

# Create the main window
root = tk.Tk()
root.title("HTML Modifier")

# Create and place text boxes
labels = ["Title", "Subtitle", "Price", "Portfolio Link", "Sales Link", "Background URL"]
entry_entries = {}

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=f"{label_text}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    
    entry_entries[label_text] = entry

# Create and place the button
generate_button = tk.Button(root, text="Generate Output", command=generate_output)
generate_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def save_content():
    # Get content from text boxes
    content = {}
    for label_text, entry_widget in entry_entries.items():
        content[label_text] = entry_widget.get()

    # Open a file dialog for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        with open(file_path, 'w') as file:
            for label_text, value in content.items():
                file.write(f"{label_text}: {value}\n")

def load_content():
    # Open a file dialog for loading
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()

        # Update the text boxes with loaded content
        for label_text, entry_widget in entry_entries.items():
            start_index = content.find(f"{label_text}: ") + len(label_text) + 2
            end_index = content.find("\n", start_index)
            entry_widget.delete(0, tk.END)
            entry_widget.insert(tk.END, content[start_index:end_index])

# Create and place the buttons
generate_button = tk.Button(root, text="Generate Output", command=generate_output)
generate_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

save_button = tk.Button(root, text="Save", command=save_content)
save_button.grid(row=len(labels) + 1, column=0, pady=5)

load_button = tk.Button(root, text="Load", command=load_content)
load_button.grid(row=len(labels) + 1, column=1, pady=5)

# Create and place the output text box
output_box = tk.Text(root, height=10, width=30, state=tk.DISABLED)
output_box.grid(row=len(labels)+2, column=0, columnspan=2, padx=10, pady=5)


# Start the GUI event loop
root.mainloop()
