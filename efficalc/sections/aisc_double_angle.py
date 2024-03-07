import dataclasses


@dataclasses.dataclass
class DoubleAngle(object):
    """This is a dataclass containing the properties of an AISC Double Angle section. Properties follow the AISC shapes
    database.

    :param A: Cross-sectional area (in^2)
    :type A: float
    :param AISC_name: The name of the AISC section
    :type AISC_name: str
    :param EDI_Std_Nomenclature: The EDI standard nomenclature name
    :type EDI_Std_Nomenclature: str
    :param H: Flexural constant
    :type H: float
    :param Ix: Moment of inertia about the x-axis (in^4)
    :type Ix: float
    :param Iy: Moment of inertia about the y-axis (in^4)
    :type Iy: float
    :param Sx: Elastic section modulus about the x-axis (in^3)
    :type Sx: float
    :param Sy: Elastic section modulus about the y-axis (in^3)
    :type Sy: float
    :param T_F: Whether the section has an additional note in the AISC shapes database (T or F)
    :type T_F: str
    :param Type: The section type
    :type Type: str
    :param W: Nominal weight (lb/ft)
    :type W: float
    :param Zx: Plastic section modulus about the x-axis (in^3)
    :type Zx: float
    :param Zy: Plastic section modulus about the y-axis (in^3)
    :type Zy: float
    :param b: Width of the flat wall of the longer legs for back-to-back angles (in)
    :type b: float
    :param b_t: Slenderness ratio for channel flange, b/t
    :type b_t: float
    :param d: Overall depth of member, or width of shorter leg for angles (in)
    :type d: float
    :param ro: Polar radius of gyration about the shear center (in)
    :type ro: float
    :param rx: Radius of gyration about the x-axis (in)
    :type rx: float
    :param ry: Radius of gyration about the y-axis (with no separation for double angles back-to-back) (in)
    :type ry: float
    :param t: Thickness of angle leg (in)
    :type t: float
    :param y: Vertical distance from designated edge of member to center of gravity of member (in)
    :type y: float
    :param yp: Vertical distance from designated edge of member to plastic neutral axis of member (in)
    :type yp: float
    """

    A: float
    AISC_name: str
    EDI_Std_Nomenclature: str
    H: float
    Ix: float
    Iy: float
    Sx: float
    Sy: float
    T_F: str
    Type: str
    W: float
    Zx: float
    Zy: float
    b: float
    b_t: float
    d: float
    ro: float
    rx: float
    ry: float
    t: float
    y: float
    yp: float


ALL_AISC_DOUBLE_ANGLE_NAMES = (
    "2L12X12X1-3/8X3/4",
    "2L12X12X1-3/8",
    "2L12X12X1-1/4X3/4",
    "2L12X12X1-1/4",
    "2L12X12X1-1/8",
    "2L12X12X1-1/4X1-1/2",
    "2L12X12X1",
    "2L12X12X1-1/8X3/4",
    "2L12X12X1-1/8X1-1/2",
    "2L10X10X1-3/8",
    "2L12X12X1X3/4",
    "2L10X10X1-3/8X1-1/2",
    "2L10X10X1-3/8X3/4",
    "2L10X10X1-1/4X1-1/2",
    "2L10X10X1-1/4",
    "2L12X12X1X1-1/2",
    "2L10X10X1-1/4X3/4",
    "2L10X10X1-1/8X1-1/2",
    "2L10X10X1-1/8",
    "2L10X10X1-1/8X3/4",
    "2L12X12X1-3/8X1-1/2",
    "2L10X10X1X1-1/2",
    "2L10X10X7/8X3/4",
    "2L10X10X1",
    "2L10X10X7/8",
    "2L10X10X1X3/4",
    "2L10X10X3/4X3/4",
    "2L10X10X3/4",
    "2L10X10X7/8X1-1/2",
    "2L10X10X3/4X1-1/2",
    "2L8X8X1-1/8",
    "2L8X8X1-1/8X3/8",
    "2L8X8X1-1/8X3/4",
    "2L8X8X1",
    "2L8X8X1X3/8",
    "2L8X8X1X3/4",
    "2L8X8X7/8X3/8",
    "2L8X8X7/8",
    "2L8X8X7/8X3/4",
    "2L8X8X3/4X3/8",
    "2L8X8X3/4",
    "2L8X8X5/8",
    "2L8X8X5/8X3/8",
    "2L8X8X5/8X3/4",
    "2L8X8X9/16",
    "2L8X8X9/16X3/8",
    "2L8X8X9/16X3/4",
    "2L8X8X1/2",
    "2L8X8X1/2X3/8",
    "2L8X8X1/2X3/4",
    "2L6X6X1",
    "2L6X6X1X3/8",
    "2L6X6X1X3/4",
    "2L6X6X7/8",
    "2L6X6X7/8X3/8",
    "2L6X6X7/8X3/4",
    "2L6X6X3/4",
    "2L6X6X3/4X3/8",
    "2L8X8X3/4X3/4",
    "2L6X6X3/4X3/4",
    "2L6X6X5/8",
    "2L6X6X5/8X3/8",
    "2L6X6X5/8X3/4",
    "2L6X6X9/16",
    "2L6X6X9/16X3/8",
    "2L6X6X9/16X3/4",
    "2L6X6X1/2X3/8",
    "2L6X6X1/2",
    "2L6X6X1/2X3/4",
    "2L6X6X7/16",
    "2L6X6X7/16X3/8",
    "2L6X6X7/16X3/4",
    "2L6X6X3/8",
    "2L6X6X3/8X3/8",
    "2L6X6X5/16",
    "2L6X6X3/8X3/4",
    "2L5X5X7/8",
    "2L5X5X7/8X3/4",
    "2L6X6X5/16X3/4",
    "2L5X5X3/4",
    "2L5X5X3/4X3/8",
    "2L6X6X5/16X3/8",
    "2L5X5X7/8X3/8",
    "2L5X5X3/4X3/4",
    "2L5X5X5/8",
    "2L5X5X5/8X3/8",
    "2L5X5X1/2",
    "2L5X5X5/8X3/4",
    "2L5X5X1/2X3/8",
    "2L5X5X1/2X3/4",
    "2L5X5X7/16",
    "2L5X5X7/16X3/8",
    "2L5X5X7/16X3/4",
    "2L5X5X3/8",
    "2L5X5X3/8X3/8",
    "2L5X5X3/8X3/4",
    "2L5X5X5/16",
    "2L5X5X5/16X3/8",
    "2L4X4X3/4",
    "2L4X4X3/4X3/4",
    "2L4X4X3/4X3/8",
    "2L4X4X5/8",
    "2L4X4X5/8X3/4",
    "2L4X4X5/8X3/8",
    "2L5X5X5/16X3/4",
    "2L4X4X1/2",
    "2L4X4X1/2X3/8",
    "2L4X4X7/16",
    "2L4X4X1/2X3/4",
    "2L4X4X7/16X3/4",
    "2L4X4X7/16X3/8",
    "2L4X4X3/8X3/4",
    "2L4X4X5/16",
    "2L4X4X3/8X3/8",
    "2L4X4X3/8",
    "2L4X4X5/16X3/4",
    "2L4X4X5/16X3/8",
    "2L4X4X1/4",
    "2L4X4X1/4X3/8",
    "2L4X4X1/4X3/4",
    "2L3-1/2X3-1/2X1/2",
    "2L3-1/2X3-1/2X1/2X3/8",
    "2L3-1/2X3-1/2X1/2X3/4",
    "2L3-1/2X3-1/2X7/16",
    "2L3-1/2X3-1/2X7/16X3/8",
    "2L3-1/2X3-1/2X7/16X3/4",
    "2L3-1/2X3-1/2X3/8",
    "2L3-1/2X3-1/2X3/8X3/8",
    "2L3-1/2X3-1/2X3/8X3/4",
    "2L3-1/2X3-1/2X5/16",
    "2L3-1/2X3-1/2X5/16X3/8",
    "2L3-1/2X3-1/2X5/16X3/4",
    "2L3-1/2X3-1/2X1/4X3/8",
    "2L3-1/2X3-1/2X1/4",
    "2L3-1/2X3-1/2X1/4X3/4",
    "2L3X3X1/2",
    "2L3X3X1/2X3/8",
    "2L3X3X1/2X3/4",
    "2L3X3X7/16",
    "2L3X3X7/16X3/8",
    "2L3X3X7/16X3/4",
    "2L3X3X3/8",
    "2L3X3X5/16X3/8",
    "2L3X3X5/16",
    "2L3X3X3/8X3/4",
    "2L3X3X3/8X3/8",
    "2L3X3X1/4X3/8",
    "2L3X3X1/4X3/4",
    "2L3X3X1/4",
    "2L3X3X5/16X3/4",
    "2L3X3X3/16X3/4",
    "2L3X3X3/16",
    "2L2-1/2X2-1/2X1/2",
    "2L2-1/2X2-1/2X1/2X3/8",
    "2L2-1/2X2-1/2X1/2X3/4",
    "2L2-1/2X2-1/2X3/8",
    "2L3X3X3/16X3/8",
    "2L2-1/2X2-1/2X3/8X3/4",
    "2L2-1/2X2-1/2X5/16",
    "2L2-1/2X2-1/2X3/8X3/8",
    "2L2-1/2X2-1/2X5/16X3/8",
    "2L2-1/2X2-1/2X5/16X3/4",
    "2L2-1/2X2-1/2X1/4",
    "2L2-1/2X2-1/2X1/4X3/8",
    "2L2-1/2X2-1/2X3/16",
    "2L2-1/2X2-1/2X3/16X3/8",
    "2L2-1/2X2-1/2X1/4X3/4",
    "2L2-1/2X2-1/2X3/16X3/4",
    "2L2X2X3/8",
    "2L2X2X3/8X3/8",
    "2L2X2X3/8X3/4",
    "2L2X2X5/16",
    "2L2X2X5/16X3/8",
    "2L2X2X5/16X3/4",
    "2L2X2X1/4",
    "2L2X2X1/4X3/8",
    "2L2X2X3/16",
    "2L2X2X1/4X3/4",
    "2L2X2X3/16X3/8",
    "2L2X2X3/16X3/4",
    "2L2X2X1/8",
    "2L2X2X1/8X3/8",
    "2L2X2X1/8X3/4",
    "2L8X6X1LLBB",
    "2L8X6X1X3/8LLBB",
    "2L8X6X1X3/4LLBB",
    "2L8X6X7/8LLBB",
    "2L8X6X7/8X3/8LLBB",
    "2L8X6X7/8X3/4LLBB",
    "2L8X6X3/4LLBB",
    "2L8X6X3/4X3/8LLBB",
    "2L8X6X3/4X3/4LLBB",
    "2L8X6X5/8X3/8LLBB",
    "2L8X6X5/8LLBB",
    "2L8X6X5/8X3/4LLBB",
    "2L8X6X9/16LLBB",
    "2L8X6X9/16X3/8LLBB",
    "2L8X6X9/16X3/4LLBB",
    "2L8X6X1/2LLBB",
    "2L8X6X1/2X3/8LLBB",
    "2L8X6X1/2X3/4LLBB",
    "2L8X6X7/16X3/8LLBB",
    "2L8X6X7/16LLBB",
    "2L8X6X7/16X3/4LLBB",
    "2L8X4X1X3/8LLBB",
    "2L8X4X1LLBB",
    "2L8X4X1X3/4LLBB",
    "2L8X4X7/8LLBB",
    "2L8X4X7/8X3/8LLBB",
    "2L8X4X3/4LLBB",
    "2L8X4X7/8X3/4LLBB",
    "2L8X4X3/4X3/8LLBB",
    "2L8X4X3/4X3/4LLBB",
    "2L8X4X5/8LLBB",
    "2L8X4X5/8X3/8LLBB",
    "2L8X4X5/8X3/4LLBB",
    "2L8X4X9/16LLBB",
    "2L8X4X9/16X3/8LLBB",
    "2L8X4X9/16X3/4LLBB",
    "2L8X4X1/2LLBB",
    "2L8X4X1/2X3/8LLBB",
    "2L8X4X1/2X3/4LLBB",
    "2L8X4X7/16LLBB",
    "2L8X4X7/16X3/8LLBB",
    "2L8X4X7/16X3/4LLBB",
    "2L7X4X3/4LLBB",
    "2L7X4X3/4X3/8LLBB",
    "2L7X4X5/8LLBB",
    "2L7X4X3/4X3/4LLBB",
    "2L7X4X5/8X3/8LLBB",
    "2L7X4X5/8X3/4LLBB",
    "2L7X4X1/2LLBB",
    "2L7X4X1/2X3/8LLBB",
    "2L7X4X1/2X3/4LLBB",
    "2L7X4X7/16LLBB",
    "2L7X4X7/16X3/8LLBB",
    "2L7X4X7/16X3/4LLBB",
    "2L7X4X3/8LLBB",
    "2L7X4X3/8X3/8LLBB",
    "2L6X4X7/8LLBB",
    "2L7X4X3/8X3/4LLBB",
    "2L6X4X7/8X3/8LLBB",
    "2L6X4X7/8X3/4LLBB",
    "2L6X4X3/4LLBB",
    "2L6X4X3/4X3/8LLBB",
    "2L6X4X3/4X3/4LLBB",
    "2L6X4X5/8LLBB",
    "2L6X4X5/8X3/8LLBB",
    "2L6X4X5/8X3/4LLBB",
    "2L6X4X9/16X3/8LLBB",
    "2L6X4X9/16LLBB",
    "2L6X4X1/2LLBB",
    "2L6X4X1/2X3/4LLBB",
    "2L6X4X1/2X3/8LLBB",
    "2L6X4X9/16X3/4LLBB",
    "2L6X4X7/16X3/8LLBB",
    "2L6X4X7/16LLBB",
    "2L6X4X3/8LLBB",
    "2L6X4X7/16X3/4LLBB",
    "2L6X4X5/16X3/4LLBB",
    "2L6X3-1/2X1/2LLBB",
    "2L6X4X5/16X3/8LLBB",
    "2L6X4X3/8X3/4LLBB",
    "2L6X4X5/16LLBB",
    "2L6X4X3/8X3/8LLBB",
    "2L6X3-1/2X1/2X3/8LLBB",
    "2L6X3-1/2X1/2X3/4LLBB",
    "2L6X3-1/2X3/8LLBB",
    "2L6X3-1/2X5/16LLBB",
    "2L6X3-1/2X3/8X3/8LLBB",
    "2L6X3-1/2X3/8X3/4LLBB",
    "2L5X3-1/2X3/4X3/4LLBB",
    "2L5X3-1/2X3/8X3/8LLBB",
    "2L5X3-1/2X5/8LLBB",
    "2L5X3-1/2X5/8X3/4LLBB",
    "2L5X3-1/2X3/8X3/4LLBB",
    "2L5X3-1/2X5/16LLBB",
    "2L5X3-1/2X1/2X3/4LLBB",
    "2L5X3-1/2X5/8X3/8LLBB",
    "2L5X3-1/2X5/16X3/8LLBB",
    "2L6X3-1/2X5/16X3/4LLBB",
    "2L5X3-1/2X3/8LLBB",
    "2L5X3-1/2X3/4LLBB",
    "2L5X3-1/2X1/2LLBB",
    "2L6X3-1/2X5/16X3/8LLBB",
    "2L5X3-1/2X3/4X3/8LLBB",
    "2L5X3-1/2X5/16X3/4LLBB",
    "2L5X3-1/2X1/4LLBB",
    "2L5X3-1/2X1/4X3/8LLBB",
    "2L5X3-1/2X1/2X3/8LLBB",
    "2L5X3-1/2X1/4X3/4LLBB",
    "2L5X3X1/2LLBB",
    "2L5X3X1/2X3/8LLBB",
    "2L5X3X1/2X3/4LLBB",
    "2L5X3X7/16LLBB",
    "2L5X3X7/16X3/8LLBB",
    "2L5X3X3/8LLBB",
    "2L5X3X7/16X3/4LLBB",
    "2L5X3X3/8X3/4LLBB",
    "2L5X3X3/8X3/8LLBB",
    "2L5X3X5/16X3/4LLBB",
    "2L5X3X1/4X3/8LLBB",
    "2L5X3X5/16X3/8LLBB",
    "2L5X3X1/4LLBB",
    "2L5X3X5/16LLBB",
    "2L5X3X1/4X3/4LLBB",
    "2L4X3-1/2X1/2LLBB",
    "2L4X3-1/2X1/2X3/8LLBB",
    "2L4X3-1/2X1/2X3/4LLBB",
    "2L4X3-1/2X3/8LLBB",
    "2L4X3-1/2X3/8X3/8LLBB",
    "2L4X3-1/2X5/16LLBB",
    "2L4X3-1/2X5/16X3/4LLBB",
    "2L4X3-1/2X5/16X3/8LLBB",
    "2L4X3-1/2X1/4LLBB",
    "2L4X3-1/2X1/4X3/8LLBB",
    "2L4X3-1/2X1/4X3/4LLBB",
    "2L4X3-1/2X3/8X3/4LLBB",
    "2L4X3X5/8X3/8LLBB",
    "2L4X3X5/8LLBB",
    "2L4X3X5/8X3/4LLBB",
    "2L4X3X1/2LLBB",
    "2L4X3X1/2X3/8LLBB",
    "2L4X3X1/2X3/4LLBB",
    "2L4X3X3/8LLBB",
    "2L4X3X3/8X3/8LLBB",
    "2L4X3X3/8X3/4LLBB",
    "2L4X3X5/16LLBB",
    "2L4X3X5/16X3/8LLBB",
    "2L4X3X5/16X3/4LLBB",
    "2L4X3X1/4LLBB",
    "2L4X3X1/4X3/8LLBB",
    "2L4X3X1/4X3/4LLBB",
    "2L3-1/2X3X1/2LLBB",
    "2L3-1/2X3X1/2X3/8LLBB",
    "2L3-1/2X3X7/16LLBB",
    "2L3-1/2X3X1/2X3/4LLBB",
    "2L3-1/2X3X7/16X3/8LLBB",
    "2L3-1/2X3X7/16X3/4LLBB",
    "2L3-1/2X3X3/8LLBB",
    "2L3-1/2X3X3/8X3/8LLBB",
    "2L3-1/2X3X5/16LLBB",
    "2L3-1/2X3X3/8X3/4LLBB",
    "2L3-1/2X3X5/16X3/8LLBB",
    "2L3-1/2X3X1/4LLBB",
    "2L3-1/2X3X1/4X3/4LLBB",
    "2L3-1/2X3X5/16X3/4LLBB",
    "2L3-1/2X3X1/4X3/8LLBB",
    "2L3-1/2X2-1/2X1/2LLBB",
    "2L3-1/2X2-1/2X1/2X3/8LLBB",
    "2L3-1/2X2-1/2X1/2X3/4LLBB",
    "2L3-1/2X2-1/2X3/8X3/8LLBB",
    "2L3-1/2X2-1/2X3/8X3/4LLBB",
    "2L3-1/2X2-1/2X3/8LLBB",
    "2L3-1/2X2-1/2X5/16X3/8LLBB",
    "2L3-1/2X2-1/2X5/16LLBB",
    "2L3-1/2X2-1/2X1/4LLBB",
    "2L3-1/2X2-1/2X5/16X3/4LLBB",
    "2L3-1/2X2-1/2X1/4X3/8LLBB",
    "2L3-1/2X2-1/2X1/4X3/4LLBB",
    "2L3X2-1/2X1/2LLBB",
    "2L3X2-1/2X1/2X3/8LLBB",
    "2L3X2-1/2X7/16LLBB",
    "2L3X2-1/2X1/2X3/4LLBB",
    "2L3X2-1/2X7/16X3/8LLBB",
    "2L3X2-1/2X7/16X3/4LLBB",
    "2L3X2-1/2X3/8LLBB",
    "2L3X2-1/2X3/8X3/8LLBB",
    "2L3X2-1/2X3/8X3/4LLBB",
    "2L3X2-1/2X5/16LLBB",
    "2L3X2-1/2X5/16X3/4LLBB",
    "2L3X2-1/2X5/16X3/8LLBB",
    "2L3X2-1/2X1/4X3/8LLBB",
    "2L3X2-1/2X1/4X3/4LLBB",
    "2L3X2-1/2X1/4LLBB",
    "2L3X2-1/2X3/16LLBB",
    "2L3X2-1/2X3/16X3/4LLBB",
    "2L3X2-1/2X3/16X3/8LLBB",
    "2L3X2X1/2LLBB",
    "2L3X2X1/2X3/8LLBB",
    "2L3X2X1/2X3/4LLBB",
    "2L3X2X3/8LLBB",
    "2L3X2X3/8X3/8LLBB",
    "2L3X2X3/8X3/4LLBB",
    "2L3X2X5/16LLBB",
    "2L3X2X5/16X3/8LLBB",
    "2L3X2X1/4LLBB",
    "2L3X2X5/16X3/4LLBB",
    "2L3X2X1/4X3/8LLBB",
    "2L3X2X1/4X3/4LLBB",
    "2L3X2X3/16X3/8LLBB",
    "2L3X2X3/16LLBB",
    "2L3X2X3/16X3/4LLBB",
    "2L2-1/2X2X3/8LLBB",
    "2L2-1/2X2X3/8X3/4LLBB",
    "2L2-1/2X2X5/16LLBB",
    "2L2-1/2X2X3/8X3/8LLBB",
    "2L2-1/2X2X5/16X3/8LLBB",
    "2L2-1/2X2X1/4LLBB",
    "2L2-1/2X2X5/16X3/4LLBB",
    "2L2-1/2X2X1/4X3/8LLBB",
    "2L2-1/2X2X1/4X3/4LLBB",
    "2L2-1/2X2X3/16LLBB",
    "2L2-1/2X2X3/16X3/4LLBB",
    "2L2-1/2X2X3/16X3/8LLBB",
    "2L2-1/2X1-1/2X1/4X3/8LLBB",
    "2L2-1/2X1-1/2X1/4LLBB",
    "2L2-1/2X1-1/2X1/4X3/4LLBB",
    "2L2-1/2X1-1/2X3/16LLBB",
    "2L2-1/2X1-1/2X3/16X3/8LLBB",
    "2L2-1/2X1-1/2X3/16X3/4LLBB",
    "2L8X6X1SLBB",
    "2L8X6X1X3/8SLBB",
    "2L8X6X1X3/4SLBB",
    "2L8X6X7/8SLBB",
    "2L8X6X7/8X3/8SLBB",
    "2L8X6X7/8X3/4SLBB",
    "2L8X6X3/4SLBB",
    "2L8X6X3/4X3/8SLBB",
    "2L8X6X3/4X3/4SLBB",
    "2L8X6X5/8X3/8SLBB",
    "2L8X6X5/8SLBB",
    "2L8X6X5/8X3/4SLBB",
    "2L8X6X9/16SLBB",
    "2L8X6X9/16X3/8SLBB",
    "2L8X6X9/16X3/4SLBB",
    "2L8X6X1/2X3/8SLBB",
    "2L8X6X1/2SLBB",
    "2L8X6X1/2X3/4SLBB",
    "2L8X6X7/16SLBB",
    "2L8X6X7/16X3/8SLBB",
    "2L8X4X1SLBB",
    "2L8X4X1X3/8SLBB",
    "2L8X6X7/16X3/4SLBB",
    "2L8X4X1X3/4SLBB",
    "2L8X4X7/8X3/8SLBB",
    "2L8X4X7/8SLBB",
    "2L8X4X7/8X3/4SLBB",
    "2L8X4X3/4X3/4SLBB",
    "2L8X4X3/4SLBB",
    "2L8X4X3/4X3/8SLBB",
    "2L8X4X5/8SLBB",
    "2L8X4X5/8X3/8SLBB",
    "2L8X4X5/8X3/4SLBB",
    "2L8X4X9/16SLBB",
    "2L8X4X9/16X3/8SLBB",
    "2L8X4X9/16X3/4SLBB",
    "2L8X4X1/2SLBB",
    "2L8X4X1/2X3/8SLBB",
    "2L8X4X1/2X3/4SLBB",
    "2L8X4X7/16X3/8SLBB",
    "2L8X4X7/16SLBB",
    "2L8X4X7/16X3/4SLBB",
    "2L7X4X3/4SLBB",
    "2L7X4X3/4X3/8SLBB",
    "2L7X4X3/4X3/4SLBB",
    "2L7X4X5/8X3/8SLBB",
    "2L7X4X5/8SLBB",
    "2L7X4X5/8X3/4SLBB",
    "2L7X4X1/2SLBB",
    "2L7X4X1/2X3/4SLBB",
    "2L7X4X1/2X3/8SLBB",
    "2L7X4X7/16SLBB",
    "2L7X4X7/16X3/8SLBB",
    "2L7X4X7/16X3/4SLBB",
    "2L7X4X3/8X3/8SLBB",
    "2L7X4X3/8SLBB",
    "2L6X4X7/8SLBB",
    "2L7X4X3/8X3/4SLBB",
    "2L6X4X7/8X3/4SLBB",
    "2L6X4X3/4X3/8SLBB",
    "2L6X4X7/8X3/8SLBB",
    "2L6X4X3/4SLBB",
    "2L6X4X3/4X3/4SLBB",
    "2L6X4X5/8SLBB",
    "2L6X4X5/8X3/4SLBB",
    "2L6X4X5/8X3/8SLBB",
    "2L6X4X9/16SLBB",
    "2L6X4X9/16X3/8SLBB",
    "2L6X4X9/16X3/4SLBB",
    "2L6X4X1/2SLBB",
    "2L6X4X1/2X3/8SLBB",
    "2L6X4X7/16SLBB",
    "2L6X4X1/2X3/4SLBB",
    "2L6X4X7/16X3/8SLBB",
    "2L6X4X7/16X3/4SLBB",
    "2L6X4X3/8SLBB",
    "2L6X4X3/8X3/4SLBB",
    "2L6X4X5/16SLBB",
    "2L6X4X5/16X3/8SLBB",
    "2L6X4X3/8X3/8SLBB",
    "2L6X4X5/16X3/4SLBB",
    "2L6X3-1/2X1/2SLBB",
    "2L6X3-1/2X1/2X3/8SLBB",
    "2L6X3-1/2X1/2X3/4SLBB",
    "2L6X3-1/2X3/8SLBB",
    "2L6X3-1/2X3/8X3/8SLBB",
    "2L6X3-1/2X3/8X3/4SLBB",
    "2L6X3-1/2X5/16SLBB",
    "2L6X3-1/2X5/16X3/4SLBB",
    "2L6X3-1/2X5/16X3/8SLBB",
    "2L5X3-1/2X3/4SLBB",
    "2L5X3-1/2X3/4X3/8SLBB",
    "2L5X3-1/2X3/4X3/4SLBB",
    "2L5X3-1/2X5/8SLBB",
    "2L5X3-1/2X5/8X3/8SLBB",
    "2L5X3-1/2X5/8X3/4SLBB",
    "2L5X3-1/2X1/2SLBB",
    "2L5X3-1/2X1/2X3/8SLBB",
    "2L5X3-1/2X1/2X3/4SLBB",
    "2L5X3-1/2X3/8SLBB",
    "2L5X3-1/2X3/8X3/8SLBB",
    "2L5X3-1/2X3/8X3/4SLBB",
    "2L5X3-1/2X5/16SLBB",
    "2L5X3-1/2X5/16X3/8SLBB",
    "2L5X3-1/2X5/16X3/4SLBB",
    "2L5X3-1/2X1/4SLBB",
    "2L5X3-1/2X1/4X3/8SLBB",
    "2L5X3-1/2X1/4X3/4SLBB",
    "2L5X3X1/2SLBB",
    "2L5X3X1/2X3/8SLBB",
    "2L5X3X7/16SLBB",
    "2L5X3X1/2X3/4SLBB",
    "2L5X3X7/16X3/4SLBB",
    "2L5X3X3/8SLBB",
    "2L5X3X7/16X3/8SLBB",
    "2L5X3X3/8X3/8SLBB",
    "2L5X3X3/8X3/4SLBB",
    "2L5X3X5/16SLBB",
    "2L5X3X5/16X3/8SLBB",
    "2L5X3X5/16X3/4SLBB",
    "2L5X3X1/4SLBB",
    "2L5X3X1/4X3/8SLBB",
    "2L4X3-1/2X1/2SLBB",
    "2L5X3X1/4X3/4SLBB",
    "2L4X3-1/2X1/2X3/8SLBB",
    "2L4X3-1/2X1/2X3/4SLBB",
    "2L4X3-1/2X3/8X3/8SLBB",
    "2L4X3-1/2X3/8SLBB",
    "2L4X3-1/2X3/8X3/4SLBB",
    "2L4X3-1/2X5/16SLBB",
    "2L4X3-1/2X5/16X3/8SLBB",
    "2L4X3-1/2X1/4SLBB",
    "2L4X3-1/2X5/16X3/4SLBB",
    "2L4X3-1/2X1/4X3/8SLBB",
    "2L4X3-1/2X1/4X3/4SLBB",
    "2L4X3X5/8SLBB",
    "2L4X3X5/8X3/8SLBB",
    "2L4X3X5/8X3/4SLBB",
    "2L4X3X1/2SLBB",
    "2L4X3X1/2X3/8SLBB",
    "2L4X3X1/2X3/4SLBB",
    "2L4X3X3/8X3/8SLBB",
    "2L4X3X3/8SLBB",
    "2L4X3X3/8X3/4SLBB",
    "2L4X3X5/16SLBB",
    "2L4X3X5/16X3/8SLBB",
    "2L4X3X1/4SLBB",
    "2L4X3X5/16X3/4SLBB",
    "2L4X3X1/4X3/8SLBB",
    "2L4X3X1/4X3/4SLBB",
    "2L3-1/2X3X1/2SLBB",
    "2L3-1/2X3X1/2X3/8SLBB",
    "2L3-1/2X3X1/2X3/4SLBB",
    "2L3-1/2X3X7/16SLBB",
    "2L3-1/2X3X7/16X3/8SLBB",
    "2L3-1/2X3X7/16X3/4SLBB",
    "2L3-1/2X3X3/8SLBB",
    "2L3-1/2X3X3/8X3/8SLBB",
    "2L3-1/2X3X3/8X3/4SLBB",
    "2L3-1/2X3X5/16SLBB",
    "2L3-1/2X3X5/16X3/8SLBB",
    "2L3-1/2X3X5/16X3/4SLBB",
    "2L3-1/2X3X1/4SLBB",
    "2L3-1/2X3X1/4X3/8SLBB",
    "2L3-1/2X3X1/4X3/4SLBB",
    "2L3-1/2X2-1/2X1/2SLBB",
    "2L3-1/2X2-1/2X1/2X3/8SLBB",
    "2L3-1/2X2-1/2X1/2X3/4SLBB",
    "2L3-1/2X2-1/2X3/8SLBB",
    "2L3-1/2X2-1/2X3/8X3/8SLBB",
    "2L3-1/2X2-1/2X3/8X3/4SLBB",
    "2L3-1/2X2-1/2X5/16SLBB",
    "2L3-1/2X2-1/2X5/16X3/8SLBB",
    "2L3-1/2X2-1/2X5/16X3/4SLBB",
    "2L3-1/2X2-1/2X1/4SLBB",
    "2L3-1/2X2-1/2X1/4X3/8SLBB",
    "2L3-1/2X2-1/2X1/4X3/4SLBB",
    "2L3X2-1/2X1/2SLBB",
    "2L3X2-1/2X1/2X3/8SLBB",
    "2L3X2-1/2X1/2X3/4SLBB",
    "2L3X2-1/2X7/16X3/8SLBB",
    "2L3X2-1/2X7/16SLBB",
    "2L3X2-1/2X3/8X3/8SLBB",
    "2L3X2-1/2X5/16SLBB",
    "2L3X2-1/2X3/8X3/4SLBB",
    "2L3X2-1/2X5/16X3/4SLBB",
    "2L3X2-1/2X1/4SLBB",
    "2L3X2-1/2X7/16X3/4SLBB",
    "2L3X2-1/2X5/16X3/8SLBB",
    "2L3X2-1/2X1/4X3/8SLBB",
    "2L3X2-1/2X3/8SLBB",
    "2L3X2-1/2X3/16X3/8SLBB",
    "2L3X2-1/2X3/16X3/4SLBB",
    "2L3X2-1/2X1/4X3/4SLBB",
    "2L3X2-1/2X3/16SLBB",
    "2L3X2X1/2X3/8SLBB",
    "2L3X2X1/2SLBB",
    "2L3X2X1/2X3/4SLBB",
    "2L3X2X3/8SLBB",
    "2L3X2X3/8X3/8SLBB",
    "2L3X2X3/8X3/4SLBB",
    "2L3X2X5/16SLBB",
    "2L3X2X5/16X3/8SLBB",
    "2L3X2X5/16X3/4SLBB",
    "2L3X2X1/4SLBB",
    "2L3X2X1/4X3/8SLBB",
    "2L3X2X1/4X3/4SLBB",
    "2L3X2X3/16SLBB",
    "2L3X2X3/16X3/8SLBB",
    "2L3X2X3/16X3/4SLBB",
    "2L2-1/2X2X3/8SLBB",
    "2L2-1/2X2X3/8X3/4SLBB",
    "2L2-1/2X2X3/8X3/8SLBB",
    "2L2-1/2X2X5/16X3/8SLBB",
    "2L2-1/2X2X5/16SLBB",
    "2L2-1/2X2X1/4SLBB",
    "2L2-1/2X2X1/4X3/8SLBB",
    "2L2-1/2X2X5/16X3/4SLBB",
    "2L2-1/2X2X1/4X3/4SLBB",
    "2L2-1/2X2X3/16SLBB",
    "2L2-1/2X2X3/16X3/8SLBB",
    "2L2-1/2X2X3/16X3/4SLBB",
    "2L2-1/2X1-1/2X1/4SLBB",
    "2L2-1/2X1-1/2X1/4X3/8SLBB",
    "2L2-1/2X1-1/2X1/4X3/4SLBB",
    "2L2-1/2X1-1/2X3/16SLBB",
    "2L2-1/2X1-1/2X3/16X3/8SLBB",
    "2L2-1/2X1-1/2X3/16X3/4SLBB",
)
