
import pandas as pd


class DataInspection:

    def __init__(self, df):
        self.df = df

        # Prepare commonly used columns
        self.order_amount = pd.to_numeric(
            df["order_amount"], errors="coerce"
        )

        self.items_count = pd.to_numeric(
            df["items_count"], errors="coerce"
        )

        self.timestamps = pd.to_datetime(
            df["order_timestamp"], errors="coerce"
        )

        self.delivery_time = pd.to_numeric(
            df["delivery_time_mins"], errors="coerce"
        )

        self.discount_amount = pd.to_numeric(
            df["discount_amount"], errors="coerce"
        )

    # 1. Define inspection categories
    def inspections(self):
        return {
            "Basic Inspection": [
                "head()", "tail()", "sample()", "shape",
                "columns", "info()", "dtypes", "describe()"
            ],

            "Missing Value Inspection": [
                "missing_per_column", "total_missing",
                "missing_percentage", "highest_missing_column",
                "columns_without_missing"
            ],

            "Duplicate Inspection": [
                "duplicate_rows", "total_duplicate_rows",
                "duplicate_order_ids"
            ],

            "Categorical Inspection": [
                "unique_cities", "unique_payment_methods",
                "unique_delivery_status", "city_frequency",
                "payment_frequency", "status_frequency"
            ],

            "Numerical Inspection": [
                "minimum_order_amount", "maximum_order_amount",
                "minimum_delivery_time", "maximum_delivery_time",
                "numerical_summary"
            ],

            "Data Validation": [
                "negative_delivery_time", "invalid_order_amount",
                "invalid_item_count", "missing_item_count",
                "discount_exceeds_order_amount",
                "missing_timestamps", "invalid_timestamps"
            ]
        }

    # 2. Define inspection operations
    def operations(self):

        df = self.df

        return {
            # Basic Inspection
            "head()": lambda: df.head(),
            "tail()": lambda: df.tail(),
            "sample()": lambda: df.sample(),
            "shape": lambda: df.shape,
            "columns": lambda: df.columns,
            "info()": lambda: df.info(),
            "dtypes": lambda: df.dtypes,
            "describe()": lambda: df.describe(include="all"),

            # Missing Value Inspection
            "missing_per_column": lambda: df.isna().sum(),
            "total_missing": lambda: df.isna().sum().sum(),
            "missing_percentage": lambda: df.isna().mean() * 100,
            "highest_missing_column": lambda: df.isna().sum().idxmax(),
            "columns_without_missing": lambda: df.columns[
                df.isna().sum() == 0
            ],

            # Duplicate Inspection
            "duplicate_rows": lambda: df[df.duplicated()],
            "total_duplicate_rows": lambda: df.duplicated().sum(),
            "duplicate_order_ids": lambda: df[
                df.duplicated("order_id", keep=False)
            ],

            # Categorical Inspection
            "unique_cities": lambda: df["city"].unique(),
            "unique_payment_methods": lambda: df["payment_method"].unique(),
            "unique_delivery_status": lambda: df["delivery_status"].unique(),
            "city_frequency": lambda: df["city"].value_counts(dropna=False),
            "payment_frequency": lambda: df["payment_method"].value_counts(dropna=False),
            "status_frequency": lambda: df["delivery_status"].value_counts(dropna=False),

            # Numerical Inspection
            "minimum_order_amount": lambda: self.order_amount.min(),
            "maximum_order_amount": lambda: self.order_amount.max(),
            "minimum_delivery_time": lambda: self.delivery_time.min(),
            "maximum_delivery_time": lambda: self.delivery_time.max(),

            "numerical_summary": lambda: pd.DataFrame({
                "order_amount": self.order_amount,
                "items_count": self.items_count,
                "discount_amount": self.discount_amount,
                "delivery_time_mins": self.delivery_time
            }).describe(),

            # Data Validation
            "negative_delivery_time": lambda: df[
                self.delivery_time < 0
            ],

            "invalid_order_amount": lambda: df[
                df["order_amount"].notna() & self.order_amount.isna()
            ],

            "invalid_item_count": lambda: df[
                df["items_count"].notna() &
                (
                    self.items_count.isna() |
                    (self.items_count % 1 != 0) |
                    (self.items_count <= 0)
                )
            ],

            "missing_item_count": lambda: df[
                df["items_count"].isna()
            ],

            "discount_exceeds_order_amount": lambda: df[
                self.discount_amount > self.order_amount
            ],

            "missing_timestamps": lambda: df[
                df["order_timestamp"].isna()
            ],

            "invalid_timestamps": lambda: df[
                df["order_timestamp"].notna() &
                self.timestamps.isna()
            ]
        }

    # 3. Execute inspections
    def run_inspections(self):

        categories = self.inspections()
        operations_map = self.operations()

        for category, methods in categories.items():

            print("\n", "=" * 150,category, "=" * 150)
            

            for method in methods:

                print(f"\n-------- {method} --------")

                try:
                    result = operations_map[method]()

                    if method != "info()":
                        print(result)

                except KeyError as error:
                    print(f"Missing column or operation: {error}")

                except Exception as error:
                    print(
                        f"Error while executing {method}: "
                        f"{type(error).__name__}: {error}"
                    )

                print("-" * 150)


# 4. Read CSV and run the inspection system
try:
    df = pd.read_csv("food_delivery_orders.csv")

    data_inspection = DataInspection(df)

    data_inspection.run_inspections()

except FileNotFoundError:
    print("Error: CSV file was not found.")

except pd.errors.EmptyDataError:
    print("Error: CSV file is empty.")

except pd.errors.ParserError as error:
    print(f"Error: Unable to parse CSV file: {error}")

except KeyError as error:
    print(f"Error: Required column is missing: {error}")

except Exception as error:
    print(f"Unexpected error: {type(error).__name__}: {error}")
