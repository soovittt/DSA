# B-Tree (Degree t)

- Nodes store multiple keys/children; balanced by design with all leaves same depth.
- Insert: split full child, promote median, then descend.
- Great for disk-based indexes due to high branching factor.
