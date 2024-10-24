import aiofiles
import pandas as pd

class AsyncFileWriter:
    def __init__(self, df, output_file):
        self.df = df
        self.output_file = output_file

    async def write_json(self):
        async with aiofiles.open(f'{self.output_file}.json', mode='w') as f:
            json_data = self.df.to_json(index=False, orient="records")
            await f.write(json_data)

    async def write_csv(self):
        async with aiofiles.open(f'{self.output_file}.csv', mode='w') as f:
            csv_data = self.df.to_csv(index=False)
            await f.write(csv_data)

    async def write_excel(self):
        async with aiofiles.tempfile.NamedTemporaryFile(delete=False) as tmp:
            self.df.to_excel(tmp.name, index=False, sheet_name='Users')
            async with aiofiles.open(f'{self.output_file}.xlsx', mode='wb') as f:
                await f.write(tmp.read())

    async def write_parquet(self):
        self.df.to_parquet(f'{self.output_file}.parquet', index=False)  # parquet does not support async yet

    async def write_files(self, output_format):
        if output_format in ['json', 'all']:
            await self.write_json()
        if output_format in ['csv', 'all']:
            await self.write_csv()
        if output_format in ['excel', 'all']:
            await self.write_excel()
        if output_format in ['parquet', 'all']:
            await self.write_parquet()

# Usage example
#async def main():
#    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
#    writer = AsyncFileWriter(df, "output_file")
#    await writer.write_files('all')

# Run the async main function
#asyncio.run(main())
