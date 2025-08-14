import pandas as pd
import io
import matplotlib.pyplot as plt

def generate_report(df, summary_df, col_x, col_y):
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        # Write data
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

        workbook = writer.book
        worksheet = workbook.add_worksheet("Charts")
        writer.sheets["Charts"] = worksheet

        # ---- Chart 1: Frequency / Distribution ----
        freq_counts = df[col_x].value_counts().reset_index()
        freq_counts.columns = [col_x, "Frequency"]

        plt.figure(figsize=(6, 4))
        plt.bar(freq_counts[col_x].astype(str), freq_counts["Frequency"])
        plt.title(f"Frequency of {col_x}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        freq_chart_img = io.BytesIO()
        plt.savefig(freq_chart_img, format="png")
        plt.close()

        worksheet.insert_image("B2", "freq_chart.png", {"image_data": freq_chart_img})

        # ---- Chart 2: Relationship between col_x and col_y ----
        try:
            if pd.api.types.is_numeric_dtype(df[col_y]):
                pivot_df = df.groupby(col_x)[col_y].mean().reset_index()

                plt.figure(figsize=(6, 4))
                plt.bar(pivot_df[col_x].astype(str), pivot_df[col_y])
                plt.title(f"Average {col_y} by {col_x}")
                plt.xticks(rotation=45)
                plt.tight_layout()
                relation_chart_img = io.BytesIO()
                plt.savefig(relation_chart_img, format="png")
                plt.close()

                worksheet.insert_image("B20", "relation_chart.png", {"image_data": relation_chart_img})

        except Exception as e:
            worksheet.write("B20", f"Could not generate relationship chart: {e}")

        # ---- Insights Section ----
        try:
            insights_sheet = workbook.add_worksheet("Insights")
            writer.sheets["Insights"] = insights_sheet

            if pd.api.types.is_numeric_dtype(df[col_y]):
                top5 = df.nlargest(5, col_y)[[col_x, col_y]]
                bottom5 = df.nsmallest(5, col_y)[[col_x, col_y]]

                insights_sheet.write(0, 0, f"Top 5 {col_x} by {col_y}")
                for i, row in enumerate(top5.itertuples(index=False), start=1):
                    insights_sheet.write(i, 0, str(row[0]))
                    insights_sheet.write(i, 1, row[1])

                insights_sheet.write(len(top5) + 2, 0, f"Bottom 5 {col_x} by {col_y}")
                for i, row in enumerate(bottom5.itertuples(index=False), start=len(top5) + 3):
                    insights_sheet.write(i, 0, str(row[0]))
                    insights_sheet.write(i, 1, row[1])

                insights_sheet.write(len(top5) + len(bottom5) + 5, 0, "Key Insights:")
                avg_val = df[col_y].mean()
                insights_sheet.write(len(top5) + len(bottom5) + 6, 0, f"The average {col_y} is {avg_val:.2f}.")

        except Exception as e:
            worksheet.write("B40", f"Could not generate insights: {e}")

    output.seek(0)
    return output
