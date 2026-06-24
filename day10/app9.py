import asyncio
import edge_tts

TEXT = f'''Vanakkam nanbargale. Naan Prabhu. 
Inniku namma Python programming oda basics pathi kathukaporom. 
Variables, loops, functions matrum lists epadi use panna vendum nu 
practical examples oda paakaporom. 
Daily konjam konjam practice pannina neengalum nalla programmer aaga mudiyum.
'''

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        #voice="en-US-AriaNeural"
        voice="ta-IN-PallaviNeural"
    )
    await communicate.save("output.mp3")

asyncio.run(main())