##################################################
#          Name:- Aaditya Sakhardande            #
#          ASU ID:- 1233720594                   #
#          Email:- asakhar3@asu.edu              #
#          Date:- 01/29/2025                     #
##################################################
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt

# Constants
MAX_YEARS = 70
SIMULATIONS = 10

# Field Labels
FIELDS = {
    'Mean Return (%)': 'mean_return',
    'Standard Deviation (%)': 'std_dev',
    'Annual Contribution ($)': 'annual_contrib',
    'Years of Contribution': 'contrib_years',
    'Years to Retirement': 'retirement_years',
    'Annual Spending in Retirement ($)': 'annual_spending',
    'Wealth at Retirement': 'retirement_wealth'
}

# Button Labels
EXIT_BUTTON = 'Exit'
CALCULATE_BUTTON = 'Calculate'

def simulate_wealth(window, user_inputs):
    try:
        r = float(user_inputs[FIELDS['Mean Return (%)']]) / 100
        sigma = float(user_inputs[FIELDS['Standard Deviation (%)']]) / 100
        contribution = float(user_inputs[FIELDS['Annual Contribution ($)']])
        spending = float(user_inputs[FIELDS['Annual Spending in Retirement ($)']])
        years_contributing = int(float(user_inputs[FIELDS['Years of Contribution']]))
        years_to_retirement = int(float(user_inputs[FIELDS['Years to Retirement']]))
    except ValueError:
        sg.popup_error("Please enter valid numeric values.")
        return

    if years_contributing > years_to_retirement:
        sg.popup_error("Years of contribution cannot exceed years to retirement.")
        return

    wealth_data = np.zeros((MAX_YEARS, SIMULATIONS))

    plt.figure()
    for sim in range(SIMULATIONS):
        wealth = [0.0]  
        noise = sigma * np.random.randn(MAX_YEARS)

        for year in range(MAX_YEARS):
            current_wealth = wealth[-1]

            if year < years_contributing:
                current_wealth = current_wealth * (1 + r + noise[year]) + contribution
            elif year < years_to_retirement:
                current_wealth = current_wealth * (1 + r + noise[year])
            else:
                current_wealth = current_wealth * (1 + r + noise[year]) - spending

            current_wealth = max(0, current_wealth)  
            wealth.append(current_wealth)

            if current_wealth == 0:
                break

        wealth = wealth[:MAX_YEARS + 1] + [0] * (MAX_YEARS + 1 - len(wealth))
        wealth_data[:, sim] = wealth[:MAX_YEARS]

        plt.plot(range(len(wealth)), wealth, label=f'Simulation {sim + 1}')

    avg_wealth_at_retirement = np.mean(wealth_data[years_to_retirement, :]) if years_to_retirement < MAX_YEARS else 0
    window[FIELDS['Wealth at Retirement']].update(f"Estimated Wealth at Retirement: ${avg_wealth_at_retirement:,.2f}")

    plt.title("Projected Wealth Over Time")
    plt.xlabel("Years")
    plt.ylabel("Wealth ($)")
    plt.grid(True)
    plt.legend()
    plt.show(block=False)

# GUI Layout
sg.theme("DarkBlue3")
layout = [[sg.Text(label, size=(25, 1)), sg.Input(key=key, size=(20, 1))] for label, key in FIELDS.items() if key != 'retirement_wealth'] + [
    [sg.Text("", key=FIELDS['Wealth at Retirement'], size=(40, 1))],
    [sg.Button(EXIT_BUTTON), sg.Button(CALCULATE_BUTTON)]
]

# Create Window
window = sg.Window("Retirement Wealth Simulator", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, EXIT_BUTTON):
        break
    if event == CALCULATE_BUTTON:
        simulate_wealth(window, values)

window.close()
