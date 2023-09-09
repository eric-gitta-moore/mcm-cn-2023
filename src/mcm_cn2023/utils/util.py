import numpy as np
import sympy


def 计算两平面夹角(plane0: sympy.Plane, plane1: sympy.Plane, is_use_deg=False):
    v0 = np.array(plane0.normal_vector).astype(float)
    v1 = np.array(plane1.normal_vector).astype(float)
    return 计算两向量夹角(v0, v1, is_use_deg)


def 计算两向量夹角(v0: np.ndarray, v1: np.ndarray, is_use_deg=False):
    dot_product = np.dot(v0, v1)
    v0_len = np.linalg.norm(v0)
    v1_len = np.linalg.norm(v1)
    try:
        angle_rad = np.arccos(dot_product / (v0_len * v1_len))
    except ZeroDivisionError as error:
        raise ZeroDivisionError("{}".format(error))

    if is_use_deg:
        return np.rad2deg(angle_rad)
    return angle_rad


def nm2m(海里):
    return 海里 * 1852


def m2nm(m):
    return m / 1852
