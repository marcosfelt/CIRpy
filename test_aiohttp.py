import cirpy
import aiohttp
import asyncio

async def test_request():
    async with aiohttp.ClientSession() as session:
        smiles = await cirpy.resolve(session, '71-43-2', 'smiles')
    real_smiles = "c1ccccc1"
    assert real_smiles == smiles

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_request())