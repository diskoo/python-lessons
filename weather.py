import python_weather
import asyncio
import os

async def getweather():
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    weather = await client.get("Тюмень")
  
    celsius = (weather.current.temperature-32)*0.55

    print("Temperature in Celsius is:",str(round(celsius)) + "°")

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
