# Replication data for "Adaptive link dynamics drive online hate networks and their mainstream influence"

Data to accompany the following paper: [DOI PENDING]

## Legal

Per Section 3(a)(1) of the CC BY 4.0 License, you *must* include the following with any shared (modified or unmodified) version of the contents of this folder:

- Identification of creators: Richard Sear, Minzhang Zheng, Neil Johnson
- URL to this dataset: https://github.com/gwdonlab/data-access/tree/main/npj-complexity-adaptive-link-dynamics
- Indication of any modifications you made and, if so, what you changed
- Copyright notice, notice of disclaimer of warranties, a notice indicating that the contents of this folder is licensed under the CC BY 4.0 License, and a notice referring to the CC BY 4.0 License (https://creativecommons.org/licenses/by/4.0/legalcode.en)

## Instructions

To use the data, load the edge and node lists into Gephi (FOSS available here: https://gephi.org/). Nodes are scaled by degree, 5-200. The graph shape is generated using the ForceAtlas 2 layout with the following parameters (if not mentioned, leave unchecked):
- Speed: 10.0
- Approximate Repulsion
- Approximation: 1.2
- Scaling: 10.0
- Stronger Gravity
- Gravity: 1.0
- Edge Weight Influence: 1.0

The image is generated after ForceAtlas 2 stabilizes using the following parameters (if not mentioned, leave unchecked):
- Node border color: darker
- Node opacity: 30.0
- Show edges
- Edge thickness: 0.001
- Edge rescale weight
- Edge min. rescaled weight: 1E-8
- Edge nax. rescaled weight: 1E-5
- Edge color: source
- Edge opacity: 10.0
- Edge curves
- Edge radius: 0.0
- Edge arrows size: 3.0

Use the boolean columns in the nodelist as appropriate to find or annotate the nodes highlighted in Supplementary Figures.