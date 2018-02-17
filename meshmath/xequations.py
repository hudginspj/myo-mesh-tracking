import math

#d0, d1, s0, s1
readings = [
    [1.0, 2.0, 3.0, 2.0],
    [1.0, 2.0, 3.0, 2.0]
]



# [d0, s0, k]
# calibrations = [
#     [1.0, 2.0, 3.0],
#     [1.0, 2.0, 3.0]
# ]



def compute_k(d0, d1, s0, s1):
    return (s0-s1)/math.log10(d1/d0)

def calibrate(cal_readings):
    cals = []
    for (d0, d1, s0, s1) in readings:
        k = compute_k(d0, d1, s0, s1)
        cals.append([d0, s0, k])
    return cals

calibrations = calibrate(readings)

def distance(node_index, s):
    (d0, s0, k) = calibrations[node_index]
    print('d0/s0/k', d0, s0, k)
    return d0 * math.pow(10, (s0 - s) / k)


print(calibrations)
print(distance(1, -8))







