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


def find_intersection(point1, point2, point3, point4):
    """
    # 示例调用
    point1 = (1, 2)
    point2 = (3, 2)
    point3 = (5, 6)
    point4 = (7, 8)
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    # 计算直线1的斜率
    m1 = (y2 - y1) / (x2 - x1) if x1 != x2 else float("inf")

    # 计算直线2的斜率
    m2 = (y4 - y3) / (x4 - x3) if x3 != x4 else float("inf")

    # 如果两条直线平行，则没有交点
    if m1 == m2:
        return None

    # 计算交点的x坐标
    x_intersect = (y3 - y1 + m1 * x1 - m2 * x3) / (m1 - m2)

    # 计算交点的y坐标
    y_intersect = m1 * (x_intersect - x1) + y1

    return (x_intersect, y_intersect)
