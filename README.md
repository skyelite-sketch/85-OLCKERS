# 85-OLCKERS
COMPLETE RENOVATION 
⸻

🧭 MASTER INSTRUCTIONS — LIBRECAD (STEP-BY-STEP)

⸻

⚙️ 1. INITIAL SETUP (DO THIS FIRST)

🔷 Open LibreCAD → New Drawing

Set Units:
	•	Go to: Options → Current Drawing Preferences
	•	Units: Millimeter
	•	Format: Decimal

⸻

🔷 Set Grid
	•	Grid spacing: 1000 mm
	•	Minor grid: 100 mm
	•	Turn ON:
	•	Snap to grid
	•	Snap to endpoints

⸻

🧱 2. CREATE LAYERS (CRITICAL)

Go to Layer List → Add Layer

Create these EXACT layers:

Layer Name	Color	Width
A-WALL-EXT	Red	0.50 mm
A-WALL-INT	Cyan	0.30 mm
A-DOOR	Green	0.25 mm
A-WINDOW	Blue	0.25 mm
A-DIMS	Yellow	0.18 mm
A-TEXT	White	0.18 mm

👉 Always draw on the correct layer.

⸻

📐 3. DRAW EXTERNAL WALLS

🔷 Step 1: Outer Rectangle
	•	Select: Draw → Rectangle
	•	First corner: 0,0
	•	Second corner: 14000,8500

⸻

🔷 Step 2: Wall Thickness
	•	Select: Modify → Offset
	•	Distance: 230
	•	Click inside → create inner wall

👉 You now have 230 mm external walls

⸻

🧱 4. DRAW INTERNAL WALL GRID

Switch to layer: A-WALL-INT

⸻

🔷 Vertical Walls

Use: Draw → Line

Draw lines at:
	•	3000,0 → 3000,8500
	•	6000,0 → 6000,8500
	•	9000,0 → 9000,8500
	•	12000,0 → 12000,8500

⸻

🔷 Horizontal Walls

Draw lines at:
	•	0,2500 → 14000,2500
	•	0,4500 → 14000,4500
	•	0,6000 → 14000,6000
	•	0,9000 → 14000,9000

⸻

🔷 Give Thickness
	•	Offset each line: 110 mm
👉 These become real walls

⸻

🚪 5. ADD DOORS (PROPER METHOD)

Switch to: A-DOOR

⸻

🔷 Step 1: Create Opening
	•	Use: Modify → Trim
	•	Remove wall segment:
	•	From 7000,2500 → 7900,2500

⸻

🔷 Step 2: Draw Door
	•	Draw line: 7000,2500 → 7900,2500
	•	Draw arc:
	•	Center: 7000,2500
	•	Radius: 900
	•	Angle: 0 → 90°

👉 That’s a standard 900 mm door

⸻

🪟 6. ADD WINDOWS

Switch to: A-WINDOW

⸻

🔷 Draw Window Openings

Use Line tool

Living:
	•	1500,4000 → 3000,4000
	•	4000,4000 → 5800,4000
	•	7000,4000 → 8200,4000

Bedrooms:
	•	2000,7500 → 3500,7500
	•	5000,7500 → 6500,7500

Master:
	•	11000,7800 → 12800,7800

⸻

🔷 Clean Openings
	•	Use Trim to remove wall behind windows

⸻

✂️ 7. CLEAN THE PLAN (VERY IMPORTANT)

Use:
	•	Trim
	•	Auto Trim

👉 Remove:
	•	Wall overlaps
	•	Extra intersections

⸻

📝 8. ADD ROOM LABELS

Switch to: A-TEXT

Use: Draw → Text

Example:

LIVING ROOM
6000 x 4500

Place in each room.

⸻

📏 9. ADD DIMENSIONS

Switch to: A-DIMS

Use: Dimension → Horizontal / Vertical

⸻

🔷 Add:

Overall:
	•	14000 (length)
	•	8500 (width)

Internal:
	•	3000 / 6000 / 9000 spacing
	•	Room sizes

⸻

🧱 10. HATCH WALLS (OPTIONAL BUT PROFESSIONAL)
	•	Select: Hatch
	•	Pattern: ANSI31
	•	Apply to wall areas

⸻

🖨️ 11. PRINT SETUP (CRUCIAL)

🔷 Go to:

File → Print Preview

⸻

🔷 Settings:
	•	Scale: 1:100
	•	Paper: A2 (recommended)

⸻

🔷 Adjust:
	•	Center drawing
	•	Fit margins

⸻

🧠 FINAL RESULT

You now have:

✅ A real architectural plan
✅ Correct wall thickness
✅ Doors + windows
✅ Dimensions
✅ Print-ready drawing

⸻

⚠️ COMMON MISTAKES (AVOID THESE)
	•	❌ Drawing without layers
	•	❌ Not trimming wall openings
	•	❌ Wrong units (must be mm)
	•	❌ Printing without scale

