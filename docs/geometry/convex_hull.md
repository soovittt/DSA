# Convex Hull (Monotone Chain)

- Sort unique points; build lower and upper hulls via cross-product orientation.
- Pop last point when it would create a non-left turn (<= 0 cross).
- Complexity: O(n log n) due to sorting; O(n) hull construction.
