<!-- markdownlint-disable -->

<h1 align="center">
    Popular Open Source Libraries for Power System Analysis
    <br>
</h1>

<p align="center">
    <strong>🏆  A ranked list of popular projects for Power System Analysis. Updated weekly.</strong>
</p>

<p align="center">
    <a href="https://best-of.org" title="Best-of Badge"><img src="http://bit.ly/3o3EHNN"></a>
    <a href="https://doi.org/10.5281/zenodo.14941137"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.14941137.svg" alt="DOI"></a>
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-140-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <a href="https://github.com/jinningwang/best-of-ps/releases" title="Best-of Updates"><img src="https://img.shields.io/github/release-date/jinningwang/best-of-ps?color=green&label=updated"></a>
    <a href="https://github.com/jinningwang/best-of-ps/graphs/traffic" title="Visits Badge"><img src="https://badges.strrl.dev/visits/jinningwang/best-of-ps"></a>
</p>

This curated list contains 140 open-source projects with a total of 71K stars grouped into 15 categories. All projects are ranked by a project-popularity score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/jinningwang/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/jinningwang/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Phasor Simulation](#phasor-simulation) _14 projects_
- [EMT Simulation](#emt-simulation) _2 projects_
- [Steady State Simulation](#steady-state-simulation) _37 projects_
- [Interface](#interface) _20 projects_
- [Gas Simulation](#gas-simulation) _3 projects_
- [Co-Simulation Environment](#co-simulation-environment) _2 projects_
- [Optimization Modeling Language](#optimization-modeling-language) _8 projects_
- [Optimizer](#optimizer) _17 projects_
- [Machine/Reinforcement Learning for Power Grid](#machinereinforcement-learning-for-power-grid) _4 projects_
- [Visualization](#visualization) _3 projects_
- [Messaging Environment](#messaging-environment) _2 projects_
- [Power System Data](#power-system-data) _19 projects_
- [Power Electronics](#power-electronics) _1 projects_
- [Database Management](#database-management) _2 projects_
- [Textbook](#textbook) _9 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(12 months no activity)_
- 💀&nbsp; Dead project _(1200 months no activity)_
- 📈📉&nbsp; Project is trending up or down
- ➕&nbsp; Project was recently added
- ❗️&nbsp; Warning _(e.g. missing/risky license)_
- 👨‍💻&nbsp; Contributors count from GitHub
- 🔀&nbsp; Fork count from GitHub
- 📋&nbsp; Issue count from GitHub
- ⏱️&nbsp; Last update timestamp on package manager
- 📥&nbsp; Download count from package manager
- 📦&nbsp; Number of dependent projects
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13">&nbsp; Support Python
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13">&nbsp; Support Julia
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13">&nbsp; Support Octave
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13">&nbsp; Support Java
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13">&nbsp; Support C
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/cpp.ico" style="display:inline;" width="13" height="13">&nbsp; Support C++
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/modelica.ico" style="display:inline;" width="13" height="13">&nbsp; Support Modelica
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/rust.ico" style="display:inline;" width="13" height="13">&nbsp; Support Rust
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/r.ico" style="display:inline;" width="13" height="13">&nbsp; Support R
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13">&nbsp; Shipped with Jupyter Notebook examples
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13">&nbsp; CI via GitHub Actions
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/azure.ico" style="display:inline;" width="13" height="13">&nbsp; CI via Azure Pipelines
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13">&nbsp; Available on PyPI
- <img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13">&nbsp; Available on Conda

<br>

## Phasor Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://ltb.curent.org/">LTB ANDES</a></b> (🥇22 ·  ⭐ 260) - Transient Stability Simulator; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/azure.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/andes) (👨‍💻 24 · 🔀 120 · 📦 28 · 📋 76 - 17% open · ⏱️ 18.04.2025):

	```
	git clone https://github.com/CURENT/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 3.2K / month · 📦 4 · ⏱️ 05.01.2025):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/conda-forge/andes) (📥 610K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge andes
	```
- [Docker Hub](https://hub.docker.com/r/CURENT/andes):
	```
	docker pull CURENT/andes
	```
</details>
<details><summary><b><a href="http://dynawo.org">Dynaωo</a></b> (🥇22 ·  ⭐ 83) - C++/Modelica simulation tools for power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dynawo/dynawo) (👨‍💻 57 · 🔀 25 · 📥 18K · 📋 1.5K - 8% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/dynawo/dynawo
	```
</details>
<details><summary><b><a href="https://www.gridlabd.org/">GridLAB-D</a></b> (🥈20 ·  ⭐ 170 · 💤) - Distribution power system simulator. <code><a href="https://github.com/gridlab-d/gridlab-d/blob/master/LICENSE">❗️Custom</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridlab-d/gridlab-d) (👨‍💻 75 · 🔀 110 · 📥 6.3K · 📋 1.3K - 24% open · ⏱️ 22.02.2024):

	```
	git clone https://github.com/gridlab-d/gridlab-d
	```
</details>
<details><summary><b><a href="https://github.com/OpenIPSL/OpenIPSL">OpenIPSL</a></b> (🥈16 ·  ⭐ 91) - A library of power system component models written in the.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenIPSL/OpenIPSL) (👨‍💻 35 · 🔀 55 · 📥 500 · 📋 120 - 12% open · ⏱️ 07.04.2025):

	```
	git clone https://github.com/OpenIPSL/OpenIPSL
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSimulationsDynamics.jl</a></b> (🥈15 ·  ⭐ 200) - Dynamic Power System simulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl) (👨‍💻 15 · 🔀 47 · 📋 140 - 33% open · ⏱️ 21.10.2024):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl
	```
</details>
<details><summary><b><a href="https://github.com/changgang/steps">STEPS</a></b> (🥈14 ·  ⭐ 52 · 💤) - Balanced large-scale AC-DC hybrid power system analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/changgang/steps) (👨‍💻 4 · 🔀 19 · 📥 48 · 📦 7 · 📋 3 - 33% open · ⏱️ 24.03.2024):

	```
	git clone https://github.com/changgang/steps
	```
- [PyPi](https://pypi.org/project/stepspy) (📥 1.4K / month · ⏱️ 22.09.2024):
	```
	pip install stepspy
	```
</details>
<details><summary><b><a href="https://gridpack.pnnl.gov/wiki/index.php/Main_Page">GridPACK</a></b> (🥈14 ·  ⭐ 50) - High-Performance Electric Grid Simulation. <code><a href="https://github.com/GridOPTICS/GridPACK/blob/develop/docs/markdown/LICENSE.md">❗️Custom</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridOPTICS/GridPACK) (👨‍💻 52 · 🔀 21 · 📥 620 · 📋 140 - 23% open · ⏱️ 26.03.2025):

	```
	git clone https://github.com/GridOPTICS/GridPACK
	```
</details>
<details><summary><b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥉13 ·  ⭐ 71) - Modelica 3rd party library for electrical power systems. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/modelica-3rdparty/PowerSystems) (👨‍💻 10 · 🔀 37 · 📋 41 - 34% open · ⏱️ 07.05.2024):

	```
	git clone https://github.com/modelica-3rdparty/PowerSystems
	```
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER</a></b> (🥉13 ·  ⭐ 61) - Inverter-based DER simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER) (👨‍💻 2 · 🔀 24 · 📦 3 · ⏱️ 15.04.2025):

	```
	git clone https://github.com/epri-dev/OpenDER
	```
- [PyPi](https://pypi.org/project/opender) (📥 1.4K / month · ⏱️ 13.04.2025):
	```
	pip install opender
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/powersas.m">PowerSAS.m</a></b> (🥉7 ·  ⭐ 20 · 💤) - Power grid analysis framework based on semi-analytical.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/powersas.m) (👨‍💻 4 · 🔀 5 · ⏱️ 05.01.2024):

	```
	git clone https://github.com/ANL-CEEESA/powersas.m
	```
</details>
<details><summary><b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉6 ·  ⭐ 8 · 💤) - EMT-TS hybrid simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenHybridSim/OpenHybridSim-code) (🔀 4 · ⏱️ 05.05.2020):

	```
	git clone https://github.com/OpenHybridSim/OpenHybridSim-code
	```
</details>
<details><summary><b><a href="http://faraday1.ucd.ie/psat.html">PSAT</a></b> (🥉4 ·  ⭐ 12 · 💤) - Power System Analysis Toolbox by Federico Milano. <code><a href="https://tldrlegal.com/search?q=GPL">❗️GPL</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sinan81/PSAT) (👨‍💻 2 · 🔀 7 · 📥 120 · ⏱️ 23.06.2020):

	```
	git clone https://github.com/Sinan81/PSAT
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/gensas">GenSAS</a></b> (🥉4 ·  ⭐ 1) - A C++ based generalized simulation tool based on semi-analytical.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/gensas) (👨‍💻 3 · 🔀 1 · ⏱️ 04.03.2025):

	```
	git clone https://github.com/ANL-CEEESA/gensas
	```
</details>
<details><summary><b><a href="https://sites.ecse.rpi.edu/~chowj/">PST</a></b> (🥉3 ·  ⭐ 5 · 💤) - Power System Toolbox from Dr. Joe H. Chow. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/pst) (🔀 1 · ⏱️ 11.04.2020):

	```
	git clone https://github.com/cuihantao/pst
	```
</details>
<br>

## EMT Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://dpsim.fein-aachen.org/">DPsim</a></b> (🥇22 ·  ⭐ 82) - Simulation for both EMT and phasor. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/dpsim) (👨‍💻 35 · 🔀 60 · 📦 11 · 📋 160 - 53% open · ⏱️ 21.04.2025):

	```
	git clone https://github.com/sogno-platform/dpsim
	```
- [PyPi](https://pypi.org/project/dpsim) (📥 430 / month · ⏱️ 10.12.2022):
	```
	pip install dpsim
	```
</details>
<details><summary><b><a href="https://github.com/NREL/ParaEMT_public">ParaEMT</a></b> (🥉9 ·  ⭐ 69) - Parallel EMT simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/ParaEMT_public) (👨‍💻 4 · 🔀 26 · ⏱️ 03.04.2025):

	```
	git clone https://github.com/NREL/ParaEMT_public
	```
</details>
<br>

## Steady State Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇33 ·  ⭐ 960) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 150 · 🔀 500 · 📦 480 · 📋 1.1K - 19% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📥 51K / month · 📦 62 · ⏱️ 06.03.2025):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/conda-forge/pandapower) (📥 26K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 100 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇32 ·  ⭐ 1.5K) - Python for Power System Analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 97 · 🔀 510 · 📦 280 · 📋 420 - 25% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📥 15K / month · 📦 27 · ⏱️ 07.04.2025):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/conda-forge/pypsa) (📥 130K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge pypsa
	```
</details>
<details><summary><b><a href="https://github.com/PowerGridModel/power-grid-model">Power Grid Model</a></b> (🥇29 ·  ⭐ 170 · 📈) - Steady-state distribution power system analysis. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGridModel/power-grid-model) (👨‍💻 26 · 🔀 35 · 📥 650 · 📦 27 · 📋 220 - 32% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/PowerGridModel/power-grid-model
	```
- [PyPi](https://pypi.org/project/power-grid-model) (📥 110K / month · 📦 6 · ⏱️ 01.05.2025):
	```
	pip install power-grid-model
	```
- [Conda](https://anaconda.org/conda-forge/power-grid-model) (📥 3.3M · ⏱️ 30.04.2025):
	```
	conda install -c conda-forge power-grid-model
	```
</details>
<details><summary><b><a href="https://www.advancedgridinsights.com/gridcal">GridCal</a></b> (🥇27 ·  ⭐ 450) - Cross-platform power systems software. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/GridCal) (👨‍💻 53 · 🔀 100 · 📥 49 · 📦 10 · 📋 240 - 13% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/SanPen/GridCal
	```
- [PyPi](https://pypi.org/project/GridCal) (📥 6.4K / month · ⏱️ 30.04.2025):
	```
	pip install GridCal
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PowSyBl Core</a></b> (🥈24 ·  ⭐ 130) - Framework to build power system software. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-core) (👨‍💻 120 · 🔀 45 · 📦 89 · 📋 650 - 45% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/powsybl/powsybl-core
	```
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥈23 ·  ⭐ 360) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 21 · 🔀 120 · 📦 140 · 📋 45 - 73% open · ⏱️ 10.04.2025):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 19K / month · 📦 16 · ⏱️ 10.04.2025):
	```
	pip install PYPOWER
	```
- [Conda](https://anaconda.org/invenia/pypower) (📥 3.2K · ⏱️ 25.03.2025):
	```
	conda install -c invenia pypower
	```
- [Docker Hub](https://hub.docker.com/r/hwanghust/pypower) (📥 24 · ⏱️ 19.05.2019):
	```
	docker pull hwanghust/pypower
	```
</details>
<details><summary><b><a href="https://matpower.org/">MATPOWER</a></b> (🥈22 ·  ⭐ 460) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 18 · 🔀 160 · 📥 550K · 📋 220 - 10% open · ⏱️ 16.04.2025):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 2.2K · ⏱️ 16.04.2025):
	```
	docker pull matpower/matpower
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">GridPath</a></b> (🥈22 ·  ⭐ 100) - Power system planning and operations. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/blue-marble/gridpath) (👨‍💻 12 · 🔀 41 · 📥 1.3K · 📦 4 · 📋 340 - 22% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/blue-marble/gridpath
	```
- [PyPi](https://pypi.org/project/GridPath) (📥 380 / month · ⏱️ 30.04.2025):
	```
	pip install GridPath
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PyPowSyBl</a></b> (🥈22 ·  ⭐ 64) - A PowSyBl and Python integration. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/pypowsybl) (👨‍💻 33 · 🔀 12 · 📥 280 · 📋 240 - 30% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/powsybl/pypowsybl
	```
- [PyPi](https://pypi.org/project/pypowsybl) (📥 11K / month · 📦 8 · ⏱️ 07.04.2025):
	```
	pip install pypowsybl
	```
</details>
<details><summary><b><a href="https://l2rpn.chalearn.org/">LightSim2Grid</a></b> (🥈22 ·  ⭐ 53) - A fast backend for the Grid2Op. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/lightsim2grid) (👨‍💻 6 · 🔀 11 · 📥 300 · 📦 64 · 📋 55 - 30% open · ⏱️ 28.04.2025):

	```
	git clone https://github.com/BDonnot/lightsim2grid
	```
- [PyPi](https://pypi.org/project/LightSim2Grid) (📥 21K / month · 📦 23 · ⏱️ 28.04.2025):
	```
	pip install LightSim2Grid
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/lightsim2grid) (📥 330 · ⏱️ 01.02.2022):
	```
	docker pull bdonnot/lightsim2grid
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥈21 ·  ⭐ 420) - Sector-Coupled Optimisation Model of the European Energy.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 91 · 🔀 270 · 📋 540 - 27% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur):
	```
	docker pull nimfetrisa/pypsa-eur
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSimulations.jl</a></b> (🥈21 ·  ⭐ 290) - Power Systems optimization simulation and modeling;.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSimulations.jl) (👨‍💻 40 · 🔀 69 · 📋 410 - 18% open · ⏱️ 21.04.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulations.jl
	```
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Earth</a></b> (🥈21 ·  ⭐ 260) - Open optimisation model for study energy system.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-earth) (👨‍💻 77 · 🔀 230 · 📋 500 - 35% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-earth
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥈19 ·  ⭐ 420) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 32 · 🔀 160 · 📋 500 - 18% open · ⏱️ 24.04.2025):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/reopt/">REopt</a></b> (🥈19 ·  ⭐ 100) - Renewable Energy Integration & Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/REopt_API) (👨‍💻 22 · 🔀 56 · 📥 570 · 📋 84 - 52% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/NREL/REopt_API
	```
</details>
<details><summary><b><a href="https://energy.mit.edu/genx/">GenX</a></b> (🥉18 ·  ⭐ 300) - Configurable capacity expansion model. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GenXProject/GenX.jl) (👨‍💻 35 · 🔀 120 · 📋 300 - 18% open · ⏱️ 05.02.2025):

	```
	git clone https://github.com/GenXProject/GenX
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-USA</a></b> (🥉18 ·  ⭐ 82) - Power System Model for the United States. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-usa) (👨‍💻 12 · 🔀 28 · 📋 320 - 27% open · ⏱️ 26.04.2025):

	```
	git clone https://github.com/PyPSA/pypsa-usa
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AMS</a></b> (🥉17 ·  ⭐ 13 · 📈) - Scheduling Modeling and Simulation; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/azure.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ams) (👨‍💻 4 · 🔀 7 · 📥 19 · 📦 3 · 📋 3 - 33% open · ⏱️ 23.04.2025):

	```
	git clone https://github.com/CURENT/ams
	```
- [PyPi](https://pypi.org/project/ltbams) (📥 1.5K / month · ⏱️ 23.04.2025):
	```
	pip install ltbams
	```
- [Conda](https://anaconda.org/conda-forge/ltbams) (📥 12K · ⏱️ 23.04.2025):
	```
	conda install -c conda-forge ltbams
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">Open RAO</a></b> (🥉16 ·  ⭐ 22) - Power systems coordinated capacity calculation and security.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-open-rao) (👨‍💻 35 · 🔀 8 · 📥 52 · 📋 160 - 37% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/powsybl/powsybl-open-rao
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/reeds/">ReEDS-2.0</a></b> (🥉15 ·  ⭐ 150) - Capacity planning and dispatch model. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/ReEDS-2.0) (👨‍💻 14 · 🔀 63 · 📋 24 - 12% open · ⏱️ 25.04.2025):

	```
	git clone https://github.com/NREL/ReEDS-2.0
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerNetworkMatrices.jl</a></b> (🥉15 ·  ⭐ 24) - Power systems matrices; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerNetworkMatrices.jl) (👨‍💻 8 · 🔀 18 · 📋 57 - 43% open · ⏱️ 11.04.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerNetworkMatrices.jl
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥉14 ·  ⭐ 140) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 38 · 🔀 51 · 📦 9 · 📋 83 - 54% open · ⏱️ 04.02.2025):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerFlows.jl</a></b> (🥉14 ·  ⭐ 21) - Collection of Power Flow solution; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerFlows.jl) (👨‍💻 10 · 🔀 20 · 📋 92 - 47% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerFlows.jl
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">ExaGO</a></b> (🥉13 ·  ⭐ 79) - Large-scale power grid optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/ExaGO) (👨‍💻 30 · 🔀 12 · 📋 85 - 55% open · ⏱️ 15.12.2024):

	```
	git clone https://github.com/pnnl/ExaGO
	```
</details>
<details><summary><b><a href="https://matpower.org/">matpower-pip</a></b> (🥉13 ·  ⭐ 23) - Easy Python Access to MATPOWER. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/matpower-pip) (👨‍💻 1 · 📦 9 · 📋 16 - 12% open · ⏱️ 21.11.2024):

	```
	git clone https://github.com/yasirroni/matpower-pip
	```
- [PyPi](https://pypi.org/project/matpower) (📥 1.2K / month · 📦 2 · ⏱️ 05.10.2024):
	```
	pip install matpower
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/UnitCommitment.jl">UnitCommitment.jl</a></b> (🥉12 ·  ⭐ 120) - Optimization package for the Security-Constrained.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/UnitCommitment.jl) (👨‍💻 6 · 🔀 28 · 📋 8 - 12% open · ⏱️ 19.08.2024):

	```
	git clone https://github.com/ANL-CEEESA/UnitCommitment.jl
	```
</details>
<details><summary><b><a href="https://matpower.org/">MOST</a></b> (🥉12 ·  ⭐ 33) - MATPOWER Optimal Scheduling Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/most) (🔀 12 · 📋 42 - 23% open · ⏱️ 16.04.2025):

	```
	git clone https://github.com/MATPOWER/most
	```
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Distribution</a></b> (🥉12 ·  ⭐ 21) - Multi-energy model for small scale applications in.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-distribution) (👨‍💻 7 · 🔀 10 · 📋 25 - 64% open · ⏱️ 08.04.2025):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-distribution
	```
</details>
<details><summary><b><a href="https://github.com/ebalogun01/EV-EcoSim">EV-EcoSim</a></b> (🥉9 ·  ⭐ 25 · 💤) - A grid-aware co-simulation platform for the design and.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ebalogun01/EV-EcoSim) (🔀 5 · 📋 72 - 12% open · ⏱️ 19.04.2024):

	```
	git clone https://github.com/ebalogun01/EV-EcoSim/
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES - Version 5.0</a></b> (🥉7 ·  ⭐ 23 · 💤) - Wholesale Power Market Test Bed. <code><a href="https://github.com/ames-market/AMES-V5.0/blob/master/LICENSE.rst">❗️Custom</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-V5.0) (👨‍💻 3 · 🔀 6 · ⏱️ 08.06.2023):

	```
	git clone https://github.com/ames-market/AMES-V5.0
	```
</details>
<details><summary><b><a href="https://github.com/LBNL-ETA/DOPER">DOPER</a></b> (🥉7 ·  ⭐ 21 · 📈) - Distributed Optimal and Predictive Energy Resources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LBNL-ETA/DOPER) (👨‍💻 3 · 🔀 11 · ⏱️ 30.01.2025):

	```
	git clone https://github.com/LBNL-ETA/DOPER
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSystemsInvestmentsPortfolios.jl</a></b> (🥉7 ·  ⭐ 12) - Data models for Power Systems investment models; NREL.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl) (👨‍💻 5 · 🔀 8 · 📋 33 - 54% open · ⏱️ 21.03.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSystemsInvestments.jl</a></b> (🥉6 ·  ⭐ 18) - Power Systems investment models; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSystemsInvestments.jl) (👨‍💻 4 · 🔀 11 · 📋 12 - 91% open · ⏱️ 08.10.2024):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestments.jl
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/reopt/">EGRIP.jl</a></b> (🥉6 ·  ⭐ 8 · 💤) - Julia/MATALB package for power system restoration planning.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/EGRIP.jl) (👨‍💻 4 · ⏱️ 11.12.2023):

	```
	git clone https://github.com/ANL-CEEESA/EGRIP.jl
	```
</details>
<details><summary><b><a href="https://github.com/yasirroni/mypower">mypower</a></b> (🥉5 ·  ⭐ 7 · 💤) - Supplementary function of MATPOWER in Python. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/mypower) (🔀 1 · ⏱️ 26.11.2022):

	```
	git clone https://github.com/yasirroni/mypower
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES (V4.0)</a></b> (🥉2 ·  ⭐ 13 · 💤) - Agent based Modeling of Electricity Systems. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-v4.0) (👨‍💻 2 · 🔀 7 · 📋 5 - 60% open · ⏱️ 28.08.2020):

	```
	git clone https://github.com/ames-market/AMES-v4.0
	```
</details>
<details><summary><b><a href="https://www.epri.com/pages/sa/opendss">OpenDSS</a></b> (🥉2) - Distribution system simulator. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- _No project information available._</details>
<br>

## Interface

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥇21 ·  ⭐ 32) - A package for access to direct dll version of OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 6 · 🔀 9 · 📦 35 · ⏱️ 22.04.2025):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 1.5K / month · 📦 7 · ⏱️ 29.03.2025):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.py</a></b> (🥇19 ·  ⭐ 94 · 💤) - A direct library interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.py) (👨‍💻 3 · 🔀 24 · 📦 73 · 📋 100 - 15% open · ⏱️ 29.03.2024):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.py
	```
- [PyPi](https://pypi.org/project/OpenDSSDirect.py) (📥 4.7K / month · 📦 16 · ⏱️ 11.03.2021):
	```
	pip install OpenDSSDirect.py
	```
</details>
<details><summary><b><a href="https://github.com/sogno-platform/cimpy">CIMpy</a></b> (🥇19 ·  ⭐ 60) - CIM files to the XML/RDF format. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/cimpy) (👨‍💻 11 · 🔀 23 · 📦 10 · 📋 24 - 50% open · ⏱️ 23.02.2025):

	```
	git clone https://github.com/sogno-platform/cimpy
	```
- [PyPi](https://pypi.org/project/cimpy) (📥 960 / month · 📦 1 · ⏱️ 20.06.2024):
	```
	pip install cimpy
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/ESA">Easy SimAuto</a></b> (🥈16 ·  ⭐ 47) - Python interface to PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/ESA) (👨‍💻 12 · 🔀 13 · 📦 7 · 📋 100 - 15% open · ⏱️ 16.01.2025):

	```
	git clone https://github.com/mzy2240/ESA
	```
- [PyPi](https://pypi.org/project/esa) (📥 2.6K / month · 📦 1 · ⏱️ 21.05.2022):
	```
	pip install esa
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">AltDSS/DSS C-API</a></b> (🥈15 ·  ⭐ 34) - a plain C interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_capi) (👨‍💻 8 · 🔀 13 · 📥 27K · 📋 120 - 13% open · ⏱️ 11.07.2024):

	```
	git clone https://github.com/dss-extensions/dss_capi
	```
</details>
<details><summary><b><a href="https://github.com/UGM-EPSLab/matpowercaseframes">matpowercaseframes</a></b> (🥈15 ·  ⭐ 5) - Parse MATPOWER case into pandas DataFrame. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/UGM-EPSLab/matpowercaseframes) (👨‍💻 7 · 🔀 2 · 📋 4 - 25% open · ⏱️ 11.02.2025):

	```
	git clone https://github.com/UGM-EPSLab/matpowercaseframes
	```
- [PyPi](https://pypi.org/project/matpowercaseframes) (📥 10K / month · 📦 3 · ⏱️ 11.02.2025):
	```
	pip install matpowercaseframes
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/grid/pydss.html">PyDSS</a></b> (🥈14 ·  ⭐ 39) - A Python wrapper for OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/PyDSS) (👨‍💻 23 · 🔀 23 · 📦 2 · 📋 33 - 51% open · ⏱️ 30.09.2024):

	```
	git clone https://github.com/NREL/PyDSS
	```
- [PyPi](https://pypi.org/project/pydss) (📥 43 / month · ⏱️ 17.08.2011):
	```
	pip install pydss
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/grg-pssedata">grg-pssedata</a></b> (🥈13 ·  ⭐ 31 · 💤) - Python tools for working with PSSE v33 data files. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/grg-pssedata) (👨‍💻 3 · 🔀 11 · 📦 6 · 📋 13 - 23% open · ⏱️ 14.12.2020):

	```
	git clone https://github.com/lanl-ansi/grg-pssedata
	```
- [PyPi](https://pypi.org/project/grg-pssedata) (📥 200 / month · 📦 1 · ⏱️ 15.12.2020):
	```
	pip install grg-pssedata
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">AltDSS-Python</a></b> (🥈13 ·  ⭐ 14 · 💤) - Modern Python bindings for an alternative.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/AltDSS-Python) (📦 12 · 📋 9 - 77% open · ⏱️ 29.03.2024):

	```
	git clone https://github.com/dss-extensions/AltDSS-Python
	```
- [PyPi](https://pypi.org/project/altdss) (📥 6.4K / month · 📦 2 · ⏱️ 29.03.2024):
	```
	pip install altdss
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool">CIMTool</a></b> (🥉12 ·  ⭐ 53) - CIMugs CIMTool for the CIM. <code><a href="https://tldrlegal.com/search?q=LGPL-2.1">❗️LGPL-2.1</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool) (👨‍💻 17 · 🔀 6 · 📥 2.2K · 📋 83 - 37% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/CIMug-org/CIMTool
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.jl</a></b> (🥉12 ·  ⭐ 28) - Cross-platform Julia interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.jl) (👨‍💻 8 · 🔀 6 · 📋 43 - 23% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.jl
	```
</details>
<details><summary><b><a href="https://github.com/felipemarkson/dssdata">DSSData</a></b> (🥉11 ·  ⭐ 16 · 💤) - A micro-framework for simulation and data analysis of.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/felipemarkson/dssdata) (👨‍💻 2 · 🔀 3 · 📥 56 · 📦 2 · 📋 36 - 13% open · ⏱️ 10.04.2023):

	```
	git clone https://github.com/felipemarkson/dssdata
	```
- [PyPi](https://pypi.org/project/dssdata) (📥 450 / month · ⏱️ 24.01.2023):
	```
	pip install dssdata
	```
</details>
<details><summary><b><a href="https://github.com/RWTH-IAEW/cimpyorm">cimpyorm</a></b> (🥉11 ·  ⭐ 10 · 💤) - Python ORM middleware for IEC CIM and CGMES datasets. <code><a href="https://tldrlegal.com/search?q=BSD-3.0">❗️BSD-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/RWTH-IAEW/cimpyorm) (👨‍💻 5 · 🔀 5 · 📦 4 · 📋 3 - 33% open · ⏱️ 19.10.2023):

	```
	git clone https://github.com/RWTH-IAEW/cimpyorm
	```
- [PyPi](https://pypi.org/project/cimpyorm) (📥 4.4K / month · ⏱️ 19.10.2023):
	```
	pip install cimpyorm
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool-Builders-Library">CIMTool-Builders-Library</a></b> (🥉9 ·  ⭐ 7) - Publically available XSLT builders. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool-Builders-Library) (👨‍💻 4 · 🔀 3 · ⏱️ 03.04.2025):

	```
	git clone https://github.com/CIMug-org/CIMTool-Builders-Library
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS MATLAB</a></b> (🥉8 ·  ⭐ 11) - MATLAB interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_matlab) (🔀 2 · 📥 1.2K · 📋 21 - 33% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/dss_matlab
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS Sharp</a></b> (🥉8 ·  ⭐ 10 · 💤) - C#/.NET wrapper library for DSS C-API. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_sharp) (📥 55 · 📦 3 · 📋 15 - 20% open · ⏱️ 15.03.2024):

	```
	git clone https://github.com/dss-extensions/dss_sharp
	```
</details>
<details><summary><b><a href="https://github.com/anderson-optimization/em-psse">PSSE RAW</a></b> (🥉5 ·  ⭐ 35 · 💤) - PSSE RAW parser. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/anderson-optimization/em-psse) (👨‍💻 2 · 🔀 15 · ⏱️ 07.01.2020):

	```
	git clone https://github.com/anderson-optimization/em-psse
	```
</details>
<details><summary><b><a href="https://ltb.curent.org">Andes.jl</a></b> (🥉4 ·  ⭐ 8 · 💤) - Julia interface for ANDES. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/Andes.jl) (🔀 1 · ⏱️ 05.02.2024):

	```
	git clone https://github.com/cuihantao/Andes.jl
	```
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER interface</a></b> (🥉4 ·  ⭐ 5) - Interface for OpenDER. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER_interface) (👨‍💻 2 · 🔀 1 · ⏱️ 10.02.2025):

	```
	git clone https://github.com/epri-dev/OpenDER_interface
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/EasySimauto.jl">EasySimauto.jl</a></b> (🥉3 ·  ⭐ 5 · 💤) - Julia interface for EasySimAuto and PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/EasySimauto.jl) (👨‍💻 2 · ⏱️ 31.07.2023):

	```
	git clone https://github.com/mzy2240/EasySimauto.jl
	```
</details>
<br>

## Gas Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇24 ·  ⭐ 180) - Pipeflow Calculation Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 25 · 🔀 66 · 📦 29 · 📋 160 - 47% open · ⏱️ 08.04.2025):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 8.1K / month · 📦 8 · ⏱️ 04.12.2024):
	```
	pip install pandapipes
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/GasModels.jl">GasModels.jl</a></b> (🥉15 ·  ⭐ 68) - Gas Network Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/GasModels.jl) (👨‍💻 14 · 🔀 16 · 📋 150 - 32% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/lanl-ansi/GasModels.jl
	```
</details>
<details><summary><b><a href="https://matpower.org/">MPNG</a></b> (🥉7 ·  ⭐ 10 · 💤) - Simulator for Optimal Power and Natural Gas Flow. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/mpng) (👨‍💻 3 · 🔀 5 · ⏱️ 13.09.2023):

	```
	git clone https://github.com/MATPOWER/mpng
	```
</details>
<br>

## Co-Simulation Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇27 ·  ⭐ 960) - Modelica-based environment for modeling and simulation. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 200 · 🔀 310 · 📥 390 · 📋 8.2K - 24% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 48K · ⭐ 6 · ⏱️ 04.04.2025):
	```
	docker pull openmodelica/openmodelica
	```
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥉26 ·  ⭐ 790) - Precise Code Interaction Coupling Environment. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 57 · 🔀 190 · 📥 34K · 📋 910 - 22% open · ⏱️ 16.04.2025):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 1.7K / month · 📦 8 · ⏱️ 02.04.2025):
	```
	pip install pyprecice
	```
- [Conda](https://anaconda.org/conda-forge/pyprecice) (📥 110K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge pyprecice
	```
- [Docker Hub](https://hub.docker.com/r/precice/precice) (📥 27K · ⏱️ 01.05.2025):
	```
	docker pull precice/precice
	```
</details>
<br>

## Optimization Modeling Language

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pyomo.org">Pyomo</a></b> (🥇40 ·  ⭐ 2.2K) - Python-based Optimization Modeling Language. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Pyomo/pyomo) (👨‍💻 170 · 🔀 530 · 📥 4.3K · 📦 3.9K · 📋 1.4K - 21% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/Pyomo/pyomo
	```
- [PyPi](https://pypi.org/project/Pyomo) (📥 510K / month · 📦 280 · ⏱️ 21.02.2025):
	```
	pip install Pyomo
	```
- [Conda](https://anaconda.org/conda-forge/pyomo) (📥 1.5M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge pyomo
	```
</details>
<details><summary><b><a href="https://github.com/cvxpy/cvxpy">CVXPY</a></b> (🥈38 ·  ⭐ 5.7K) - Convex optimization modeling language. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxpy/cvxpy) (👨‍💻 210 · 🔀 1.1K · 📥 590 · 📦 17K · 📋 1.5K - 16% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/cvxpy/cvxpy
	```
- [PyPi](https://pypi.org/project/cvxpy) (📥 1.9M / month · 📦 650 · ⏱️ 13.04.2025):
	```
	pip install cvxpy
	```
- [Conda](https://anaconda.org/conda-forge/cvxpy) (📥 1.6M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge cvxpy
	```
</details>
<details><summary><b><a href="https://cvxopt.org/">CVXOPT</a></b> (🥈28 ·  ⭐ 1K) - Python Software for Convex Optimization. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxopt/cvxopt) (👨‍💻 9 · 🔀 210 · 📦 14K · 📋 190 - 21% open · ⏱️ 23.10.2024):

	```
	git clone https://github.com/cvxopt/cvxopt
	```
- [PyPi](https://pypi.org/project/cvxopt) (📥 590K / month · 📦 390 · ⏱️ 09.08.2023):
	```
	pip install cvxopt
	```
- [Conda](https://anaconda.org/conda-forge/cvxopt) (📥 1.4M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge cvxopt
	```
</details>
<details><summary><b><a href="https://jump.dev">JuMP</a></b> (🥉25 ·  ⭐ 2.3K) - Julia-based Optimization Modeling Language. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/jump-dev/JuMP.jl) (👨‍💻 160 · 🔀 400 · 📋 1.5K - 0% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/jump-dev/JuMP.jl
	```
</details>
<details><summary><b><a href="https://github.com/metab0t/PyOptInterface">PyOptInterface</a></b> (🥉19 ·  ⭐ 270) - Efficient modeling interface for optimization in.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/metab0t/PyOptInterface) (👨‍💻 2 · 🔀 14 · 📦 17 · 📋 22 - 13% open · ⏱️ 22.04.2025):

	```
	git clone https://github.com/metab0t/PyOptInterface
	```
- [PyPi](https://pypi.org/project/pyoptinterface) (📥 5.2K / month · 📦 4 · ⏱️ 19.03.2025):
	```
	pip install pyoptinterface
	```
</details>
<details><summary><b><a href="https://github.com/XiongPengNUS/rsome">RSOME</a></b> (🥉17 ·  ⭐ 310) - Robust Stochastic Optimization Made Easy. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/XiongPengNUS/rsome) (👨‍💻 3 · 🔀 57 · 📋 45 - 15% open · ⏱️ 15.11.2024):

	```
	git clone https://github.com/XiongPengNUS/rsome
	```
- [PyPi](https://pypi.org/project/rsome) (📥 1.3K / month · 📦 4 · ⏱️ 29.10.2024):
	```
	pip install rsome
	```
</details>
<details><summary><b><a href="https://github.com/sanurielf/kvxopt">KVXOPT</a></b> (🥉13 ·  ⭐ 11) - CVXOPT with more wrappers suite-sparse. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sanurielf/kvxopt) (👨‍💻 15 · 🔀 1 · 📦 30 · ⏱️ 08.05.2024):

	```
	git clone https://github.com/sanurielf/kvxopt
	```
- [PyPi](https://pypi.org/project/kvxopt) (📥 9.8K / month · 📦 12 · ⏱️ 08.05.2024):
	```
	pip install kvxopt
	```
- [Conda](https://anaconda.org/conda-forge/kvxopt) (📥 300K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge kvxopt
	```
</details>
<details><summary><b><a href="https://github.com/exanauts/ExaModels.jl">ExaModels</a></b> (🥉10 ·  ⭐ 57) - An algebraic modeling and automatic differentiation tool in.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/exanauts/ExaModels.jl) (👨‍💻 6 · 🔀 6 · 📋 27 - 44% open · ⏱️ 07.02.2025):

	```
	git clone https://github.com/exanauts/ExaModels.jl
	```
</details>
<br>

## Optimizer

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://developers.google.com/optimization/">OR-Tools</a></b> (🥇38 ·  ⭐ 12K · 📉) - Google Optimization Tools. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 180 · 🔀 2.2K · 📥 900K · 📦 320 · 📋 3.1K - 2% open · ⏱️ 17.02.2025):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/ortools) (📥 1.9M / month · 📦 280 · ⏱️ 17.02.2025):
	```
	pip install ortools
	```
- [Conda](https://anaconda.org/conda-forge/ortools-python) (📥 110K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ortools-python
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Xopt</a></b> (🥇37 ·  ⭐ 12K · 📉) - Flexible high-level optimization in Python. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 180 · 🔀 2.2K · 📥 900K · 📦 320 · 📋 3.1K - 2% open · ⏱️ 17.02.2025):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/xopt) (📥 1.4K / month · 📦 3 · ⏱️ 10.04.2025):
	```
	pip install xopt
	```
- [Conda](https://anaconda.org/conda-forge/xopt) (📥 49K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge xopt
	```
</details>
<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥈36 ·  ⭐ 1.2K) - Large-scale Sparse Linear Problem Optimizer. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 84 · 🔀 210 · 📥 2.2K · 📦 1.2K · 📋 860 - 12% open · ⏱️ 20.03.2025):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/highspy) (📥 240K / month · 📦 67 · ⏱️ 20.03.2025):
	```
	pip install highspy
	```
- [Conda](https://anaconda.org/conda-forge/highs) (📥 24K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge highs
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Tulip</a></b> (🥈35 ·  ⭐ 12K · 📉) - Interior-point solver in pure Julia. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 180 · 🔀 2.2K · 📥 900K · 📦 320 · 📋 3.1K - 2% open · ⏱️ 17.02.2025):

	```
	git clone https://github.com/google/or-tools
	```
</details>
<details><summary><b><a href="https://osqp.org">OSQP</a></b> (🥈33 ·  ⭐ 1.8K) - Operator Splitting QP Solver. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/r.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/osqp/osqp) (👨‍💻 36 · 🔀 360 · 📥 110K · 📋 380 - 26% open · ⏱️ 09.04.2025):

	```
	git clone https://github.com/osqp/osqp
	```
- [PyPi](https://pypi.org/project/osqp) (📥 2.3M / month · 📦 99 · ⏱️ 02.04.2025):
	```
	pip install osqp
	```
- [Conda](https://anaconda.org/conda-forge/osqp) (📥 1.2M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge osqp
	```
</details>
<details><summary><b><a href="https://www.scipopt.org/">PySCIPOpt</a></b> (🥈31 ·  ⭐ 870) - Python interface for SCIP. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/scipopt/PySCIPOpt) (👨‍💻 78 · 🔀 260 · 📦 350 · 📋 560 - 4% open · ⏱️ 22.04.2025):

	```
	git clone https://github.com/scipopt/PySCIPOpt
	```
- [PyPi](https://pypi.org/project/PySCIPOpt) (📥 69K / month · 📦 47 · ⏱️ 25.02.2025):
	```
	pip install PySCIPOpt
	```
- [Conda](https://anaconda.org/conda-forge/pyscipopt) (📥 490K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge pyscipopt
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Ipopt</a></b> (🥈27 ·  ⭐ 1.5K) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 35 · 🔀 290 · 📥 20K · 📋 610 - 1% open · ⏱️ 15.04.2025):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 1.6K / month · 📦 10 · ⏱️ 07.04.2021):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/conda-forge/ipopt) (📥 1.6M · ⏱️ 23.04.2025):
	```
	conda install -c conda-forge ipopt
	```
</details>
<details><summary><b><a href="https://github.com/cvxgrp/scs">SCS</a></b> (🥈27 ·  ⭐ 570) - Splitting Conic Solver. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxgrp/scs) (👨‍💻 29 · 🔀 140 · 📋 190 - 24% open · ⏱️ 15.04.2025):

	```
	git clone https://github.com/cvxgrp/scs
	```
- [PyPi](https://pypi.org/project/scs) (📥 1.7M / month · 📦 56 · ⏱️ 04.01.2025):
	```
	pip install scs
	```
- [Conda](https://anaconda.org/conda-forge/scs) (📥 1.3M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge scs
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.rs">Clarabel.rs</a></b> (🥉26 ·  ⭐ 430 · 📉) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.rs) (👨‍💻 11 · 🔀 32 · 📦 32 · 📋 60 - 26% open · ⏱️ 07.03.2025):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.rs
	```
- [PyPi](https://pypi.org/project/clarabel) (📥 1.5M / month · 📦 31 · ⏱️ 02.02.2025):
	```
	pip install clarabel
	```
- [Conda](https://anaconda.org/conda-forge/clarabel) (📥 200K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge clarabel
	```
</details>
<details><summary><b><a href="https://github.com/embotech/ecos">ECOS</a></b> (🥉25 ·  ⭐ 500 · 💤) - Conic solver for second-order cone programming. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/r.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/embotech/ecos) (👨‍💻 40 · 🔀 120 · 📋 160 - 40% open · ⏱️ 04.01.2022):

	```
	git clone https://github.com/embotech/ecos
	```
- [PyPi](https://pypi.org/project/ecos) (📥 660K / month · 📦 49 · ⏱️ 18.06.2024):
	```
	pip install ecos
	```
- [Conda](https://anaconda.org/conda-forge/ecos) (📥 1M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ecos
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">CBC</a></b> (🥉23 ·  ⭐ 890 · 📈) - COIN-OR Branch-and-Cut solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 34 · 🔀 120 · 📥 46K · 📋 510 - 28% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coincbc) (📥 1.3M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge coincbc
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Clp</a></b> (🥉23 ·  ⭐ 890 · 📈) - COIN-OR Linear Programming Solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 34 · 🔀 120 · 📥 46K · 📋 510 - 28% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coin-or-clp) (📥 970K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge coin-or-clp
	```
</details>
<details><summary><b><a href="https://github.com/PREDICT-EPFL/piqp">PIQP</a></b> (🥉22 ·  ⭐ 110) - Proximal Interior Point Quadratic Programming solver. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/r.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PREDICT-EPFL/piqp) (👨‍💻 4 · 🔀 15 · 📥 670 · 📦 45 · 📋 16 - 43% open · ⏱️ 05.04.2025):

	```
	git clone https://github.com/PREDICT-EPFL/piqp
	```
- [PyPi](https://pypi.org/project/piqp) (📥 24K / month · 📦 9 · ⏱️ 17.03.2025):
	```
	pip install piqp
	```
- [Conda](https://anaconda.org/conda-forge/piqp) (📥 210K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge piqp
	```
</details>
<details><summary><b><a href="https://ampl.com/">AMPLPY</a></b> (🥉22 ·  ⭐ 80) - Python API for AMPL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ampl/amplpy) (👨‍💻 9 · 🔀 20 · 📦 120 · 📋 48 - 2% open · ⏱️ 27.04.2025):

	```
	git clone https://github.com/ampl/amplpy
	```
- [PyPi](https://pypi.org/project/amplpy) (📥 79K / month · 📦 6 · ⏱️ 25.04.2025):
	```
	pip install amplpy
	```
- [Conda](https://anaconda.org/conda-forge/amplpy) (📥 420K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge amplpy
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.jl">Clarabel.jl</a></b> (🥉16 ·  ⭐ 200) - Interior-point solver for convex conic optimisation in.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.jl) (👨‍💻 12 · 🔀 19 · 📋 58 - 10% open · ⏱️ 07.03.2025):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.jl
	```
</details>
<details><summary><b><a href="https://github.com/MadNLP/MadNLP.jl">MadNLP</a></b> (🥉16 ·  ⭐ 180) - A solver for nonlinear programming with GPU support. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MadNLP/MadNLP.jl) (👨‍💻 15 · 🔀 16 · 📋 97 - 36% open · ⏱️ 09.04.2025):

	```
	git clone https://github.com/MadNLP/MadNLP.jl
	```
</details>
<details><summary><b><a href="https://www.opti-verse.org/">OptiVerse</a></b> (🥉6 ·  ⭐ 12) - A library with innovative optimization solutions. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/feyntech-opt/OptiVerse) (👨‍💻 5 · 🔀 12 · ⏱️ 15.02.2025):

	```
	git clone https://github.com/feyntech-opt/OptiVerse
	```
</details>
<br>

## Machine/Reinforcement Learning for Power Grid

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇26 ·  ⭐ 340) - Modeling sequential decision making in power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/grid2op) (👨‍💻 32 · 🔀 130 · 📋 380 - 14% open · ⏱️ 15.04.2025):

	```
	git clone https://github.com/rte-france/Grid2Op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 3.1K / month · 📦 23 · ⏱️ 15.04.2025):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 10K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/RLGC-Project/RLGC">RLGC</a></b> (🥈9 ·  ⭐ 120 · 💤) - RL for Grid Control (RLGC). <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/RLGC-Project/RLGC) (👨‍💻 4 · 🔀 32 · 📋 15 - 33% open · ⏱️ 08.04.2022):

	```
	git clone https://github.com/RLGC-Project/RLGC
	```
</details>
<details><summary><b><a href="https://github.com/JarvisETHZ/Daline">Daline</a></b> (🥉7 ·  ⭐ 18) - A Data-driven Power Flow Linearization Toolbox. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/JarvisETHZ/Daline) (📥 6 · ⏱️ 26.04.2025):

	```
	git clone https://github.com/JarvisETHZ/Daline
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉4 ·  ⭐ 9 · 💤) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes_gym) (👨‍💻 2 · 🔀 5 · ⏱️ 28.01.2022):

	```
	git clone https://github.com/cuihantao/andes_gym
	```
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.powsybl.org">PowSyBl Diagram</a></b> (🥇18 ·  ⭐ 83) - single-line substation diagrams and network graph.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-diagram) (👨‍💻 27 · 🔀 14 · 📦 31 · 📋 180 - 39% open · ⏱️ 30.04.2025):

	```
	git clone https://github.com/powsybl/powsybl-diagram
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerGraphics.jl</a></b> (🥉15 ·  ⭐ 30) - Visualization for PowerSimulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerGraphics.jl) (👨‍💻 11 · 🔀 17 · 📋 39 - 38% open · ⏱️ 19.03.2025):

	```
	git clone https://github.com/NREL-Sienna/powergraphics.jl
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AGVis</a></b> (🥉11 ·  ⭐ 7) - Geographical Visualization for Power Grid; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 9 · 🔀 5 · 📥 18 · 📦 3 · 📋 25 - 36% open · ⏱️ 07.06.2024):

	```
	git clone https://github.com/CURENT/agvis
	```
- [PyPi](https://pypi.org/project/agvis) (📥 110 / month · ⏱️ 07.06.2024):
	```
	pip install agvis
	```
</details>
<br>

## Messaging Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥇24 ·  ⭐ 130) - Co-simulation framework. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 39 · 🔀 42 · 📥 27K · 📋 680 - 13% open · ⏱️ 25.02.2025):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 18K / month · 📦 13 · ⏱️ 28.02.2025):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/conda-forge/helics) (📥 21K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge helics
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB DiME</a></b> (🥉7 ·  ⭐ 3 · 💤) - Distributed Messaging Environment; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/dime) (👨‍💻 4 · 🔀 2 · 📋 48 - 27% open · ⏱️ 31.07.2023):

	```
	git clone https://github.com/CURENT/dime
	```
</details>
<br>

## Power System Data

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/MV-LV-Networks">Australian MV-LV Networks</a></b> ( ⭐ 26 · 💤)  - Large-scale three-phase Australian MV distribution..

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow</a></b> ( ⭐ 330 · 💤)  - Benchmarks for OPF.

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Unit Commitment</a></b> ( ⭐ 95 · 💤)  - Benchmarks for UC.

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow with HVDC Lines</a></b> ( ⭐ 23 · 💤)  - Benchmarks for OPF with HVDC.

🔗&nbsp;<b><a href="https://github.com/enliten/ENLITEN-Grid-Econ-Data">WECC-and-NPCC-Electricity-Economic-Data</a></b> ( ⭐ 7)  - Economic data on WECC and NPCC.

🔗&nbsp;<b><a href="https://opendata.elia.be/pages/home/">OpenDataElia</a></b>  - Data by opendatasoft.

🔗&nbsp;<b><a href="https://github.com/owid/energy-data">Data on Energy</a></b> ( ⭐ 330)  - Data on energy by Our World in Data.

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 60 · 💤)  - Cross-Domain Data Hub with Data in USA.

🔗&nbsp;<b><a href="https://github.com/openEDI/documentation">PV Rooftop Database</a></b> ( ⭐ 61)  - NREL PV Rooftop Database.

🔗&nbsp;<b><a href="https://github.com/rte-france/digital-fault-recording-database">Electrical Signals Databases</a></b> ( ⭐ 27)  - Voltage and current samples from Digital Fault Recorder.

🔗&nbsp;<b><a href="https://github.com/lbl-hub/CSEE-Benchmark">A new power system benchmark</a></b> ( ⭐ 27 · 💤)  - A new type of power system calculation example by the..

🔗&nbsp;<b><a href="https://github.com/NanpengYu/pmuBAGE">pmuBAGE</a></b> ( ⭐ 8 · 💤)  - Synthetic phasor measurement unit dataset.

<details><summary><b><a href="https://www.gridstatus.io">GridStatus</a></b> (🥇25 ·  ⭐ 330) - Extract data from ISOs and other sources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridstatus/gridstatus) (👨‍💻 32 · 🔀 62 · 📦 20 · 📋 120 - 37% open · ⏱️ 01.05.2025):

	```
	git clone https://github.com/kmax12/gridstatus
	```
- [PyPi](https://pypi.org/project/gridstatus) (📥 23K / month · 📦 2 · ⏱️ 22.04.2025):
	```
	pip install gridstatus
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥈24 ·  ⭐ 180 · 📉) - Tools to combine multiple power plant databases. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 34 · 🔀 64 · 📥 87 · 📦 77 · 📋 95 - 22% open · ⏱️ 23.04.2025):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 1.9K / month · ⏱️ 01.02.2025):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/conda-forge/powerplantmatching) (📥 68K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powerplantmatching
	```
</details>
<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥈23 ·  ⭐ 310) - Calculating Renewable Power Potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 40 · 🔀 100 · 📦 100 · 📋 140 - 28% open · ⏱️ 08.04.2025):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 2.3K / month · ⏱️ 30.01.2025):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/conda-forge/atlite) (📥 77K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge atlite
	```
</details>
<details><summary><b><a href="https://groups.io/g/powergenome">PowerGenome</a></b> (🥉21 ·  ⭐ 210) - Create inputs for power systems models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGenome/PowerGenome) (👨‍💻 18 · 🔀 68 · 📋 180 - 50% open · ⏱️ 21.03.2025):

	```
	git clone https://github.com/PowerGenome/PowerGenome
	```
- [PyPi](https://pypi.org/project/PowerGenome) (📥 360 / month · ⏱️ 21.03.2025):
	```
	pip install PowerGenome
	```
- [Conda](https://anaconda.org/conda-forge/powergenome) (📥 930 · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powergenome
	```
</details>
<details><summary><b><a href="https://simbench.de/en/">SimBench</a></b> (🥉21 ·  ⭐ 120) - Benchmark dataset of German LV/MV/HV grids including.. <code><a href="https://tldrlegal.com/search?q=odbl-1.0">❗️odbl-1.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code>juptyer</code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/simbench) (👨‍💻 4 · 🔀 30 · 📦 46 · 📋 34 - 5% open · ⏱️ 13.04.2025):

	```
	git clone https://github.com/e2nIEE/simbench
	```
- [PyPi](https://pypi.org/project/simbench) (📥 5K / month · 📦 10 · ⏱️ 13.04.2025):
	```
	pip install simbench
	```
</details>
<details><summary><b><a href="https://www.energydatamodel.org/">EnergyDataModel</a></b> (🥉14 ·  ⭐ 58) - Represent energy systems as Python data classes. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rebase-energy/EnergyDataModel) (👨‍💻 3 · 🔀 4 · ⏱️ 07.04.2025):

	```
	git clone https://github.com/rebase-energy/EnergyDataModel
	```
- [PyPi](https://pypi.org/project/energydatamodel) (📥 130 / month · 📦 2 · ⏱️ 23.03.2025):
	```
	pip install energydatamodel
	```
</details>
<details><summary><b><a href="https://deepsolar.web.app">DeepSolar</a></b> (🥉9 ·  ⭐ 250 · 💤) - Houseshold-level solar panel identification with deep learning. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/wangzhecheng/DeepSolar) (👨‍💻 2 · 🔀 70 · 📋 17 - 76% open · ⏱️ 26.03.2019):

	```
	git clone https://github.com/wangzhecheng/DeepSolar
	```
</details>
<br>

## Power Electronics

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/gseim/gseim">GSEIM</a></b> (🥇6 ·  ⭐ 2 · 💤) - Simulation of electrical circuits. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/pypi.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gseim/gseim) (👨‍💻 1):

	```
	git clone https://github.com/gseim/gseim
	```
- [PyPi](https://pypi.org/project/GSEIM) (📥 25 / month · ⏱️ 16.07.2022):
	```
	pip install GSEIM
	```
</details>
<br>

## Database Management

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/NREL/dgen">dGen</a></b> (🥇16 ·  ⭐ 64) - The Distributed Generation Market Demand (dGen) model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/dgen) (👨‍💻 10 · 🔀 160 · 📋 42 - 54% open · ⏱️ 17.04.2025):

	```
	git clone https://github.com/NREL/dgen
	```
</details>
<details><summary><b><a href="https://github.com/dsgrid/dsgrid">dsgrid</a></b> (🥉14 ·  ⭐ 27) - Demand-side grid projects, datasets and queries. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dsgrid/dsgrid) (👨‍💻 6 · 🔀 4 · 📋 120 - 44% open · ⏱️ 20.12.2024):

	```
	git clone https://github.com/dsgrid/dsgrid
	```
</details>
<br>

## Textbook

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://powercybertraining.github.io">PowerCyber Training</a></b> ( ⭐ 3)  - PowerCyber Training modules source. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/github.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Power-Systems-Textbook/TextbookSimulations">TextbookSimulations</a></b> ( ⭐ 11 · 💤)  - Examples and problems accompanying Daniel Kirschens.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/CURENT/ece522">UTK ECE 522 - Power System Analysis II</a></b> ( ⭐ 6)  - Hands-on Project for Power System Analysis II (UTK.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/bcornelusse/ELEC0447-analysis-power-systems">ELEC0447 Analysis of Electric Power and Energy Systems</a></b> ( ⭐ 22)  - Masters course of power systems analysis at ULige. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-0-dss_python">Tutorial on DER Hosting Capacity Part 0</a></b> ( ⭐ 5)  - Using dss_python. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV">Tutorial on DER Hosting Capacity Part 1</a></b> ( ⭐ 3)  - Advanced Tools for the Analysis of Three-Phase.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV">Tutorial on DER Hosting Capacity Part 2</a></b> ( ⭐ 2)  - Time-Series Analysis and PV Hosting Capacity of LV.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV">Tutorial on DER Hosting Capacity Part 3</a></b> ( ⭐ 1)  - Volt-Watt Control and PV Hosting Capacity of LV.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV">Tutorial on DER Hosting Capacity Part 4</a></b> ( ⭐ 2)  - Monte Carlo Assessment of PV Hosting Capacity of an.. <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/jinningwang/best-of-ps/blob/develop/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>



---

## Project Popularity Score

- Has homepage link & description: `+ 1`
- Has an existing GitHub repository: `+ 1`
- Has a license: `+ 1`
- Has a commonly used license (e.g. MIT): `+ 1`
- Has multiple releases: `+ 1`
- Has stable releases based on semantic version: `+ 1`
- Has a release that is less than 6 months old: `+ 1`
- Repo was update in the last 3 months: `+ 1`
- Is older than 6 months: `+ 1`
- Metrics from GitHub & package mangers:
  - Number of stars: `+ log(COUNT / 2)`
  - Number of contributors: `+ log(COUNT / 2) - 1`
  - Number of commits: `+ log(COUNT / 2) - 1`
  - Number of forks: `+ log(COUNT / 2)`
  - Number of monthly downloads: `+ log(COUNT / 2) - 1`
  - Number of dependent projects: `+ log(COUNT / 1.5)`
  - Number of watchers: `+ log(COUNT / 2) - 1`
  - Number of closed issues: `+ log(COUNT / 2) - 1`

**NOTE**: This calculation is just chosen by ***EXPERIENCE***. There is ***NO*** scientific proof that this really reflects the ***QUALITY*** of a project.

## Project Data Collection

The data collection can be deficient for the projects that are not majorly hosted in GitHub.

## Related Resources

- [HIFLD Open](https://hifld-geoplatform.hub.arcgis.com/pages/hifld-open): Public domain data for community preparedness, resiliency, research, and more
- [FNET/GridEye Web Display](https://fnetpublic.utk.edu/): A low-cost, quickly deployable GPS-synchronized wide-area frequency measurement network
- [Grid Event Signature Library](https://gesl.ornl.gov/): An initiative spearheaded by ORNL and LLNL
- [Electric Grid Test Cases by TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/): The power system test cases on this page are do not contain Critical Energy Infrastructure Information (CEII) and are provided in a variety of different formats, including PowerWorld Simulator and PowerWorld DS (*.pwb, *.pwd, *.tsb, *.aux), Matpower (*.m), PSSE (*.raw, *.dyr), and PSLF (*.epc, *.dyd).
- [Energy Systems Datasets](https://ieee-pes-data-sharing.org/datasets): a platform provides comprehensive datasets for energy systems research and development, by IEEE Task Force on Data Sharing in Energy Systems
- [Electricity Map Data](https://portal.electricitymaps.com/datasets)
- [Der-CAM](https://dercam-app.lbl.gov/): Distributed Energy Resources Customer Adoption Model for DER investment planning
- [DOME](http://faraday1.ucd.ie/dome.html): A power system analysis tool, entirely based on Python as well as on public domain efficient C and Fortran libraries, by Prof. Federico Milano.
- [G-PST Tools Portal](https://g-pst.github.io/tools/): An open tools portal with a classification approach
- [Open Source Software (OSS) for Electricity Market Research, Teaching, and Training](https://www2.econ.iastate.edu/tesfatsi/ElectricOSS.htm)
- [Open-Source-Power-Electronic-Tools](https://github.com/upb-lea/awesome-open-source-power-electronics)

## Contribution

Contributions are encouraged and always welcome! If you like to add or update projects, choose one of the following ways:

- Open an issue by selecting one of the provided categories from the [issue page](https://github.com/jinningwang/best-of-ps/issues/new/choose) and fill in the requested information.
- Modify the [projects.yaml](https://github.com/jinningwang/best-of-ps/blob/main/projects.yaml) with your additions or changes, and submit a pull request. This can also be done directly via the [Github UI](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml).

If you like to contribute to or share suggestions regarding the project metadata collection or markdown generation, please refer to the [best-of-generator](https://github.com/best-of-lists/best-of-generator) repository. If you like to create your own best-of list, we recommend to follow [this guide](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

For more information on how to add or update projects, please read the [contribution guidelines](https://github.com/jinningwang/best-of-ps/blob/main/CONTRIBUTING.md). By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/jinningwang/best-of-ps/blob/main/.github/CODE_OF_CONDUCT.md).

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
