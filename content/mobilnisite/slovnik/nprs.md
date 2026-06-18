---
slug: "nprs"
url: "/mobilnisite/slovnik/nprs/"
type: "slovnik"
title: "NPRS – Narrowband Positioning Reference Signals"
date: 2025-01-01
abbr: "NPRS"
fullName: "Narrowband Positioning Reference Signals"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nprs/"
summary: "NPRS jsou referenční signály vysílané v NB-IoT, které umožňují určování polohy zařízení. Jsou klíčové pro služby založené na poloze v aplikacích IoT, jako je sledování majetku, protože poskytují časov"
---

NPRS je soubor referenčních signálů vysílaných v sítích NB-IoT, které umožňují určování polohy zařízení pro služby založené na poloze tím, že poskytují časová měření.

## Popis

Narrowband Positioning Reference Signals (NPRS) jsou specializované downlinkové referenční signály definované pro Narrowband Internet of Things (NB-IoT) za účelem usnadnění určování polohy zařízení. Jsou navrženy pro provoz v úzkém 180kHz pásmu nosné NB-IoT, což je odlišuje od positioning reference signals ([PRS](/mobilnisite/slovnik/prs/)) používaných v širších pásmech LTE. NPRS vysílají základnové stanice (eNBs pro LTE, gNBs pro NR-NB-IoT) ve specifických podrámcích nakonfigurovaných sítí. Jejich hlavní funkcí je poskytovat známý, předvídatelný signálový vzor, který může uživatelské zařízení (UE) detekovat a měřit s vysokou přesností, a to i v náročných rádiových podmínkách typických pro nasazení IoT, jako jsou hluboko vnitřní nebo podzemní lokality.

Architektura NPRS zahrnuje pečlivé mapování v rámci mřížky fyzických zdrojů NB-IoT. Signály zabírají specifické resource elements (REs) ve vyčleněných NPRS podrámcích, čímž se vyhýbají kolizím s jinými kritickými signály, jako jsou Narrowband Primary a Secondary Synchronization Signals ([NPSS](/mobilnisite/slovnik/npss/)/[NSSS](/mobilnisite/slovnik/nsss/)) a broadcast kanály. Vysílací vzor, včetně periodicity, konfigurace utlumení (muting) a sekvence přeskakování frekvencí (frequency hopping), je konfigurovatelný pomocí signalizace vyšší vrstvy (např. přes [LPP](/mobilnisite/slovnik/lpp/) nebo [RRC](/mobilnisite/slovnik/rrc/)). Tato konfigurovatelnost umožňuje síti optimalizovat výkon určování polohy, řídit interferenci mezi buňkami a vyvažovat přesnost polohy vůči systémové režii a spotřebě energie zařízení. UE měří čas příchodu NPRS z více sousedních buněk a hlásí tato měření Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)) síti nebo lokačnímu serveru.

NPRS umožňují polohové techniky jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) v kontextu NB-IoT. V OTDOA UE měří časový rozdíl mezi příchodem NPRS z referenční buňky a z několika sousedních buněk. Tato RSTD měření pak lokační server (např. Enhanced Serving Mobile Location Centre, [E-SMLC](/mobilnisite/slovnik/e-smlc/)) použije k výpočtu zeměpisné polohy zařízení pomocí multilaterace. Návrh NPRS upřednostňuje tzv. hearability – schopnost UE detekovat slabé signály ze vzdálených buněk – prostřednictvím funkcí jako nízká střída (duty cycle), zvýšení výkonu (power boosting) a vzory utlumení, které snižují interbuněčnou interferenci. To z NPRS činí základní kámen pro umožnění regulatorních (např. E911) i komerčních lokalizačních služeb pro zařízení massive machine-type communication (mMTC), která vyžadují dlouhou životnost baterie a rozšířené pokrytí.

## K čemu slouží

NPRS byly zavedeny, aby řešily specifickou výzvu lokalizace zařízení NB-IoT, což je klíčový požadavek pro mnoho aplikací IoT. Před verzí Rel-14 NB-IoT, jakožto nová technologie navržená pro mMTC, postrádala standardizované možnosti určování polohy. Zatímco starší LTE nabízelo metody určování polohy jako OTDOA využívající PRS, tyto signály nebyly vhodné pro ultranízkopásmový provoz NB-IoT (180 kHz). Stávající LTE PRS vyžadovaly širší pásmo pro dostatečné rozlišení v časové oblasti a zpracovatelský zisk, což zařízení NB-IoT nemohla podporovat. Vznikl tak problém: případy užití IoT, jako je sledování v logistice, chytré měření a bezpečnostní alarmy, vyžadovaly spolehlivou informaci o poloze, ale rádiová technologie pro ně navržená neměla žádné efektivní síťové řešení pro určování polohy.

Vytvoření NPRS bylo motivováno potřebou polohového signálu optimalizovaného pro omezení NB-IoT. Tato omezení zahrnují omezenou výpočetní kapacitu zařízení, extrémní požadavky na energetickou účinnost pro víceletou životnost baterie a provoz v režimech s rozšířeným pokrytím (např. až 20 dB rozšíření pokrytí). NPRS byly navrženy od základů tak, aby pracovaly v rámci jediného fyzického resource bloku, využívaly delší signálové sekvence a opakování k dosažení potřebného zpracovatelského zisku pro detekci v podmínkách hlubokého pokrytí. Řeší problém poskytování přesných časových měření bez kompromisů vůči základním principům návrhu NB-IoT – nízké složitosti a ultra nízké spotřebě energie. Jejich zavedení v Rel-14 umožnilo NB-IoT splnit jak komerční požadavky na lokalizační služby, tak regulatorní požadavky na určování polohy, což z něj učinilo úplnější a životaschopnější technologii pro trh massive IoT.

## Klíčové vlastnosti

- Optimalizováno pro 180kHz pásmo nosné NB-IoT
- Podporuje určování polohy metodou Observed Time Difference of Arrival (OTDOA)
- Konfigurovatelná periodicita a vzory utlumení pro řízení interference
- Navrženo pro vysokou hearability (detekovatelnost) z více buněk ve scénářích s rozšířeným pokrytím
- Umožňuje provoz v in-band, guard-band a standalone režimech nasazení NB-IoT
- Využívá přeskakování frekvencí (frequency hopping) pro potlačení úniků a zlepšení robustnosti měření

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [NPSS – Narrowband Primary Synchronization Signal](/mobilnisite/slovnik/npss/)
- [NSSS – Narrowband Secondary Synchronization Signal](/mobilnisite/slovnik/nsss/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NPRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nprs/)
