import pandas as pd
import matplotlib.pyplot as plt
from missles import data  # Import data from data.py

def plot_conflict_data(data):
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    # Convert week column to datetime using the first date of the range
    df['week'] = pd.to_datetime(df['week'].str.split(' to').str[0])
    
    # Create a figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle('Conflict Analysis Over Time')
    
    # Plot attacks on first subplot with two y-axes
    color1, color2 = '#d62728', '#1f77b4'  # Red and Blue
    
    # Primary y-axis (Hezbollah Missiles)
    ln1 = ax1.plot(df['week'], df['hezbollah_missiles_fired'], 
                   color=color1, label='Hezbollah Missiles Fired')
    ax1.set_ylabel('Hezbollah Missiles Fired', color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    
    # Secondary y-axis (Israeli Airstrikes)
    ax1_twin = ax1.twinx()
    ln2 = ax1_twin.plot(df['week'], df['israeli_airstrikes'], 
                       color=color2, label='Israeli Airstrikes')
    ax1_twin.set_ylabel('Israeli Airstrikes', color=color2)
    ax1_twin.tick_params(axis='y', labelcolor=color2)
    
    # Add legends for first subplot
    lns = ln1 + ln2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc='upper left')
    
    # Plot casualties on second subplot
    ax2.plot(df['week'], df['hezbollah_casualties'], 
            color=color1, linestyle='--', label='Hezbollah Casualties')
    ax2.plot(df['week'], df['israeli_casualties'], 
            color=color2, linestyle='--', label='Israeli Casualties')
    ax2.set_ylabel('Number of Casualties')
    ax2.set_xlabel('Week')
    ax2.legend()
    ax2.grid(True)
    
    # Format x-axis dates on both subplots
    for ax in [ax1, ax2]:
        ax.grid(True)
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    # Adjust layout to prevent label overlap
    plt.tight_layout()
    
    return fig

def main():
    fig = plot_conflict_data(data)
    plt.show()

if __name__ == "__main__":
    main()