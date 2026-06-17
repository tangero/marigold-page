---
slug: "mnrf"
url: "/mobilnisite/slovnik/mnrf/"
type: "slovnik"
title: "MNRF – Mobile station Not Reachable Flag"
date: 2025-01-01
abbr: "MNRF"
fullName: "Mobile station Not Reachable Flag"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnrf/"
summary: "Příznak uložený v HLR nebo HSS, který indikuje, že mobilní zařízení není v současnosti pro síť dosažitelné. Nastavuje se při selhání procedur iniciovaných sítí (např. pagingu), čímž se zabrání zbytečn"
---

MNRF je příznak uložený v HLR nebo HSS, který signalizuje, že mobilní zařízení není dosažitelné. Tím se zabrání zbytečné signalizaci a umožní optimalizované uložení zpráv při selhání pagingu sítě.

## Popis

Příznak nedosažitelnosti mobilní stanice (Mobile station Not Reachable Flag, MNRF) je parametr údajů o účastníkovi, který je udržován v domácím registru polohy ([HLR](/mobilnisite/slovnik/hlr/)) v sítích GSM/UMTS nebo na serveru domácích účastníků ([HSS](/mobilnisite/slovnik/hss/)) v sítích LTE/5G. Jedná se o booleovský indikátor (nastavený nebo vymazaný), který síti signalizuje, zda je mobilní stanice (UE) v daném okamžiku dosažitelná pro služby iniciované sítí (mobile-terminated), jako jsou hlasové hovory nebo SMS. Příznak nastavuje síť, konkrétně návštěvnický registr polohy (VLR) nebo entita [MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/), když zjistí, že UE není dosažitelná. K tomuto zjištění obvykle dojde po selhání procedury pagingu iniciované sítí – například proto, že UE je mimo pokrytí, vypnutá nebo se nachází v klidovém stavu [RRC](/mobilnisite/slovnik/rrc/) (radio resource control), kdy na ni nelze kontaktovat.

Fungování příznaku zahrnuje koordinovaný proces mezi obslužným síťovým uzlem a domácí databází. Když transakce iniciovaná sítí (např. požadavek na sestavení hovoru) dorazí ke vstupní [MSC](/mobilnisite/slovnik/msc/) nebo SMS routeru, ten se dotazuje HLR/HSS na směrovací informace. Pokud je MNRF nastaven, může HLR/HSS okamžitě informovat dotazující se entitu, že účastník není dosažitelný, a případně spustit alternativní procedury, jako je přesměrování hovoru na hlasovou schránku nebo uložení SMS v centru SMS (SMSC) s indikátorem 'čekající zpráva'. Odpovědnost za správu příznaku má obslužný uzel (VLR/MME/AMF) na základě své znalosti o dosažitelnosti UE. Nastaví MNRF prostřednictvím aktualizační procedury směrem k HLR/HSS při selhání pagingu a vymaže jej, když UE následně provede aktualizaci polohy, služební požadavek nebo jakoukoli jinou signalizační interakci, která potvrdí, že je zpět online.

Z architektonického hlediska je MNRF klíčovou součástí správy mobility a optimalizací pro úsporu energie. Zabrání síti plýtvat prostředky na opakované marné pokusy o paging nedosažitelné UE napříč více lokalizačními oblastmi. Místo toho může síť služby bufferovat, dokud není příznak vymazán. MNRF úzce souvisí s dalšími stavy účastníka, jako je časovač Mobile Reachable Timer a procedura implicitního odpojení (implicit detach). V systému 5G je podobná funkčnost řízena prostřednictvím stavů účastníka v [UDM](/mobilnisite/slovnik/udm/) (unified data repository) a oznámení o dosažitelnosti od AMF, čímž je zachováno stejné konceptuální chování pro optimalizaci signalizace a doručování služeb.

## K čemu slouží

MNRF existuje za účelem optimalizace efektivity síťové signalizace a zlepšení uživatelského zážitku u služeb iniciovaných sítí, když je účastník dočasně nedosažitelný. Bez takového příznaku by každý pokus o hovor nebo SMS iniciovaný sítí spustil plnou proceduru pagingu v celé poslední známé lokalizační oblasti, což by spotřebovávalo cenné prostředky rádiového přístupu i jádra sítě, i když je ze strany zařízení známo (z nedávných selhání), že je mimo pokrytí nebo vypnuté. To by vedlo ke zvýšení latence služeb, zbytečné zátěži síťových prvků a snížení výdrže baterie jiných UE kvůli nadměrnému vysílání pagingu.

Řeší problém plýtvání signalizací tím, že umožní síti 'zapamatovat si' stav nedosažitelnosti. Když je MNRF nastaven, může [HLR](/mobilnisite/slovnik/hlr/)/HSS poskytnout okamžitou zpětnou vazbu na pokusy o doručení služby, což umožní rychlé zpracování selhání nebo aktivaci mechanismů typu 'ulož a předej' (store-and-forward), jako je čekání na SMS. Vytváří tak efektivnější síť s lepším využitím zdrojů.

Koncept byl zaveden již v raných standardech GSM, aby řešil realitu mobilních sítí, kde se účastníci často pohybují mimo a zpět do pokrytí. Poskytuje standardizovaný způsob, jak může domácí síť být informována o stavu dosažitelnosti od návštěvnické sítě, což umožňuje konzistentní chování napříč nasazeními od více dodavatelů. Jeho vývoj do LTE a 5G dokazuje jeho trvalý význam při správě mobility a establishmentu relací v stále složitějších IP sítích a zajišťuje, že jsou zachovány základní principy síťové efektivity a spolehlivého doručování služeb.

## Klíčové vlastnosti

- Booleovský příznak uložený v HLR/HSS/UDM indikující stav dosažitelnosti UE
- Nastavován obslužným síťovým uzlem (VLR/MME/AMF) při selhání pagingu
- Vymazán, když UE úspěšně provede aktualizaci polohy nebo služební požadavek
- Umožňuje okamžitou síťovou odpověď na pokusy o služby iniciované sítí
- Snižuje zbytečnou signalizaci pagingu a zatížení sítě
- Umožňuje služby typu 'ulož a předej', jako je čekání na SMS

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.272** (Rel-19) — CS Fallback in EPS

---

📖 **Anglický originál a plná specifikace:** [MNRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnrf/)
