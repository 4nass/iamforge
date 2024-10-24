import aiofiles
import pandas as pd

class AsyncFileConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        
    async def convert_csv_to_excel(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_csv(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.tempfile.NamedTemporaryFile(delete=False) as tmp:
            df.to_excel(tmp.name, index=False, sheet_name='Users')
            async with aiofiles.open(output_file, mode='wb') as f:
                await f.write(tmp.read())

    async def convert_csv_to_json(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_csv(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            json_data = df.to_json(index=False)
            await f.write(json_data)

    async def convert_csv_to_parquet(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_csv(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        df.to_parquet(output_file, index=False)

    async def convert_excel_to_csv(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_excel(self.input_file, dtype=str, sheet_name='Users')

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            csv_data = df.to_csv(index=False)
            await f.write(csv_data)

    async def convert_excel_to_json(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_excel(self.input_file, dtype=str, sheet_name='Users')

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            json_data = df.to_json(index=False)
            await f.write(json_data)

    async def convert_excel_to_parquet(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_excel(self.input_file, dtype=str, sheet_name='Users')

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        df.to_parquet(output_file, index=False)

    async def convert_json_to_csv(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_json(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            csv_data = df.to_csv(index=False)
            await f.write(csv_data)

    async def convert_json_to_parquet(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_json(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        df.to_parquet(output_file, index=False)

    async def convert_json_to_excel(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_json(self.input_file, dtype=str)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.tempfile.NamedTemporaryFile(delete=False) as tmp:
            df.to_excel(tmp.name, index=False, sheet_name='Users')
            async with aiofiles.open(output_file, mode='wb') as f:
                await f.write(tmp.read())

    async def convert_parquet_to_csv(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_parquet(input_file)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            csv_data = df.to_csv(index=False)
            await f.write(csv_data)

    async def convert_parquet_to_json(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_parquet(input_file)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.open(output_file, mode='w') as f:
            json_data = df.to_json(index=False)
            await f.write(json_data)

    async def convert_parquet_to_excel(self, output_file, columns_to_keep=None, column_mapping=None):
        df = pd.read_parquet(input_file)

        if columns_to_keep:
            df = df[columns_to_keep]

        if column_mapping:
            df = df.rename(columns=column_mapping)

        async with aiofiles.tempfile.NamedTemporaryFile(delete=False) as tmp:
            df.to_excel(tmp.name, index=False, sheet_name='Users')
            async with aiofiles.open(output_file, mode='wb') as f:
                await f.write(tmp.read())
