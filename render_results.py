

import pandas as pd

import matplotlib.pyplot as plt
import data from data

def plot_conflict_data(data):
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    # Convert week column to datetime using the first date of the range
    df['week'] = pd.to_datetime(df['week'].str.split(' to').str[0])
    
    # Create a figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle('Conflict Analysis Over Time')
    
    # Plot attacks
    ax1.plot(df['week'], df['hezbollah_attacks'], 'r-', label='Hezbollah Attacks')
    ax1.plot(df['week'], df['israeli_airstrikes'], 'b-', label='Israeli Airstrikes')
    ax1.set_ylabel('Number of Attacks')
    ax1.legend()
    ax1.grid(True)
    
    # Plot casualties
    ax2.plot(df['week'], df['hezbollah_casualties'], 'r--', label='Hezbollah Casualties')
    ax2.plot(df['week'], df['israeli_casualties'], 'b--', label='Israeli Casualties')
    ax2.set_ylabel('Number of Casualties')
    ax2.set_xlabel('Week')
    ax2.legend()
    ax2.grid(True)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label overlap
    plt.tight_layout()
    
    return fig

# Example usage:
# fig = plot_conflict_data(data)
# plt.show()


def main():
  fig = plot_conflict_data(data)
  fig.show()

if __name__ == "__main__":
    main()















