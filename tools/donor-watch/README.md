# donor-watch

Automated salvage-Tesla donor watchlist for the Slipstream flagship build — and for anyone else hunting a Model 3/Y pack donor. Applies the [Donor Procurement Guide](../../guides/Donor_Procurement_and_Teardown_Guide_v0_1.md) filter to auction listings, tracks auction countdowns, and pings you ("this Model 3 auctions in 3 hours") via [ntfy.sh](https://ntfy.sh) push and/or email.

**Status: v0.1, experimental.** Auction sites rotate bot protection constantly; this tool is built to degrade gracefully (a blocked source becomes a "check manually" line, never a crash). Expect to maintain the fetchers.

## What it does

Every run: query sources for Model 3/Y salvage lots → apply the donor filter (reject flood/fire/Austin-4680, prefer front/rear-hit + Run-and-Drive + Fremont VIN + 2021+ LFP trims) → diff against `watchlist.json` → notify on **new matches** and **anything auctioning within 48 h**.

## Setup

```bash
pip install requests
cp config.example.json config.json     # edit: your zip, sources, notify targets
python3 donor_watch.py --dry-run       # first run, no state written
```

**Push notifications (easiest):** pick a hard-to-guess topic string, put it in `ntfy_topic`, install the ntfy app on your phone, subscribe to the topic. Done — no accounts.
**Email:** fill the `email` block (any SMTP provider; use an app password).

## Run it automatically (GitHub Actions)

The workflow at `.github/workflows/donor-watch.yml` runs every 6 hours on a fork of this repo, commits the updated `watchlist.json` (so your watch history is versioned), and notifies via your ntfy topic (set repo secret `NTFY_TOPIC`). Fork → add secret → enable Actions.

## Human-in-the-loop verdicts

Every surfaced lot is **[NEEDS REVIEW]** until you decide — open the listing, eyeball the damage, then:

```bash
python3 donor_watch.py --approve copart:12345678   # keep tracking + urgent countdown reminders
python3 donor_watch.py --reject copart:12345678    # strike it from the list for good
```

Approved lots carry **[APPROVED]** in every subsequent report and countdown alert; rejected lots never appear again. Nothing is silently dismissed by the filter except flood/fire and Austin-4680 — side/undercarriage hits surface with an "inspect-first" flag because photos can't clear them but a human can.

## Ground rules

- **Watch, don't bot.** This tool never logs in, never bypasses CAPTCHAs, and defaults to a polite schedule. Bidding happens with your own Copart/IAAI account, by you.
- Copart's public search endpoint and IAAI's listing pages are unofficial and change without notice; when they block, use the aggregators manually ([bid.cars](https://bid.cars) for historical hammer prices, AutoBidMaster/SCA/Salvagebid as broker frontends) — the filter logic in `score_lot()` is the durable part of this tool.
- The distance filter (`home_zip`/`radius_miles`) is currently applied by choosing which yards your query covers — Copart's API location filtering is fussy; contributions welcome.

## The filter, in code

`score_lot()` encodes Guide #1: **reject** flood/water/fire, Austin-built (VIN pos 11 = A); **flag** side/undercarriage hits for review; **prefer** front/rear damage, Run-and-Drive, Fremont (F), 2021+ Model 3 SR/RWD (CATL LFP — the flagship's preferred pack), parts-only titles (cheaper, check your state). Airbag deployment is *not* a reject — a fired pyro fuse is a $30–60 part and scares off the competition.

*Contributions: fetcher fixes are the most-wanted PR. See CONTRIBUTING.md at repo root.*
