import enum


class ActivityLevel(str, enum.Enum):
    NONE = "none"
    LIGHT = "light"
    MODERATE = "moderate"
    HIGH = "high"


class UserGoal(str, enum.Enum):
    HEALTH = "health"
    MAINTAIN = "maintain"
    CUT = "cut"
    BULK = "bulk"


class TargetMode(str, enum.Enum):
    CALCULATED = "calculated"
    CUSTOM = "custom"
    MIXED = "mixed"


class PreferenceType(str, enum.Enum):
    DIET = "diet"
    RESTRICTION = "restriction"
    ALLERGY = "allergy"
    HEALTH_TOPIC = "health_topic"


class TargetSource(str, enum.Enum):
    CALCULATED = "calculated"
    REFERENCE = "reference"
    CUSTOM = "custom"
    PROFESSIONAL = "professional"
    MIXED = "mixed"


class FoodCategoryType(str, enum.Enum):
    PROTEIN = "protein"
    CARBOHYDRATES = "carbohydrates"
    FAT = "fat"
    FIBER = "fiber"


class LifeStage(str, enum.Enum):
    STANDARD = "standard"
    PREGNANCY = "pregnancy"
    LACTATION = "lactation"


class ReferenceType(str, enum.Enum):
    RDA = "RDA"
    AI = "AI"
    UL = "UL"


class TipType(str, enum.Enum):
    GENERAL = "general"
    PERSONALIZED = "personalized"
    PROTEIN = "protein"
    CARBOHYDRATES = "carbohydrates"
    FAT = "fat"
    FIBER = "fiber"