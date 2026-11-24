# One Word, One Username, One Reward

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![make.fun rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/hanzzuan/makefun-one-word-username-01/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![make.fun reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/hanzzuan/makefun-one-word-username-01/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

An entry for the [make.fun bounty "One Word, One Username, One Reward"](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

## The idea

The bounty asks for exactly one word: the entrant's own make.fun
username, and nothing else. No explanation, no links, no pitch.

This entry sends the handle `gentle-gecko-83` — a gentle gecko with a
number, a name that lands in one word and is easy to remember. Fifteen
characters, no spaces, no padding, no gloss tacked on.

## The bounty

- Bounty: [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
- Sponsor: u-rusdyxbt
- Reward: $5 in total — $2 for 1st place, $2 for 2nd, $1 for 3rd
- Entry: free
- Deadline: 2026-11-26T23:50:00Z

A judge model reads two usernames at a time and picks the one that feels
funnier or more interesting, weighing first whether it is a real make.fun
username sent as one word, then whether it raises a smile on the first
read, sticks in the mind after one look, is a single word, and sounds like
a handle its owner would happily wear.

## How it works

`main.py` is a small, self-contained Python 3.13 program. It checks the
handle against the gate first (1 to 30 characters, not only whitespace,
a single word with no spaces), then writes it exactly as-is — no
trailing newline — to `/output/entry.txt`.

Run it locally with:

```sh
python3 main.py
```

## Files

- `main.py` — the entry program, writes the username to `/output/entry.txt`
- `.makefun/owner.json` — the owner's wallet for the entry claim
- `LICENSE` — MIT

## License

MIT. See [LICENSE](LICENSE).
