# FLL-evicka

## Project Structure
```
.
├── LICENSE
├── pyhon
│   ├── evicka.py
│   └── main.py
├── 'language name'
│   ├── evicka.x  program containing functions
│   ├── pathn.x   program containing path or
│   └── main.x    program containing every path
└── README.md
```
## Python
Version: `pybricks-micropython` <br>
Packages: `pybricks` <br>
Structure: 
```
.
├── evicka.py  functions to simplify programming of robot 
└── main.py    contains robot game paths
```

### Evicka module
#### To use this module:
  * Put `evicka.py` into your project folder
  * Put `import evicka` to file, where you wish to use this module
  
#### This module contains:
  * `reset()` - resets angle of gyroscope and motors
  * `mov(speed, time)` - moves robot for *time* seconds in *speed* speed, uses gyroscope
  * `rot(speed, angle)` - rotates robot to *angle* degrees and in *speed* speed, uses gyroscope
  * `stick(speed, angle)` - moves *stick module* to desired height using *angle* degrees and *speed* speed
  * `claw(speed, angle)` - opens or closes *claw module* using *angle* degrees and *speed* speed
  
#### Where to connect sensors and motors?
  * Left large servo motor - Port B - `left`
  * Right large servo motor - Port C - `right`
  * Left medium servo motor - Port D - `sLeft`
  * Right medium servo motor - Port A - `sRight`
  * Gyro sensor - Port S1 - `gyro`
