import numpy as np
import matplotlib.pyplot as plt
import random

plt.ion()

fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor('#0a0a1a')

def gaussian(x, c, s):
    return np.exp(-((x - c) ** 2) / (2 * s ** 2))

protons = [
    {'center': 1.0, 'vel':  0.045, 'sigma': 0.55, 'color': '#ff6b6b', 'label': 'H¹'},
    {'center': 2.5, 'vel':  0.030, 'sigma': 0.60, 'color': '#ff8c42', 'label': 'H¹'},
    {'center': 7.5, 'vel': -0.030, 'sigma': 0.60, 'color': '#ffb347', 'label': 'H¹'},
    {'center': 9.0, 'vel': -0.045, 'sigma': 0.55, 'color': '#ffd93d', 'label': 'H¹'},
]


helium  = {'center': 5.0, 'vel': -0.02, 'sigma': 0.7, 'color': '#ffe600', 'label': 'He⁴'}
neutron = {'center': 5.0, 'vel':  0.10, 'sigma': 0.2, 'color': '#ffffff', 'label': 'n'}
positron= {'center': 5.0, 'vel': -0.12, 'sigma': 0.2, 'color': '#00ff88', 'label': 'e⁺'}
neutrino= {'center': 5.0, 'vel':  0.15, 'sigma': 0.15, 'color': '#a78bfa', 'label': 'ν'}

state = {
    'fused': False,
    'fusion_frame': 0,
    'temperature': 5.0,
    'energy': 0.0,
    'attempts': 0,
    'successes': 0,
}

frame = 0
x = np.linspace(0, 10, 800)

try:
    while True:
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 6)
        ax.set_facecolor('#0a0a1a')
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color('#333366')
        ax.set_title("☀  Sun Core: Proton-Proton Fusion Chain  ☀",
                     color='white', fontsize=16, pad=15, fontweight='bold')

     
    
        if not state['fused']:
            for p in protons:
                p['center'] += p['vel']
                p['sigma'] = max(0.32, p['sigma'] - 0.003)

            # Average distance from center (5.0)
            avg_dist = np.mean([abs(p['center'] - 5.0) for p in protons])
            state['temperature'] = max(5.0, 100.0 - avg_dist * 12)

            # Draw each proton cloud
            for p in protons:
                cloud = gaussian(x, p['center'], p['sigma'])
                ax.fill_between(x, cloud * 3.0, alpha=0.35,
                                color=p['color'], label=p['label'])
                ax.plot(p['center'], 0, 'o', color=p['color'],
                        markersize=14, markeredgecolor='white',
                        markeredgewidth=1.5)

            # Draw overlap of all protons (fusion zone)
            all_clouds = np.array([gaussian(x, p['center'], p['sigma'])
                                   for p in protons])
            overlap = np.min(all_clouds, axis=0)
            ax.fill_between(x, overlap * 3.5, alpha=0.85,
                            color='#ffcc00', label='Fusion Zone')

            overlap_area = np.trapezoid(overlap, x)
            prob = min(overlap_area * 3, 1.0)

            if prob > 0.35:
                state['attempts'] += 1
                if random.random() < prob * 0.10:
                    state['fused'] = True
                    state['fusion_frame'] = frame
                    state['successes'] += 1
                    state['energy'] = 26.73  # MeV (p-p chain total)
                    # Products start at center
                    helium['center'] = 5.0
                    neutron['center'] = 5.0
                    positron['center'] = 5.0
                    neutrino['center'] = 5.0

       
        else:
            helium['center'] += helium['vel']
            neutron['center'] += neutron['vel']
            positron['center'] += positron['vel']
            neutrino['center'] += neutrino['vel']

            he_cloud = gaussian(x, helium['center'], helium['sigma'])
            n_cloud  = gaussian(x, neutron['center'], neutron['sigma'])
            p_cloud  = gaussian(x, positron['center'], positron['sigma'])
            nu_cloud = gaussian(x, neutrino['center'], neutrino['sigma'])

            ax.fill_between(x, he_cloud * 3.5, alpha=0.55,
                            color=helium['color'], label='He⁴ (alpha)')
            ax.fill_between(x, n_cloud * 2.5, alpha=0.7,
                            color=neutron['color'], label='Neutron')
            ax.fill_between(x, p_cloud * 2.0, alpha=0.6,
                            color=positron['color'], label='Positron e⁺')
            ax.fill_between(x, nu_cloud * 1.8, alpha=0.6,
                            color=neutrino['color'], label='Neutrino ν')

            ax.plot(helium['center'], 0, 'o', color=helium['color'],
                    markersize=22, markeredgecolor='white', markeredgewidth=2)
            ax.plot(neutron['center'], 0, 'o', color=neutron['color'],
                    markersize=10, markeredgecolor='white', markeredgewidth=1)
            ax.plot(positron['center'], 0, 'o', color=positron['color'],
                    markersize=9, markeredgecolor='white', markeredgewidth=1)
            ax.plot(neutrino['center'], 0, 'o', color=neutrino['color'],
                    markersize=8, markeredgecolor='white', markeredgewidth=1)

            # Energy message
            if frame - state['fusion_frame'] < 70:
                ax.text(5, 5.3,
                        "⚡ 26.73 MeV ENERGY RELEASED  (E=mc²) ⚡",
                        color='#ffcc00', ha='center', fontsize=15,
                        fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.6',
                                  facecolor='#1a1a3a', edgecolor='#ffcc00',
                                  linewidth=2))

                ax.text(5, 4.5,
                        "4 H¹  →  He⁴ + 2e⁺ + 2ν + Energy",
                        color='#a0d8ff', ha='center', fontsize=12,
                        family='monospace')

            # Reset loop
            if helium['center'] < 0 or neutrino['center'] > 10:
                protons[0]['center'] = 1.0; protons[0]['sigma'] = 0.55
                protons[1]['center'] = 2.5; protons[1]['sigma'] = 0.60
                protons[2]['center'] = 7.5; protons[2]['sigma'] = 0.60
                protons[3]['center'] = 9.0; protons[3]['sigma'] = 0.55
                state['fused'] = False
                state['energy'] = 0.0

       
        info = (
            f"Temperature: {state['temperature']:.1f} MK\n"
            f"Attempts: {state['attempts']}\n"
            f"Fusions: {state['successes']}\n"
            f"Quantum Tunneling: {'YES' if state['fused'] else 'pending'}"
        )
        ax.text(0.15, 5.6, info, color='#a0d8ff', fontsize=10,
                family='monospace', verticalalignment='top',
                bbox=dict(boxstyle='round,pad=0.5',
                          facecolor='#12122a', edgecolor='#333366'))

        ax.legend(loc='upper right', facecolor='#0a0a1a',
                  edgecolor='#333366', labelcolor='white',
                  fontsize=9, ncol=2)

        plt.pause(0.03)
        frame += 1

except KeyboardInterrupt:
    print("Simulation stopped.")
    plt.close('all')