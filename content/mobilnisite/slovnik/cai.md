---
slug: "cai"
url: "/mobilnisite/slovnik/cai/"
type: "slovnik"
title: "CAI – Channel Assignment Indicator"
date: 2025-01-01
abbr: "CAI"
fullName: "Channel Assignment Indicator"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cai/"
summary: "Signalizační mechanismus v UMTS, který indikuje, zda byl uživatelskému zařízení přidělen vyhrazený fyzický kanál. Umožňuje efektivní přidělování kanálů a správu zdrojů tím, že poskytuje explicitní inf"
---

CAI je signalizační mechanismus v UMTS, který indikuje, zda byl uživatelskému zařízení přidělen vyhrazený fyzický kanál, což umožňuje efektivní správu zdrojů během navazování spojení a přechodu mezi buňkami.

## Popis

Channel Assignment Indicator (CAI) je základní signalizační prvek v protokolovém zásobníku rádiového rozhraní UMTS (Universal Mobile Telecommunications System), který konkrétně funguje na fyzické vrstvě podle specifikací 3GPP. Funguje jako binární indikátor vysílaný z Node B k uživatelskému zařízení (UE), který explicitně sděluje, zda byl pro použití UE úspěšně alokován a přidělen vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)). Tento indikátor je klíčový během důležitých procedur správy rádiových zdrojů, jako je zřizování rádiového beareru, rekonfigurace a události přechodu mezi buňkami, kdy UE přechází mezi různými konfiguracemi kanálů nebo oblastmi pokrytí buněk.

Z architektonického hlediska je CAI implementován v rámci struktury fyzického kanálu rádiového rozhraní UMTS, konkrétně je spojen s Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)). DPCCH přenáší řídicí informace vrstvy 1, včetně pilotních bitů pro odhad kanálu, příkazů pro řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)) a volitelně Transport Format Combination Indicator ([TFCI](/mobilnisite/slovnik/tfci/)). V určitých konfiguracích a scénářích jsou pro přenos CAI využita specifická pole nebo bitové vzorce v rámci rámcové struktury DPCCH. Síť (Node B) nastaví hodnotu CAI na základě výsledku svých interních algoritmů pro přidělování kanálů a kontrol dostupnosti zdrojů a poté ji vysílá k UE. Fyzická vrstva UE přijme a dekóduje CAI a předá indikaci stavu přidělení vyšším vrstvám ([MAC](/mobilnisite/slovnik/mac/) a [RRC](/mobilnisite/slovnik/rrc/)), které následně řídí chování při přenosu.

Z provozního hlediska CAI funguje ve spolupráci s dalšími řídicími signály vrstvy 1 a signalizací vyšší vrstvy Radio Resource Control (RRC). Když vrstva RRC nařídí přechod vyžadující nový vyhrazený kanál, UE začne monitorovat CAI na přidělených zdrojích fyzického kanálu. Pozitivní CAI (typicky '1' nebo specifický bitový vzor) informuje UE, že kanál je skutečně přidělen a aktivní, a autorizuje jej k zahájení vysílání na přidruženém Dedicated Physical Data Channel ([DPDCH](/mobilnisite/slovnik/dpdch/)). Negativní nebo chybějící CAI indikuje, že přidělení kanálu selhalo nebo čeká na vyřízení, což přiměje UE buď počkat, nebo přejít k alternativním procedurám, jako je návrat na společné kanály nebo zahájení opětovného zřízení. Tento mechanismus zabraňuje UE vysílat na zdrojích, které síť ještě nezfinalizovala, a předchází tak rušení a konfliktům zdrojů.

Role CAI se rozšiřuje na správu mobility, zejména během měkkých a tvrdých přechodů mezi buňkami. Když se UE pohybuje a mění se její aktivní sada buněk, obsluhující a cílové Node B koordinují přidělování kanálů. CAI poskytuje UE jasné potvrzení s nízkou latencí o tom, který nově přidělený kanál buňky je připraven k použití, a usnadňuje tak plynulé přechody. Dále, v kontextu měření a reportování, může spolehlivost dekódování CAI ovlivnit odhady kvality kanálu a následné úpravy řízení výkonu. Integrace CAI do návrhu fyzické vrstvy UMTS odráží rovnováhu mezi explicitní řídicí signalizací a efektivním využitím vzácných rádiových zdrojů, čímž zajišťuje synchronizované porozumění stavu kanálů mezi síťovou infrastrukturou a mobilními terminály.

## K čemu slouží

CAI byl vytvořen k řešení základní výzvy spolehlivé a jednoznačné koordinace přidělování kanálů mezi sítí UMTS a uživatelským zařízením v dynamickém rádiovém prostředí. Před 3GPP Release 4 se správa kanálů více spoléhala na signalizaci vyšších vrstev a implicitní časovače, což mohlo vést k selhání synchronizace, zbytečnému rušení nebo přerušení hovoru, pokud měly UE a síť rozdílnou představu o dostupnosti kanálu. Explicitní mechanismus CAI poskytuje potvrzení s nízkou latencí na fyzické vrstvě, které odstraní nejednoznačnost, a zajišťuje, že UE začne vysílat na vyhrazeném fyzickém kanálu až po obdržení explicitní autorizace od sítě.

Primární problém, který CAI řeší, je problém 'handshake při přidělování kanálu'. Během zřizování rádiového beareru, rekonfigurace nebo přechodu mezi buňkami se funkce správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) sítě rozhodne alokovat vyhrazený kanál. Mezi tím, kdy signalizace RRC nařídí UE použít kanál, a tím, kdy plánovač a hardware Node B skutečně nakonfigurují a aktivují tento kanál, však existuje časová mezera. Bez CAI by UE mohlo začít vysílat pouze na základě příkazů RRC, což by potenciálně mohlo způsobit kolize, pokud Node B ještě není připraveno přijímat. CAI tuto smyčku uzavírá tím, že poskytuje přímý signál 'povolit/zakázat' na fyzické vrstvě od Node B k UE, synchronizovaný se skutečnou dostupností kanálu.

Historicky motivace pro CAI vycházela ze zvýšené složitosti UMTS založeného na WCDMA ve srovnání se sítí GSM. UMTS zavedlo proměnné spreading faktory, rychlé řízení výkonu a měkký přechod mezi buňkami, což činí stav kanálu dynamičtějším. CAI jako součást řídicího kanálu DPCCH se stal nezbytnou součástí pro robustní provoz, zejména pro služby s přísnými požadavky na zpoždění, jako je hlas a video v reálném čase. Umožnil síti udržovat těsnou kontrolu nad využitím zdrojů a zároveň poskytovat UE jasnou okamžitou zpětnou vazbu, čímž se zlepšila celková kapacita systému, úspěšnost navazování hovorů a spolehlivost přechodů mezi buňkami v raných sítích 3G.

## Klíčové vlastnosti

- Binární indikátor na fyzické vrstvě vysílaný z Node B k UE
- Poskytuje explicitní potvrzení přidělení vyhrazeného fyzického kanálu (DPCH)
- Integrální součást struktury Dedicated Physical Control Channel (DPCCH)
- Umožňuje synchronizovanou aktivaci kanálu mezi sítí a terminálem
- Podporuje spolehlivé procedury zřizování a rekonfigurace rádiového beareru
- Usnadňuje koordinované použití kanálů během měkkých a tvrdých přechodů mezi buňkami

## Související pojmy

- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [CAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cai/)
