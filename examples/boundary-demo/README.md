# Boundary demo

A silent, all-English teaching example. A fixed circle's top point becomes interior to a neighboring disk when radii increase to the right. A fixed magnified panel shows the old point, followed by the local envelope and its outward direction.

With Python and the platform dependencies for Manim CE installed:

```sh
python -m pip install -r examples/boundary-demo/requirements.txt
python -m manim -qm --fps 30 examples/boundary-demo/scene.py BoundaryDemo
```

This uses Arial through Pango and no LaTeX objects. Use an installed replacement font if Arial is unavailable. Output goes to Manim's `media/` folder. The scene reads `timings.json` next to its source. It has no audio; the timing is adapted from the development prototype. This packaged version has a final-frame smoke check, not a fresh full audiovisual validation.

The continuous family has centers `(u, 0)` and radii `0.4 + g*u`, with `u` between -1 and 1. The gradient moves from 0 to 0.3. Only selected disks are shown. The local upper envelope has normal `(-g, sqrt(1-g*g))`; endpoint caps are omitted. Allowed regions are not probability distributions.

This example tests retained references, linked geometry, local magnification and traceable contributions. It is not a proof or a simulation of a particular scientific paper.
