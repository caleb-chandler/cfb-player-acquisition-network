"""
Script to generate graphics for the CFB Network Analysis blog post
"""
import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

def create_portal_growth_chart():
    """Create bar chart showing transfer portal growth 2021-2025"""
    years = ['2021', '2022', '2023', '2024', '2025']
    nodes = [264, 282, 283, 352, 410]
    edges = [958, 1225, 1413, 2340, 3296]

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(years))
    width = 0.35

    bars1 = ax.bar(x - width/2, nodes, width, label='Schools Participating', color='#3498db')
    bars2 = ax.bar(x + width/2, [e/10 for e in edges], width, label='Transfers (÷10)', color='#e74c3c')

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Transfer Portal Growth (2021-2025)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend()

    # Add value labels on bars
    for bar, val in zip(bars1, nodes):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, str(val),
                ha='center', va='bottom', fontsize=10)
    for bar, val in zip(bars2, edges):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, str(val),
                ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig('C:/Users/User/website/caleb-chandler.github.io/assets/imgs/cfb/portal_growth.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print('Saved: portal_growth.png')
    plt.close()


def create_hub_schools_table():
    """Create visual table of top transfer portal hub schools"""
    # Data from degree_analysis files - top net positive schools aggregated
    schools = [
        ('Virginia', 14, 29, 15, '+435'),
        ('Colorado', 15, 47, 32, '+390'),
        ('UCLA', 13, 22, 9, '+416'),
        ('Louisville', 12, 26, 14, '+379'),
        ('Memphis', 23, 33, 10, '+364'),
        ('Auburn', 6, 20, 14, '+350'),
        ('Oregon', -3, 24, 27, '+347'),
        ('Ole Miss', 4, 26, 22, '+350'),
        ('Kansas', 11, 22, 11, '+339'),
        ('Arizona State', 8, 24, 16, '+330'),
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')

    # Create table
    columns = ['School', 'Net Transfers', 'Players In', 'Players Out', 'NPV (2025)']
    table_data = [[s[0], f"+{s[1]}" if s[1] > 0 else str(s[1]), str(s[2]), str(s[3]), s[4]] for s in schools]

    table = ax.table(cellText=table_data, colLabels=columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8)

    # Style header
    for i in range(len(columns)):
        table[(0, i)].set_facecolor('#3498db')
        table[(0, i)].set_text_props(color='white', fontweight='bold')

    # Alternate row colors
    for i in range(1, len(schools) + 1):
        for j in range(len(columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#f0f0f0')

    plt.title('Top 10 Transfer Portal Winners (by Net Portal Value)', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('C:/Users/User/website/caleb-chandler.github.io/assets/imgs/cfb/hub_schools.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print('Saved: hub_schools.png')
    plt.close()


if __name__ == '__main__':
    create_portal_growth_chart()
    create_hub_schools_table()
    print('All graphics created successfully!')
