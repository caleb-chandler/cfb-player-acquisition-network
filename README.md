# College Football Player Acquisition Network Analysis

An in-depth network analysis of college football player movement, including traditional high school recruiting along with the transfer portal. Utilizes graph theory to quantify structural differences between these two acquisition mechanisms and evaluates the strategic impact of the transfer portal on team performance.

## Project Overview

**Recruiting Network:** A set of bipartite graphs representing connections between schools and hometowns via recruits for each year from 2000-2026. Used to generate a projected network linking schools to one another via shared recruiting grounds.

**Transfer Portal Network:** A directed flow network of transfers moving between schools (2021-2025).

This repository contains the code to gather data, build these networks, calculate advanced topology metrics, generate null models for statistical validation, and visualize the results.

## Repository Structure

*data.ipynb:* Fetches raw data from the CollegeFootballData API. Collects recruiting commits, transfer portal activity, rosters, and team/player performance metrics (PPA, FPI, SRS).

*cleaning.ipynb:* Preprocesses raw data. Handles multi-player transfer edges, imputes missing player ratings based on star-counts, and prepares edge lists for NetworkX.

*analysis.ipynb:* The core computational notebook where the resulting data is analyzed.

*gephi-projects/:* .gephi files used for creating the network visualizations found in the report.

*imgs/:* Output directory for plots and graphs.
