---
slug: "srit"
url: "/mobilnisite/slovnik/srit/"
type: "slovnik"
title: "SRIT – Set of Radio Interface Technologies"
date: 2025-01-01
abbr: "SRIT"
fullName: "Set of Radio Interface Technologies"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srit/"
summary: "Definovaná kombinace více technologií rádiového přístupu (RAT), kterou může síť nebo zařízení podporovat současně nebo jako alternativy. Jedná se o konceptuální seskupení používané v síťovém plánování"
---

SRIT je definovaná kombinace více technologií rádiového přístupu, kterou může síť nebo zařízení podporovat; používá se pro plánování a specifikaci schopností s více technologiemi RAT.

## Popis

Sada technologií rádiového rozhraní (SRIT) je formalizovaný koncept v rámci 3GPP, který specifikuje konkrétní soubor technologií rádiového přístupu. Nejde o jediný protokol nebo rozhraní, ale o definovanou sadu používanou pro specifikaci požadavků, schopností a testovacích scénářů, zejména pro uživatelská zařízení (UE) a síťové uzly podporující více technologií [RAT](/mobilnisite/slovnik/rat/). SRIT explicitně uvádí, které technologie RAT jsou zahrnuty, například LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)), NR (New Radio), [UTRA](/mobilnisite/slovnik/utra/) ([WCDMA](/mobilnisite/slovnik/wcdma/)/[TD-SCDMA](/mobilnisite/slovnik/td-scdma/)) nebo dokonce GSM/[EDGE](/mobilnisite/slovnik/edge/) ([GERAN](/mobilnisite/slovnik/geran/)). Tato definice umožňuje přesné vyjádření toho, které kombinace technologií musí zařízení nebo síťová funkce podporovat. Například SRIT pro UE může být {LTE, NR}, což označuje zařízení schopné LTE-NR duální konektivity.

V praktické aplikaci se SRIT používá v několika klíčových oblastech. Za prvé, ve specifikacích pro [RF](/mobilnisite/slovnik/rf/) (Radio Frequency) certifikační testování (např. 3GPP TS 37.910) SRIT definuje kombinaci technologií RAT, pro kterou se testuje výkon vysílače a přijímače UE. Testy pokrývají scénáře, jako je simultánní vysílání/příjem na více technologiích RAT, a zajišťují, že nedochází k škodlivému rušení a že jsou splněny požadavky na výkon pro každou technologii RAT v sadě. Za druhé, ve specifikacích funkcí, jako je agregace nosných (CA) nebo duální konektivita (DC), může SRIT definovat přípustné nebo požadované kombinace technologií RAT pro dané nasazení funkce. To poskytuje jasný rámec pro interoperabilitu.

Z architektonického hlediska koncept SRIT reflektuje heterogenní povahu moderních sítí rádiového přístupu (HetNets). Posouvá se mimo specifikace pro jedinou technologii RAT a modeluje reálné prostředí, kde může být UE připojeno k LTE kotvící buňce a NR sekundární buňce, nebo může být schopno předání mezi nimi. SRIT je nástroj pro systémové návrháře a testovací inženýry k vytváření jednoznačných požadavků. Úzce souvisí s deklarovanými schopnostmi UE prostřednictvím signalizace RRC (Radio Resource Control) nebo procedur přenosu schopností UE, kde UE informuje síť o technologiích RAT a kombinacích pásem, které podporuje, což lze interpretovat jako jednu nebo více sad SRIT.

## K čemu slouží

Koncept SRIT byl zaveden, aby řešil rostoucí složitost zařízení a sítí s více technologiemi RAT. Před jeho formalizací se specifikace často zabývaly každou technologií RAT izolovaně. S příchodem funkcí jako agregace LTE-WLAN (LWA), duální konektivita LTE-NR (EN-DC) a později NR-NR DC však vznikla potřeba standardizovaného způsobu, jak odkazovat na specifické kombinace technologií a specifikovat pro ně požadavky. To bylo hnací silou snahy průmyslu o bezproblémový provoz s více technologiemi RAT, kde zařízení mohou využívat více rádiových spojení pro zvýšené přenosové rychlosti, spolehlivost a mobilitu.

Jeho vytvoření, zejména v Release 9 spolu s ranými pracemi na LTE-Advanced, poskytlo základní model pro definování chování UE a sítě v kontextu více technologií RAT. Vyřešil problém nejednoznačných odkazů na „vícemódová“ zařízení tím, že poskytl přesnou, vyčíslitelnou sadu. Tato přesnost je klíčová pro certifikační testování, protože zajišťuje, že zařízení, které deklaruje podporu LTE a NR společně, je testováno ve všech relevantních kombinovaných provozních scénářích, a ne pouze u každé technologie RAT samostatně. Také napomáhá síťovému plánování a vývoji funkcí tím, že jasně vymezuje, které kombinace technologií jsou předmětem konkrétní specifikace nebo možnosti nasazení sítě.

## Klíčové vlastnosti

- Formálně definuje konkrétní kombinaci technologií rádiového přístupu (např. {E-UTRA, NR})
- Slouží jako základ pro definování požadavků RF certifikačních testů pro UE s více technologiemi RAT
- Poskytuje jasný rozsah pro funkce jako agregace nosných a duální konektivita
- Umožňuje přesnou specifikaci schopností UE a požadavků sítě
- Podporuje testování simultánního vysílání a příjmu napříč různými technologiemi RAT
- Usnadňuje jednoznačnou komunikaci ve standardech a síťovém plánování

## Související pojmy

- [RAT – Radio Access Technology](/mobilnisite/slovnik/rat/)
- [E-UTRA – Enhanced Universal Terrestrial Radio Access](/mobilnisite/slovnik/e-utra/)

## Definující specifikace

- **TR 36.912** (Rel-19) — TR on LTE-Advanced (Further E-UTRA)
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.911** (Rel-19) — 3GPP 5G NTN Self-Evaluation Report

---

📖 **Anglický originál a plná specifikace:** [SRIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/srit/)
