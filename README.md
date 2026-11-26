# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/jinan86/deadpan-forecasts/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/jinan86/deadpan-forecasts/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

A [make.fun](https://make.fun) entry for **Deadpan Forecasts for Cities That Do Not Exist**: one absurd-but-believable weather line for an invented city, delivered in the plain, confident tone of a deadpan TV meteorologist.

## The entry

`main.py` writes exactly one forecast line to `/output/entry.txt` — 1–160 UTF-8 characters, a single line:

> Good evening from Tarnwick, where tonight's fog will apologise for arriving 40 minutes early and leave by 9.

Tarnwick does not exist. Its fog, however, is punctual, polite, and 40 minutes early.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates its own output before exiting: exactly one line, 1–160 characters, valid UTF-8.

## License

MIT — see [LICENSE](LICENSE).
