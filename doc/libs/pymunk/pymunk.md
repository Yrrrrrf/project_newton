# [Pymunk](http://www.pymunk.org/en/latest/)

Is a easy-to-use pythonic 2d physics library that can be used whenever you need 2d rigid body physics from Python. Perfect when you need 2d physics in your game, demo or other application! It is built on top of the very capable 2d physics library Chipmunk.

## Installation
```bash
pip install pymunk
```

## Usage
```python
import pymunk


space = pymunk.Space()  # Create a Space which contain the simulation
space.gravity = 0, -1000  # Set its gravity

body = pymunk.Body(1, 1666)  # Create a Body with mass and moment
body.position = 50, 100  # Set the position of the body

poly = pymunk.Poly.create_box(body)  # Create a box shape and attach to body
space.add(body, poly)  # Add both body and shape to the simulation

while True:  # Infinite loop simulation
    space.step(0.02)  # Step the simulation one step forward
    print(body.position)  # Print the body's position
```

## Examples
```bash
python -m pymunk.examples -l  # List all examples
python -m pymunk.examples.tank  # Run a specific example
```


## Documentation
- [Pymunk](http://www.pymunk.org/en/latest/)
- -> [Chipmunk](https://chipmunk-physics.net/release/ChipmunkLatest-Docs/)