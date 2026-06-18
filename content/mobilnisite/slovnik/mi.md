---
slug: "mi"
url: "/mobilnisite/slovnik/mi/"
type: "slovnik"
title: "MI – Misleading Information"
date: 2025-01-01
abbr: "MI"
fullName: "Misleading Information"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mi/"
summary: "Misleading Information (MI) označuje falešná nebo klamná data vstřikovaná do bezdrátové sítě nebo v ní generovaná s úmyslem narušit provoz, snížit výkon nebo způsobit nesprávná rozhodnutí. Jde o klíčo"
---

MI je bezpečnostní hrozba v 3GPP, kdy jsou do bezdrátové sítě vstřikována falešná nebo klamná data s cílem narušit provoz, snížit výkon nebo způsobit nesprávná rozhodnutí, například zfalšování polohy UE.

## Popis

Misleading Information (MI) je široká kategorie bezpečnostních útoků definovaná v 3GPP, při které protivník (často označovaný jako útočník nebo škodlivý uživatel) úmyslně poskytuje, upravuje nebo generuje falešná data, která jsou zpracovávána síťovými prvky nebo uživatelským zařízením (UE). Hlavním cílem je uvést systém v omyl, aby činil nesprávná rozhodnutí, došlo ke snížení výkonu nebo k odepření služby. Útoky MI mohou cílít na různé síťové funkce, ale zvláštní důraz je kladen na kontext služeb polohování, navigace a časové synchronizace.

V kontextu polohování, například u LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo NR Positioning Protocol (NRPPa), se MI často projevuje jako falšování nebo manipulace s polohou. Útočník může vysílat padělané nebo znovu přehrávané polohové referenční signály (např. pro [OTDOA](/mobilnisite/slovnik/otdoa/) - Observed Time Difference of Arrival) nebo poskytovat uživatelskému zařízení (UE) zfalšovaná asistenční data. UE by při použití těchto zavádějících informací vypočítala nesprávnou geografickou polohu. Podobně může útočník poskytnout zavádějící informace síťové funkci Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) o měřeních UE, což způsobí, že síť odvodí chybnou polohu. Technické specifikace, jako je TS 38.857 (studie o NR polohování), tyto hrozby podrobně analyzují.

Mechanismy generování MI se liší. Mohou zahrnovat útoky na úrovni signálu, například generování rádiových signálů napodobujících legitimní základnové stanice (falešné gNB/[eNB](/mobilnisite/slovnik/enb/)) s manipulovaným časováním nebo obsahem. Mohou také zahrnovat útoky na úrovni protokolu, kdy jsou legitimní signalizační zprávy zachyceny a upraveny (útok typu man-in-the-middle) nebo zcela zfalšovány před vstříknutím do komunikačního proudu. Síť a UE musí používat protiopatření k detekci a zmírnění MI. Mezi ně patří kryptografické ověřování signalizačních zpráv (např. pomocí ochrany integrity), ověřování konzistence dat, používání více nezávislých polohovacích metod (např. kombinace [GNSS](/mobilnisite/slovnik/gnss/) s pozemními signály) a algoritmy detekce anomálií, které identifikují nepravděpodobné skoky v poloze nebo charakteristiky signálu.

Mimo polohování je MI obecným modelem hrozby použitelným pro další oblasti, jako je konfigurace sítě (poskytování falešných systémových informačních bloků), správa mobility (zasílání falešných povelů k předání spojení) nebo systémy správy. Bezpečnostní architektura 3GPP proto považuje ochranu proti MI za základní požadavek a ukládá bezpečnostní opatření, jako je ochrana integrity, ochrana proti přehrání a autorizační kontroly, aby byla zajištěna autenticita a spolehlivost kritických informací.

## K čemu slouží

Formální uznání a studium Misleading Information v rámci standardů 3GPP je hnáno rostoucí závislostí na bezdrátových sítích pro bezpečnostně kritické a vysoce přesné služby. Rané mobilní systémy se primárně zaměřovaly na hlas a základní přenos dat, kde bezpečnostní hrozby často představovalo odposlouchávání nebo krádež služby. Jak se sítě vyvíjely, aby podporovaly přesné polohové služby (pro tísňová volání, logistiku, automobilový průmysl), navigaci a vysoce automatizované procesy, důsledky přijetí falešných dat se staly závažnými.

MI řeší konkrétní mezeru v modelech hrozeb: útoky, které se nutně nesnaží prolomit důvěrnost nebo ukrást službu, ale zkorumpovat vnímání reality systémem. Například falšování polohy vozidla v systému [V2X](/mobilnisite/slovnik/v2x/) by mohlo způsobit katastrofické nehody. Manipulace s časovými signály by mohla narušit finanční transakce nebo synchronizaci energetické sítě. Vytvoření falešných konfiguračních dat sítě by mohlo vést k rozsáhlým výpadkům služeb. Tradiční bezpečnostní opatření, jako je samotné šifrování, jsou nedostatečná, protože MI může zahrnovat platně zašifrovaný, ale logicky nepravdivý obsah pocházející z kompromitované nebo falešné entity.

Proto 3GPP zahájila studie (např. v TS 38.857), aby systematicky analyzovala hrozby MI, zejména pro nové technologie, jako je 5G NR polohování. Cílem je definovat prostředí hrozeb, vyhodnotit potenciální dopady a standardizovat nezbytná bezpečnostní protiopatření v samotném návrhu protokolu. Tento proaktivní přístup „bezpečnost od návrhu“ zajišťuje, že funkce jako polohování jsou budovány s odolností proti klamání, což činí síť důvěryhodnou pro aplikace, kde je autenticita dat stejně důležitá jako dostupnost a důvěrnost.

## Klíčové vlastnosti

- Model bezpečnostní hrozby zahrnující poskytování falešných dat síti nebo UE
- Zvláště kritický pro služby polohování, navigace a časové synchronizace (PNT)
- Může se projevovat jako falšování polohy, přehrávání signálu nebo fabrikace dat
- Cílí na integritu a autenticitu informací, nikoli pouze na jejich důvěrnost
- Vyžaduje protiopatření jako kryptografická ochrana integrity a ověřování z více zdrojů
- Studován napříč více vydáními 3GPP, aby reagoval na vyvíjející se vektory útoků

## Definující specifikace

- **TS 23.090** (Rel-19) — USSD Stage 2 Specification
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [MI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mi/)
