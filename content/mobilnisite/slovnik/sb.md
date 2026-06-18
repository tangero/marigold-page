---
slug: "sb"
url: "/mobilnisite/slovnik/sb/"
type: "slovnik"
title: "SB – Synchronization Burst"
date: 2025-01-01
abbr: "SB"
fullName: "Synchronization Burst"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sb/"
summary: "Specifický typ burstu používaný v GSM a UMTS pro procedury počáteční synchronizace a vyhledávání buněk. Nese známou tréninkovou sekvenci, která mobilní stanici umožňuje odhadnout časování a frekvenční"
---

SB je specifický typ burstu používaný v GSM a UMTS pro počáteční synchronizaci a vyhledávání buněk. Nese známou tréninkovou sekvenci, která umožňuje odhad časování a frekvenčního posunu pro navázání rádiového spoje.

## Popis

Synchronization Burst (SB) je kritický signál fyzické vrstvy definovaný ve specifikacích 3GPP pro systémy GSM a UMTS. Jeho primární funkcí je usnadnit počáteční proces vyhledávání buněk a synchronizace pro uživatelské zařízení (UE). SB je vysílán základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/) v GSM, Node B v UMTS) a obsahuje přesně definovanou, známou tréninkovou sekvenci nebo synchronizační kód. Když se UE zapne nebo vstoupí do nové oblasti, skenuje tyto bursty. Po jejich detekci UE koreluje přijímaný signál se známou sekvencí, čímž dosáhne několika klíčových cílů: přesné časové synchronizace pro sladění svého interního hodinového signálu se strukturou snímků a časových slotů sítě a frekvenční synchronizace pro korekci posunů nosné frekvence způsobených nepřesností oscilátorů nebo Dopplerova jevu.

V systému GSM je SB součástí struktury vysílacího kanálu. Je vysílán na specifických časových slotech a nese informace jako Base Station Identity Code ([BSIC](/mobilnisite/slovnik/bsic/)) a číslo snímku. UE použije časování získané z SB k následnému naslouchání jiným řídicím kanálům, jako je Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)), pro získání systémových informací. Robustnost návrhu SB, s jeho specifickými autokorelačními vlastnostmi, zajišťuje spolehlivou detekci i v podmínkách nízkého poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)) a při vícecestném šíření.

V UMTS je synchronizační procedura koncepčně podobná, ale používá dvoustupňový proces s primárním a sekundárním synchronizačním kanálem (P-SCH a S-SCH). Koncept SB je ztělesněn v těchto synchronizačních kanálech, kde jsou vysílány specifické primární a sekundární synchronizační kódy. UE nejprve použije P-SCH k dosažení synchronizace na časový slot a poté S-SCH k dosažení synchronizace na snímek a identifikaci kódové skupiny buňky. Principy použití známého periodického signálu pro získání časování zůstávají konzistentní se základním konceptem SB z GSM.

Role Synchronization Burst je zásadní pro dostupnost sítě a mobilitu. Bez úspěšné synchronizace nemůže UE dekódovat žádné další downlinkové přenosy ani zahájit náhodný přístup. Jeho návrh přímo ovlivňuje dobu počátečního přístupu, výkon vyhledávání buněk v heterogenních sítích a celkovou energetickou účinnost UE, protože rychlejší synchronizační proces snižuje dobu, po kterou musí být přijímací obvody aktivní během výběru buňky.

## K čemu slouží

Synchronization Burst byl vytvořen k řešení základního problému, jak se může mobilní zařízení bez předchozí znalosti síťového časování rychle a spolehlivě zamknout na buněčnou základnovou stanici. V počátcích digitální buněčné komunikace (GSM) byla potřeba metody, aby UE mohla najít a synchronizovat se se sítí během sekund. Před synchronizací je časování UE neznámé a frekvence jeho lokálního oscilátoru může být nepřesná. SB poskytuje předvídatelný, periodický referenční signál ve struktuře rádiového snímku.

Motivace byla hnána potřebou efektivního vstupu do sítě a podpory mobility. Vyhrazený, optimalizovaný burst pro synchronizaci, na rozdíl od použití generických burstů pro přenos dat, umožňuje rychlejší vyhledávání buněk, což zlepšuje uživatelský zážitek při zapnutí a při přechodech mezi buňkami. Také umožňuje robustnější provoz v náročných rádiových podmínkách. Známá sekvence uvnitř SB je navržena pro vynikající autokorelační vlastnosti, což ji činí snadno detekovatelnou a umožňuje přesný odhad časového zpoždění rádiového kanálu, což je klíčové pro následnou demodulaci dat.

Tento přístup řešil omezení méně strukturovaných přístupových metod a poskytl standardizovaný mechanismus s nízkou režií, který je nezbytný pro provoz jakéhokoli buněčného systému. Jeho úspěch v GSM vedl k vývoji tohoto konceptu do struktur synchronizačních kanálů v UMTS, LTE a NR, kde základní požadavek na vyhrazený synchronizační signál zůstává, i když s různými implementacemi, jako jsou [PSS](/mobilnisite/slovnik/pss/) a [SSS](/mobilnisite/slovnik/sss/).

## Klíčové vlastnosti

- Nese známou tréninkovou sekvenci pro korelační detekci
- Umožňuje přesnou časovou synchronizaci (zarovnání na slot a snímek)
- Napomáhá odhadu a korekci frekvenčního posunu
- Vysílán periodicky pro podporu počátečního přístupu a převýběru buňky
- Navržen pro robustní detekci v prostředích s nízkým SNR a při vícecestném šíření
- Nese minimální systémové identifikační informace (např. BSIC v GSM)

## Související pojmy

- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.810** (Rel-8) — IMS Service Interaction Management Study
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [SB na 3GPP Explorer](https://3gpp-explorer.com/glossary/sb/)
