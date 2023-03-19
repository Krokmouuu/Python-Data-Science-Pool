import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a csv file into a pandas DataFrame."""

    try:
        assert path.endswith('.csv'), "The file is not a csv"
        df = pd.read_csv(path)
        print("Dataset dimensions :", df.shape)
    except AssertionError as e:
        print("AssertionError:", e)
        return None
    except FileExistsError as e:
        print("FileExistsError:", e)
        return None
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
        return None
    except ValueError as e:
        print("ValueError:", e)
        return None
    except TypeError as e:
        print("TypeError:", e)
        return None

    return df
