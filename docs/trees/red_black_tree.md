# Red-Black Tree

- Properties: root black; red has black children; equal black-height on all root-to-leaf paths.
- Insert fixup cases: recolor with red uncle; rotate when triangle/line forms (LL/LR/RL/RR).
- Guarantees O(log n) height with simple local fixups.
