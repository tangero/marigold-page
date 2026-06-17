---
slug: "bwp"
url: "/mobilnisite/slovnik/bwp/"
type: "slovnik"
title: "BWP – Bandwidth Part"
date: 2026-01-01
abbr: "BWP"
fullName: "Bandwidth Part"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bwp/"
summary: "Bandwidth Part (BWP, část šířky pásma) je souvislá sada fyzických bloků zdrojů (PRB) nakonfigurovaná v rámci šířky pásma kanálu pro UE. Umožňuje energeticky účinný provoz tím, že umožňuje UE monitorov"
---

BWP (část šířky pásma) je souvislá sada fyzických bloků zdrojů nakonfigurovaná v rámci šířky pásma kanálu, která umožňuje energeticky účinný provoz tím, že umožňuje UE monitorovat pouze podmnožinu celkové šířky pásma.

## Popis

Bandwidth Part (BWP, část šířky pásma) je základní koncept v 5G New Radio (NR), který definuje souvislou podmnožinu celkové šířky pásma kanálu přidělenou uživatelskému zařízení (UE). Na rozdíl od LTE, kde UE typicky pracují na celé šířce pásma nosné, NR zavádí BWP pro zajištění větší flexibility a účinnosti. Každý BWP je charakterizován svou numerologií (rozestup podnosných a cyklická předpona), šířkou pásma (počet PRB) a frekvenční polohou v rámci nosné. UE může být nakonfigurováno až se čtyřmi downlink BWP a čtyřmi uplink BWP na obsluhovanou buňku, ale v daném okamžiku může být aktivní pouze jeden downlink BWP a jeden uplink BWP. Tato konfigurace umožňuje síti dynamicky se přizpůsobovat různým požadavkům služeb a schopnostem UE.

Provoz BWP je řízen signalizací Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro polostatickou konfiguraci a pomocí Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) pro dynamické přepínání. Když je UE nakonfigurováno s více BWP, monitoruje Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) pouze v rámci aktivního BWP, což výrazně snižuje spotřebu energie. Mechanismus přepínání BWP umožňuje síti přesouvat UE mezi různými šířkami pásma a numerologiemi na základě stavu provozu, požadavků služeb nebo hledisek úspory energie. Například UE může pracovat na úzkém BWP pro základní konektivitu a operace v režimu nečinnosti a poté přepnout na širší BWP pro relace s vysokou propustností dat.

Z architektonického hlediska konfigurace BWP zahrnuje parametry jako pole locationAndBandwidth (udávající počáteční PRB a šířku pásma v PRB), subcarrierSpacing a cyclicPrefix. Počáteční BWP je konfigurován pro procedury počátečního přístupu včetně synchronizace a náhodného přístupu. Výchozí BWP se používá pro záložní provoz, když po konfigurovanou dobu časovače nedochází k přenosu dat. Časovač nečinnosti BWP spustí přepnutí na výchozí BWP, když UE po stanovenou dobu nepřijímalo plánování, což dále zvyšuje energetickou účinnost.

BWP hraje klíčovou roli při podpoře různorodých scénářů spektra v 5G NR. Umožňuje provoz v nosných se širokou šířkou pásma (až 400 MHz v FR2) a zároveň akomoduje UE s omezenými RF schopnostmi. Technologie podporuje scénáře smíšené numerologie, kde různé služby (eMBB, URLLC, mMTC) mohou být multiplexovány na stejné nosné prostřednictvím různých BWP. BWP také usnadňuje sdílení spektra mezi různými operátory nebo mezi 4G a 5G prostřednictvím pečlivé konfigurace BWP, která se vyhýbá oblastem rušení.

Implementace BWP zahrnuje koordinaci mezi více vrstvami protokolu. Na fyzické vrstvě BWP definuje skutečnou šířku pásma pro přenos a příjem. Na vrstvě [MAC](/mobilnisite/slovnik/mac/) probíhají procedury přepínání BWP a správa časovačů. RRC se zabývá konfigurací a rekonfigurací parametrů BWP. Tento vícevrstvý přístup zajišťuje, že operace BWP jsou synchronizovány napříč zásobníkem protokolů, čímž se zachovává kontinuita služeb při optimalizaci využití zdrojů a spotřeby energie.

## K čemu slouží

Bandwidth Part (část šířky pásma) byl zaveden v 5G NR, aby řešil několik omezení předchozích buněčných systémů, zejména pevného provozu na šířce pásma v LTE. V LTE UE typicky pracovala na celé šířce pásma nosné bez ohledu na jejich skutečné požadavky na data, což vedlo ke zbytečné spotřebě energie. To se stalo obzvláště problematickým se zavedením nosných se širokou šířkou pásma v 5G (až 100 MHz v FR1 a 400 MHz ve FR2), kde by vyžadování monitorování celé šířky pásma u všech UE bylo nepraktické a energeticky neúčinné.

Primární motivací pro vytvoření BWP bylo umožnit energeticky účinný provoz pro UE, zejména ta podporující nosné se širokou šířkou pásma. Tím, že umožňuje UE monitorovat pouze podmnožinu celkové šířky pásma, když se nevěnují činnostem s vysokou propustností, BWP výrazně snižuje spotřebu energie. To je klíčové pro mobilní zařízení, kde je výdrž baterie hlavním faktorem. Dále BWP podporuje různorodé schopnosti UE tím, že umožňuje zařízením s různými RF schopnostmi pracovat na stejné nosné prostřednictvím vhodně nakonfigurovaných částí šířky pásma.

Dalším klíčovým problémem, který BWP řeší, je efektivní podpora smíšených služeb a numerologií v rámci stejné nosné. 5G NR zavedlo flexibilní numerologii s různými rozestupy podnosných (15, 30, 60, 120, 240 kHz) pro podporu různorodých případů užití. BWP umožňuje různým službám (např. eMBB se širokou šířkou pásma a mMTC s úzkou šířkou pásma) koexistovat na stejné nosné tím, že jsou jim přiděleny různé BWP s vhodnými numerologiemi. Tato flexibilita nebyla v předchozích generacích dostupná a představuje významný pokrok v účinnosti využití spektra.

## Klíčové vlastnosti

- Podporuje až čtyři konfigurovatelné BWP na obsluhovanou buňku v downlinku a uplinku
- Umožňuje dynamické přepínání BWP prostřednictvím DCI pro rychlou adaptaci na podmínky provozu
- Snižuje spotřebu energie UE prostřednictvím úzkopásmového monitorování během období nízké aktivity
- Usnadňuje provoz se smíšenou numerologií v rámci stejné šířky pásma nosné
- Podporuje různorodé schopnosti UE prostřednictvím konfigurace adaptivní na šířku pásma
- Poskytuje záložní mechanismus prostřednictvím výchozího BWP a časovače nečinnosti

## Definující specifikace

- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [BWP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bwp/)
