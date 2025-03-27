# Description: This script creates a GUI application that allows the user to enter a Pokémon name and view its information and stats.
import tkinter as tk
from tkinter import ttk, messagebox
from poke_api import get_pokemon_info

# Main function
# This function creates the main window and all the GUI components
def main():
    # Create main window
    root = tk.Tk()
    root.title("Pokémon Information Viewer")
    root.resizable(False, False)
    
    # Style configuration
    style = ttk.Style()
    style.configure('TFrame', padding=5)
    style.configure('TLabel', padding=5)
    style.configure('TButton', padding=5)
    
    # Input Frame - Top section
    def create_input_frame():
        frm_input = ttk.Frame(root)
        frm_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
        lbl_name.grid(row=0, column=0, padx=(0, 5))
        
        ent_name = ttk.Entry(frm_input, width=25)
        ent_name.grid(row=0, column=1, padx=5)
        ent_name.focus()
        
        # This function is called when the "Get Info" button is clicked
        def handle_get_info():
            name = ent_name.get().strip()
            if not name:
                messagebox.showerror("Error", "Please enter a Pokémon name")
                return
            
            try:
                poke_info = get_pokemon_info(name)
                if not poke_info:
                    messagebox.showerror("Error", f"Pokémon '{name}' not found")
                    return
                
                update_info_frame(poke_info)
                update_stats_frame(poke_info)
                
            except Exception as e:
                messagebox.showerror("API Error", f"Failed to fetch data: {str(e)}")
        
        btn_get = ttk.Button(frm_input, text="Get Info", command=handle_get_info)
        btn_get.grid(row=0, column=2, padx=(5, 0))
        
        return ent_name
    
    # Info Frame - Left section
    def create_info_frame():
        frm_info = ttk.LabelFrame(root, text="Info", padding=10)
        frm_info.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        # Height
        ttk.Label(frm_info, text="Height:").grid(row=0, column=0, sticky="e", pady=2)
        lbl_height = ttk.Label(frm_info, width=15)
        lbl_height.grid(row=0, column=1, sticky="w", padx=(5, 0), pady=2)
        
        # Weight
        ttk.Label(frm_info, text="Weight:").grid(row=1, column=0, sticky="e", pady=2)
        lbl_weight = ttk.Label(frm_info, width=15)
        lbl_weight.grid(row=1, column=1, sticky="w", padx=(5, 0), pady=2)
        
        # Type (handles 1 or 2 types)
        ttk.Label(frm_info, text="Type:").grid(row=2, column=0, sticky="e", pady=2)
        lbl_type = ttk.Label(frm_info, width=15)
        lbl_type.grid(row=2, column=1, sticky="w", padx=(5, 0), pady=2)
        
        return lbl_height, lbl_weight, lbl_type
    
    # Stats Frame - Right section
    def create_stats_frame():
        frm_stats = ttk.LabelFrame(root, text="Stats", padding=10)
        frm_stats.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        
        stats = [
            ("HP:", 0), ("Attack:", 1), ("Defense:", 2),
            ("Special Attack:", 3), ("Special Defense:", 4), ("Speed:", 5)
        ]
        
        bars = []
        for i, (label, _) in enumerate(stats):
            ttk.Label(frm_stats, text=label).grid(row=i, column=0, sticky="e", pady=2)
            bar = ttk.Progressbar(frm_stats, length=180, maximum=255)
            bar.grid(row=i, column=1, sticky="w", padx=(5, 0), pady=2)
            bars.append(bar)
        
        return bars
    
    # Update functions
    def update_info_frame(poke_info):
        lbl_height.config(text=f"{poke_info['height']} dm")
        lbl_weight.config(text=f"{poke_info['weight']} hg")
        
        types = [t['type']['name'] for t in poke_info['types']]
        lbl_type.config(text=", ".join(types).title())
    
    def update_stats_frame(poke_info):
        for i, bar in enumerate(bars):
            bar['value'] = poke_info['stats'][i]['base_stat']
    
    # Create GUI components
    ent_name = create_input_frame()
    lbl_height, lbl_weight, lbl_type = create_info_frame()
    bars = create_stats_frame()
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()