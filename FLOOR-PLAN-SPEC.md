# Floor Plan Specification

## Overview
This document outlines the complete floor plan specification including all rooms, dimensions, doors, and windows layout with grid coordinates.

## Rooms
- **Living Room**  
  - **Dimensions**: 20ft x 15ft
  - **Coordinates**: (0,0) to (20,15)
  - **Doors**: 1 (Entry from hallway)
  - **Windows**: 2 (South wall)

- **Kitchen**  
  - **Dimensions**: 15ft x 10ft
  - **Coordinates**: (20,0) to (35,10)
  - **Doors**: 1 (Entry to Living Room)
  - **Windows**: 1 (East wall)

- **Bedroom**  
  - **Dimensions**: 15ft x 12ft
  - **Coordinates**: (0,15) to (15,27)
  - **Doors**: 1 (Entry from hallway)
  - **Windows**: 1 (North wall)

- **Bathroom**  
  - **Dimensions**: 8ft x 6ft
  - **Coordinates**: (15,15) to (23,21)
  - **Doors**: 1 (Entry from hallway)
  - **Windows**: 0

## Doors
| Room          | Type        | Location  | Dimensions  |
|---------------|-------------|-----------|-------------|
| Living Room   | Entry       | Hallway   | 3ft wide    |
| Kitchen       | Entry       | Living Room| 2ft wide    |
| Bedroom       | Entry       | Hallway   | 3ft wide    |
| Bathroom      | Entry       | Hallway   | 2ft wide    |

## Windows
| Room          | Type       | Location  | Dimensions  |
|---------------|------------|-----------|-------------|
| Living Room   | Double Paned | South Wall | 4ft wide   |
| Living Room   | Double Paned | South Wall | 4ft wide   |
| Kitchen       | Single Pane  | East Wall | 3ft wide   |
| Bedroom       | Single Pane  | North Wall | 3ft wide   |
