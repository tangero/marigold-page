---
slug: "gss"
url: "/mobilnisite/slovnik/gss/"
type: "slovnik"
title: "GSS – GNSS System Simulator"
date: 2025-01-01
abbr: "GSS"
fullName: "GNSS System Simulator"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/gss/"
summary: "Testovací zařízení, které simuluje signály z globálních navigačních družicových systémů (GNSS), jako jsou GPS, Galileo nebo GLONASS. Používá se při testování shody (conformance) a výkonu uživatelského"
---

GSS (simulátor systému GNSS) je testovací zařízení, které simuluje signály GNSS pro řízené laboratorní testování uživatelského zařízení (UE) za účelem ověření jeho funkcí založených na poloze.

## Popis

[GNSS](/mobilnisite/slovnik/gnss/) System Simulator (GSS) je sofistikované testovací zařízení používané především při vývoji, certifikaci a validaci mobilních zařízení (uživatelského zařízení, UE), která obsahují služby určování polohy. Jeho hlavní funkcí je generovat a vysílat simulované rádiové kmitočtové ([RF](/mobilnisite/slovnik/rf/)) signály, které jsou nerozlišitelné od signálů vysílaných skutečnými konstelacemi globálních navigačních družicových systémů (GNSS), jako jsou [GPS](/mobilnisite/slovnik/gps/) (USA), Galileo (EU), [GLONASS](/mobilnisite/slovnik/glonass/) (Rusko) nebo BeiDou (Čína). Tím, že to dělá v odstíněném laboratorním prostředí, umožňuje inženýrům testovat polohovací modul UE bez závislosti na živých, proměnných signálech z oblohy.

GSS funguje tak, že modeluje celou geometrii družicové konstelace, orbitální mechaniku a charakteristiky signálu. Testující může definovat konkrétní scénář včetně simulovaného času, data, zeměpisné polohy (zeměpisná šířka, délka, nadmořská výška) a sady viditelných satelitů. Simulátor vypočítá přesnou fázi kódu, Dopplerův posuv a výkon signálu pro každý simulovaný družicový signál, tak jak by byl přijímán na definovaném testovacím místě. Tyto digitální výpočty jsou následně převedeny na analogový RF signál na příslušných kmitočtech v pásmu L (např. [L1](/mobilnisite/slovnik/l1/), L5). Testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) přijímá tento signál prostřednictvím galvanického kabelového připojení nebo RF antény v odstíněné komoře.

Specifikace 3GPP, zejména řady TS 25.171, 36.171 a 37.571, definují požadavky na testy shody (conformance) pro polohovací schopnosti UE za použití GSS. Tyto testovací případy ověřují, že UE splňuje požadavky na výkon pro metriky jako je čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)), citlivost (zachycení a sledování) a přesnost polohy za různých řízených podmínek, včetně statických a dynamických scénářů. GSS umožňuje opakovatelné a reprodukovatelné testování náročných podmínek, které je obtížné spolehlivě zachytit při reálném terénním testování, jako jsou podmínky slabého signálu, specifické odrazy (multipath) nebo scénáře rušení.

## K čemu slouží

Standardizace testovacích metod s použitím GSS byla hnací silou potřeby spolehlivé, konzistentní a opakovatelné certifikace polohového výkonu v mobilních zařízeních. Jak se služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)) staly klíčovou funkcí pro nouzová volání (E911/eCall), navigaci a různé aplikace, síťoví operátoři a regulační orgány požadovali záruky minimální úrovně výkonu. Samotné terénní testování je nedostatečné kvůli své proměnlivosti (měnící se geometrie satelitů, počasí, rušení) a nedostatku opakovatelnosti.

GSS poskytuje řízené laboratorní prostředí, které tyto problémy řeší. Umožňuje testujícím vytvářet přesné, opakovatelné scénáře pro ověření výkonnostních benchmarků. Také umožňuje testování okrajových případů a režimů selhání, které jsou klíčové pro robustnost, jako je provoz s velmi nízkou úrovní signálu, za přítomnosti specifických zdrojů rušení nebo během simulovaných efektů odrazů v městské zástavbě (urban canyon). Definováním těchto testů ve specifikacích 3GPP se zajišťuje jednotný benchmark pro všechny výrobce UE, což garantuje základní úroveň kvality služeb určování polohy pro koncové uživatele napříč různými zařízeními a sítěmi.

## Klíčové vlastnosti

- Generuje simulované RF signály pro více konstelací GNSS (GPS, Galileo atd.)
- Modeluje plnou dynamiku družicové konstelace a šíření signálu
- Umožňuje vytváření opakovatelných statických a dynamických testovacích scénářů
- Umožňuje řízení klíčových parametrů, jako je výkon signálu, Dopplerův posuv a odrazy (multipath)
- Podporuje testování shody (conformance) podle definice v 3GPP TS 37.571
- Umožňuje testování výkonu UE v řízených podmínkách slabého signálu a rušení

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.571** (Rel-19) — UE Conformance for Positioning

---

📖 **Anglický originál a plná specifikace:** [GSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gss/)
