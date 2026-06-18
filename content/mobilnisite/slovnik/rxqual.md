---
slug: "rxqual"
url: "/mobilnisite/slovnik/rxqual/"
type: "slovnik"
title: "RXQUAL – Received Signal Quality"
date: 2025-01-01
abbr: "RXQUAL"
fullName: "Received Signal Quality"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rxqual/"
summary: "RXQUAL je klíčové rádiové měření odhadující míru bitových chyb (BER) před dekódováním kanálu. Ukazuje kvalitu a integritu rádiového spoje a používá se spolu s RXLEV pro rozhodování o předávání hovoru,"
---

RXQUAL je měření v GSM rádiovém rozhraní, které odhaduje míru bitových chyb před dekódováním kanálu. Používá se jako ukazatel kvality spoje pro rozhodování o předávání hovoru, řízení výkonu a diagnostiku rušení.

## Popis

Received Signal Quality (RXQUAL) je klíčové měření kvality spoje v GSM a příbuzných 3GPP technologiích. Na rozdíl od [RXLEV](/mobilnisite/slovnik/rxlev/), které měří sílu signálu, RXQUAL odhaduje míru bitových chyb ([BER](/mobilnisite/slovnik/ber/)) na přijímaném digitálním signálu před dekódováním kanálu. Je to přímý ukazatel poškození, které rádiový burst utrpěl vlivem faktorů jako je rušení, mnohocestné útlumy a šum. Z architektonického hlediska RXQUAL měří fyzická vrstva přijímače – v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) pro downlink a v základnové stanici ([BTS](/mobilnisite/slovnik/bts/)) pro uplink. Měření se typicky odvozuje porovnáním známé tréninkové sekvence (midamble) vložené do každého normálního burstu s přijatou verzí a výpočtem míry chyb na tomto známém bitovém vzoru.

Operace zahrnuje zpracování demodulovaných bitů předtím, než jsou předány přes ekvalizér a dekodér kanálu. Vypočtená hrubá BER se pak mapuje na jednu z osmi diskrétních úrovní RXQUAL (0 až 7), kde RXQUAL 0 představuje nejlepší kvalitu (BER < 0,2 %) a RXQUAL 7 nejhorší (BER > 12,8 %). Tato kvantovaná hodnota je hlášena vyšším vrstvám (správa [RR](/mobilnisite/slovnik/rr/)) a zahrnuta do měřicích hlášení odesílaných síti. Řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) používá tato hlášení doplňkově spolu s RXLEV.

RXQUAL hraje zásadní roli v optimalizaci sítě a udržování kvality hovoru. Jeho primární funkcí je informovat o rozhodnutích o předávání hovoru. Předání může být spuštěno kvůli špatné kvalitě (předání založené na RXQUAL), i když je úroveň signálu (RXLEV) přijatelná, což je klíčové ve scénářích omezených rušením. Je také klíčovým vstupem pro algoritmy řízení výkonu; pokud je RXQUAL špatné, síť může nařídit zvýšení vysílacího výkonu pro překonání rušení, za předpokladu, že RXLEV již není příliš vysoké. Dále přetrvávající špatné hodnoty RXQUAL při dobrém RXLEV jsou klasickým diagnostickým příznakem ko-kanálového nebo přilehlého kanálového rušení, což usměrňuje snahy o plánování a optimalizaci sítě za účelem zlepšení frekvenční reutilizace a celkové kapacity systému.

## K čemu slouží

RXQUAL bylo zavedeno, aby řešilo klíčové omezení používání pouze síly signálu ([RXLEV](/mobilnisite/slovnik/rxlev/)) pro řízení sítě. Silný signál negarantuje kvalitní spojení; může být zkreslen vysokou úrovní rušení od jiných buněk používajících stejnou frekvenci (ko-kanálové rušení) nebo přilehlou frekvenci. Spoléhání se pouze na RXLEV by mohlo vést k tomu, že by mobilní stanice uvízla na silném, ale silně rušeném kanálu, což by mělo za následek přerušení hovoru nebo špatnou kvalitu hlasu.

Vytvoření RXQUAL bylo motivováno potřebou druhého, ortogonálního metrika, které přímo odráželo použitelnost rádiového spoje. Řeší problém rozlišení mezi slabým signálem (špatné pokrytí) a silným, ale zkresleným signálem (špatná kvalita způsobená rušením). Toto rozlišení umožňuje síti aplikovat správný lék: předání hovoru na jinou buňku při problémech s pokrytím, nebo předání na jiný frekvenční kanál či úpravu řízení výkonu při problémech s rušením. Poskytnutím standardizované míry kvality spoje RXQUAL umožnilo inteligentnější a robustnější správu rádiových zdrojů, což bylo nezbytné pro dosažení vysoké kapacity a kvalitativních cílů hustých nasazení GSM sítí.

## Klíčové vlastnosti

- Odhaduje hrubou míru bitových chyb (BER) před dekódováním kanálu
- Hlášeno jako celočíselný index od 0 (nejlepší) do 7 (nejhorší) odpovídající rozsahům BER
- Odvozeno z míry chyb na známé tréninkové sekvenci v rámci GSM burstu
- Klíčový spouštěč pro rozhodování o předání hovoru založeném na kvalitě
- Kritický vstup pro algoritmy řízení výkonu pro boj s rušením
- Primární diagnostické metrika pro identifikaci síťových podmínek omezených rušením

## Související pojmy

- [RXLEV – Received Signal Level](/mobilnisite/slovnik/rxlev/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [RXQUAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rxqual/)
